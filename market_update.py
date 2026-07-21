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
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=%5EGSPC&region=US&lang=en-US",
]

MAX_HEADLINES = 6
MAX_PER_FEED = 3


# ---------------------------------------------------------------------------
# Data fetching
# ---------------------------------------------------------------------------

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
            closes = (data[sym]["Close"] if len(symbols) > 1 else data["Close"]).dropna()
            if len(closes) >= 2:
                last, prev = float(closes.iloc[-1]), float(closes.iloc[-2])
                quotes[sym] = (last, (last - prev) / prev * 100.0)
            elif len(closes) == 1:
                quotes[sym] = (float(closes.iloc[-1]), None)
        except (KeyError, IndexError, TypeError):
            pass
    return quotes


def fetch_headlines():
    """Return up to MAX_HEADLINES headline strings from the news feeds."""
    headlines = []
    for url in NEWS_FEEDS:
        try:
            resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            from_this_feed = 0
            for item in root.iter("item"):
                title = item.findtext("title", "").strip()
                if title and title not in headlines:
                    headlines.append(title)
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
        news += [f"• {html.escape(h)}" for h in headlines]
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
