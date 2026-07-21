# Stock Market Update

Sends a brief daily global market digest to a Telegram chat via GitHub Actions.
Designed to be read in a minute or two.

## What's in the digest

- US indices (previous close) and live US futures
- A configurable stock watchlist
- Europe & Asia indices
- Crypto, commodities, and FX
- A few top market headlines

Data comes from Yahoo Finance (via `yfinance`) and public RSS feeds — free, no API key needed.

## Setup

1. Create a Telegram bot with [@BotFather](https://t.me/BotFather) and note the bot token
2. Message your bot once, then get your chat ID (e.g. via `https://api.telegram.org/bot<TOKEN>/getUpdates`)
3. Add two repository secrets under **Settings → Secrets and variables → Actions**:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
4. Trigger a test from **Actions → Daily Market Update → Run workflow**

The workflow then runs automatically on its daily schedule.

## Running locally

```bash
pip install -r requirements.txt
python market_update.py --dry-run          # print the message, don't send
TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=... python market_update.py
```

## Customising

- **Watchlist / indices** — edit the lists at the top of `market_update.py`
- **Schedule** — edit the `cron` line in `.github/workflows/daily-market-update.yml` (times are UTC)
- **Weekends** — sends every day by default; change the cron to `0 6 * * 1-5` to skip weekends
