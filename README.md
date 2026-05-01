# DeDollar Stock Monitor

A professional stock monitoring dashboard for 4 DeDollarisation-safe Indian small caps
filtered through Vijay Kedia's SMILE Framework.

## Monitored Stocks
- HBL Engineering (HBLPOWER.NS) — Defence & Railway Electronics
- Sandur Manganese (SANDUMA.NS) — Mining & Value-Added Steel  
- Shivalik Bimetal Controls (SHIVALIK.NS) — Precision Bimetals & EV Shunts
- Elecon Engineering (ELECONT.NS) — Industrial Gears & Material Handling

## Quick Start

### Option 1 — Open directly in browser (no server needed)
Just open `index.html` in your browser. All market data is fetched client-side from Yahoo Finance.

### Option 2 — Run with Flask server (recommended)
```bash
pip install flask
python3 run.py
# Opens http://localhost:5000 automatically
```

## Features
- Live NSE/BSE price data (via Yahoo Finance)
- Configurable price drop alerts (5%, 10%, 15%, custom %)
- Financial health drill-down for each stock
- SMILE Framework algorithm explained
- DeDollarisation safety analysis
- 10-year return projections (bear/base/bull)
- Auto-refresh (configurable 30s to 15min)

## Hosting Online (free options)

### Vercel (recommended — zero config)
1. Push to GitHub
2. Connect repo at vercel.com
3. Done — live in 60 seconds

### Railway.app
1. `railway login && railway init && railway up`

### Render.com
- Set start command: `python3 server.py`
- Set port: 5000

## Data Source
Yahoo Finance (free, no API key needed). Data fetched in your browser.
If Yahoo Finance is blocked, the app uses realistic simulated prices.
