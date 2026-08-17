#!/usr/bin/env python3
"""Daily global market digest, delivered via Telegram.

Pulls quotes from Yahoo Finance and top headlines from CNBC/Yahoo RSS,
formats a short briefing (1-2 minute read), and sends it to a Telegram chat.

Usage:
    python market_update.py            # send to Telegram (needs env vars)
    python market_update.py --dry-run  # print the message instead of sending

Required environment variables (for sending):
    TELEGRAM_BOT_TOKEN  - bot token from @BotFather
    TELEGRAM_CHAT_ID    - target chat id
"""

import os
import re
import sys
import html
import datetime as dt
import xml.etree.ElementTree as ET

import requests
import yfinance as yf

# ---------------------------------------------------------------------------
# What we track
# ---------------------------------------------------------------------------

US_INDICES = [
    ("^GSPC", "S&P 500"),
    ("^IXIC", "Nasdaq"),
    ("^DJI", "Dow"),
]

US_FUTURES = [
    ("ES=F", "S&P fut"),
    ("NQ=F", "Nasdaq fut"),
]

TECH_STOCKS = [
    ("AAPL", "Apple"),
    ("MSFT", "Microsoft"),
    ("NVDA", "Nvidia"),
    ("AMZN", "Amazon"),
    ("GOOGL", "Alphabet"),
    ("META", "Meta"),
    ("TSLA", "Tesla"),
    ("AMD", "AMD"),
    ("AVGO", "Broadcom"),
    ("TSM", "TSMC"),
    ("PLTR", "Palantir"),
]

GLOBAL_INDICES = [
    ("^FTSE", "FTSE 100"),
    ("^GDAXI", "DAX"),
    ("^N225", "Nikkei"),
    ("^HSI", "Hang Seng"),
]

CRYPTO = [
    ("BTC-USD", "Bitcoin"),
    ("ETH-USD", "Ethereum"),
]

COMMODITIES_FX = [
    ("GC=F", "Gold"),
    ("CL=F", "WTI Oil"),
    ("DX-Y.NYB", "Dollar idx"),
]

NEWS_FEEDS = [
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",  # CNBC Markets
    "https://feeds.bbci.co.uk/news/business/rss.xml",  # BBC Business
    "https://feeds.content.dowjones.io/public/rss/mw_topstories",  # MarketWatch
]

MAX_HEADLINES = 6
MAX_PER_FEED = 3


# ---------------------------------------------------------------------------
# Data fetching
# ---------------------------------------------------------------------------

def _quote_from_closes(closes):
    """Turn a close-price series into (last, pct_change) or None."""
    closes = closes.dropna()
    if len(closes) >= 2:
        last, prev = float(closes.iloc[-1]), float(closes.iloc[-2])
        return last, (last - prev) / prev * 100.0
    if len(closes) == 1:
        return float(closes.iloc[-1]), None
    return None


def fetch_quotes(pairs):
    """Return {symbol: (last_price, pct_change)} for a list of (symbol, label)."""
    symbols = [s for s, _ in pairs]
    data = yf.download(
        symbols, period="5d", interval="1d",
        group_by="ticker", progress=False, threads=True,
    )
    quotes = {}
    for sym in symbols:
        try:
            closes = data[sym]["Close"] if len(symbols) > 1 else data["Close"]
            quote = _quote_from_closes(closes)
            if quote:
                quotes[sym] = quote
        except (KeyError, IndexError, TypeError):
            pass

    # The batch download intermittently drops symbols; retry the misses one
    # at a time, which usually succeeds.
    for sym in symbols:
        if sym in quotes:
            continue
        try:
            hist = yf.Ticker(sym).history(period="5d", interval="1d")
            quote = _quote_from_closes(hist["Close"])
            if quote:
                quotes[sym] = quote
        except Exception as exc:  # a single dud symbol shouldn't break the run
            print(f"warning: quote retry failed {sym}: {exc}", file=sys.stderr)
    return quotes


def is_clickbait(title):
    """Filter out listicle/SEO filler so only real news gets through."""
    lower = title.lower()
    spam_markers = (
        "better buy", "should you buy", "is it time to", "here's why",
        "heres why", "vs.", " etf", "motley fool", "zacks", "top stocks",
        "stocks to", "reasons to", "prediction:", "if you'd invested",
    )
    return "?" in title or any(m in lower for m in spam_markers)


# A headline must mention at least one of these to count as market news.
# Single words are matched as whole words; phrases as substrings.
MARKET_WORDS = {
    # markets & macro
    "stock", "stocks", "shares", "market", "markets", "nasdaq", "s&p",
    "dow", "invest", "investor", "investors", "trader", "traders",
    "trading", "bond", "bonds", "yield", "yields", "treasury", "ipo",
    "earnings", "revenue", "profit", "profits", "valuation", "merger",
    "acquisition", "acquires", "buyback", "dividend", "fed", "inflation",
    "cpi", "gdp", "recession", "tariff", "tariffs", "economy", "economic",
    "ecb", "unemployment", "payrolls",
    # assets
    "bitcoin", "crypto", "ethereum", "opec", "crude", "dollar", "currency",
    "fx", "gold", "oil",
    # the watchlist & big tech
    "apple", "microsoft", "nvidia", "amazon", "alphabet", "google",
    "meta", "tesla", "amd", "broadcom", "tsmc", "palantir", "intel",
    "openai", "anthropic", "chip", "chips", "chipmaker", "semiconductor",
    "ai",
}

MARKET_PHRASES = (
    "wall street", "hedge fund", "short sell", "federal reserve",
    "rate cut", "rate hike", "interest rate", "trade deal", "trade war",
    "central bank", "bank of england", "jobs report", "big tech",
)

# Human-interest / lifestyle markers that veto a headline even when it
# happens to contain a market keyword (e.g. an "AI" story about a shopper).
# Whole-word matches to avoid false hits ("pet" inside "Peter").
NON_MARKET_VETO_WORDS = {
    "shopper", "shoppers", "shoplifter", "ejected", "arrested", "outbreak",
    "rental", "tenant", "pet", "pets", "recipe", "holiday", "tourist",
    "celebrity", "royal", "footballer", "olympic", "olympics", "weather",
    "wedding",
}
NON_MARKET_VETO_PHRASES = ("world cup",)


def _tokens(text):
    return {w.strip(".,:;!'\"’‘()") for w in text.lower().split()}


def is_market_relevant(title):
    lower = title.lower()
    tokens = _tokens(lower)
    if tokens & NON_MARKET_VETO_WORDS or any(p in lower for p in NON_MARKET_VETO_PHRASES):
        return False
    return bool(tokens & MARKET_WORDS) or any(p in lower for p in MARKET_PHRASES)


def is_near_duplicate(title, picked):
    """True if this headline covers the same story as one already picked."""
    stop = {"the", "a", "an", "of", "to", "in", "on", "for", "and", "as",
            "at", "with", "over", "after", "is", "are", "its", "his", "her",
            "new", "us", "u.s.", "says", "say"}
    words = {w.strip(".,:;'\"’‘") for w in title.lower().split()} - stop
    for other in picked:
        other_words = {w.strip(".,:;'\"’‘") for w in other.lower().split()} - stop
        if len(words & other_words) >= 3:
            return True
    return False


SUMMARY_MAX_CHARS = 180


def clean_summary(raw, title):
    """Turn a raw RSS description into a short plain-text context line.

    Returns "" if the description is empty or adds nothing beyond the title.
    """
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)          # strip HTML tags
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    # Some feeds prefix the summary with the source or repeat the title.
    text = re.sub(r"^(continue reading|read more)[.:\s-]*", "", text, flags=re.I)
    if not text:
        return ""
    # Skip summaries that just echo the headline.
    if text.lower().startswith(title.lower()[:40]):
        return ""
    if len(text) > SUMMARY_MAX_CHARS:
        cut = text[:SUMMARY_MAX_CHARS].rsplit(" ", 1)[0].rstrip(",;:")
        text = cut + "…"
    return text


def fetch_headlines():
    """Return up to MAX_HEADLINES (title, summary) pairs from the feeds."""
    headlines = []
    titles = []
    for url in NEWS_FEEDS:
        try:
            resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            from_this_feed = 0
            for item in root.iter("item"):
                title = item.findtext("title", "").strip()
                if (title and not is_clickbait(title)
                        and is_market_relevant(title)
                        and not is_near_duplicate(title, titles)):
                    summary = clean_summary(item.findtext("description", ""), title)
                    headlines.append((title, summary))
                    titles.append(title)
                    from_this_feed += 1
                if len(headlines) >= MAX_HEADLINES or from_this_feed >= MAX_PER_FEED:
                    break
            if len(headlines) >= MAX_HEADLINES:
                return headlines
        except Exception as exc:  # a dead feed shouldn't kill the digest
            print(f"warning: feed failed {url}: {exc}", file=sys.stderr)
    return headlines


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def arrow(pct):
    if pct is None:
        return "•"
    if pct >= 1.5:
        return "🚀"
    if pct > 0:
        return "🟢"
    if pct <= -1.5:
        return "🔻"
    if pct < 0:
        return "🔴"
    return "⚪"


def fmt_price(value):
    if value >= 1000:
        return f"{value:,.0f}"
    return f"{value:,.2f}"


def fmt_line(label, quote):
    if quote is None:
        return f"• {label}: n/a"
    price, pct = quote
    pct_str = f"{pct:+.1f}%" if pct is not None else "—"
    return f"{arrow(pct)} {label}: {fmt_price(price)} ({pct_str})"


def section(title, pairs, quotes):
    lines = [f"<b>{title}</b>"]
    for sym, label in pairs:
        lines.append(fmt_line(label, quotes.get(sym)))
    return "\n".join(lines)


def build_message():
    all_pairs = US_INDICES + US_FUTURES + TECH_STOCKS + GLOBAL_INDICES + CRYPTO + COMMODITIES_FX
    quotes = fetch_quotes(all_pairs)
    headlines = fetch_headlines()

    today = dt.datetime.now(dt.timezone.utc).strftime("%a %d %b %Y")
    parts = [f"📊 <b>Market Update — {today}</b>"]

    parts.append(section("🇺🇸 US Markets (prev close)", US_INDICES, quotes))
    parts.append(section("⏳ US Futures (live)", US_FUTURES, quotes))
    parts.append(section("💻 Tech Watchlist", TECH_STOCKS, quotes))
    parts.append(section("🌍 Europe & Asia", GLOBAL_INDICES, quotes))
    parts.append(section("₿ Crypto", CRYPTO, quotes))
    parts.append(section("🛢 Commodities & FX", COMMODITIES_FX, quotes))

    if headlines:
        news = ["<b>📰 Headlines</b>"]
        for title, summary in headlines:
            line = f"• <b>{html.escape(title)}</b>"
            if summary:
                line += f"\n  {html.escape(summary)}"
            news.append(line)
        parts.append("\n".join(news))

    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Delivery
# ---------------------------------------------------------------------------

def send_telegram(message):
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        sys.exit("error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set")
    resp = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=30,
    )
    if not resp.ok:
        sys.exit(f"error: Telegram API returned {resp.status_code}: {resp.text}")
    print("Update sent.")


def main():
    message = build_message()
    if "--dry-run" in sys.argv:
        print(message)
    else:
        send_telegram(message)


if __name__ == "__main__":
    main()
