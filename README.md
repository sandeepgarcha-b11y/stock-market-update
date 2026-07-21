# Stock Market Update

A daily global market digest delivered to Telegram every morning (~7am UK time).
Brief enough to read in a minute or two, with a bias toward US tech.

## What's in the digest

- 🇺🇸 **US markets** — S&P 500, Nasdaq, Dow (previous close)
- ⏳ **US futures** — live S&P and Nasdaq futures, so you know where things are heading pre-open
- 💻 **Tech watchlist** — Magnificent 7 (Apple, Microsoft, Nvidia, Amazon, Alphabet, Meta, Tesla) plus AMD, Broadcom, TSMC, Palantir
- 🌍 **Europe & Asia** — FTSE 100, DAX, Nikkei, Hang Seng
- ₿ **Crypto** — Bitcoin, Ethereum
- 🛢 **Commodities & FX** — Gold, WTI oil, Dollar index
- 📰 **Headlines** — top 3 market stories from CNBC/Yahoo Finance

Data comes from Yahoo Finance (via `yfinance`) — free, no API key needed.

## One-time setup

### 1. Create a Telegram bot

1. In Telegram, message [@BotFather](https://t.me/BotFather) and send `/newbot`
2. Follow the prompts; copy the **bot token** it gives you
3. Start a chat with your new bot (press **Start** / send any message)

### 2. Get your chat ID

Visit (with your token substituted in):

```
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

Find `"chat":{"id": ...}` in the response — that number is your **chat ID**.

### 3. Add repository secrets

In this repo on GitHub: **Settings → Secrets and variables → Actions → New repository secret**

| Secret | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | the token from BotFather |
| `TELEGRAM_CHAT_ID` | your chat ID |

### 4. Test it

Go to **Actions → Daily Market Update → Run workflow** to trigger a test run.
After that it runs automatically every day at 06:00 UTC.

## Running locally

```bash
pip install -r requirements.txt
python market_update.py --dry-run          # print the message, don't send
TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=... python market_update.py
```

## Customising

- **Watchlist / indices** — edit the lists at the top of `market_update.py`
- **Schedule** — edit the `cron` line in `.github/workflows/daily-market-update.yml`
  (times are UTC; GitHub cron can drift a few minutes)
- **Weekends** — it currently sends every day; on weekends stock prices show
  Friday's close but crypto stays live. To skip weekends change the cron to
  `0 6 * * 1-5`.
