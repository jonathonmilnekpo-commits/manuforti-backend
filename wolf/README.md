# Wolf - Autonomous Polymarket Trading Agent

**Phase 1: Paper Trading Architecture**

## Overview

Wolf is a fully autonomous trading agent for Polymarket prediction markets. It runs multiple strategies in parallel, enforces hard risk limits, and operates 24/7 without human intervention.

**Status:** Phase 1 (paper trading) - No real money at risk

## Architecture

```
wolf/
├── core/
│   ├── config.py           # Portfolio, Guardrails, Logger, constants
│   ├── polymarket_client.py # Polymarket API wrapper
│   └── engine.py           # Main trading engine
├── strategies/
│   └── base.py             # Strategy base class + 4 strategies
├── cli.py                  # Command line interface
└── logs/                   # Trading logs (created at runtime)
```

## Strategies

1. **Information Arbitrage** - Speed of information processing
2. **Mispricing Detection** - Superior probabilistic reasoning
3. **Market Making** - Providing liquidity in thin markets
4. **Correlation Exploitation** - Understanding conditional probabilities

## Guardrails (Hard Limits)

| Limit | Value | Action |
|-------|-------|--------|
| Max position | 5% of bankroll | Reject trade |
| Max daily loss | 10% | Halt 24h |
| Max drawdown | 25% | Halt, require reset |
| Min bankroll | $100 | Stop all trading |
| Max trades/day | 50 | Reject trades |
| Max open positions | 20 | Close oldest |

## Usage

### Run single cycle (paper trading)
```bash
cd /Users/jonathonmilne/.openclaw/workspace/wolf
python3 -m wolf.cli cycle --bankroll 500
```

### Run continuously
```bash
python3 -m wolf.cli start --bankroll 500 --interval 300
```

### Check status
```bash
python3 -m wolf.cli status
```

### Emergency halt
```bash
python3 -m wolf.cli halt --reason "Manual stop"
```

### Reset after halt
```bash
python3 -m wolf.cli reset
# Type 'WOLF_RESET' to confirm
```

## Phase 1: Paper Trading

In Phase 1, Wolf simulates trading using real Polymarket data but no real money:
- Fetches live market data from Polymarket
- Runs strategies to identify opportunities
- Simulates trade execution
- Tracks simulated P&L
- Enforces all guardrails

**No wallet required. No API key required for read-only access.**

## Phase 2: Live Trading (Future)

When ready for live trading:
1. Create Safe wallet (multi-sig)
2. Fund with starting bankroll ($500)
3. Add API key for trade execution
4. Update `polymarket_client.py` with wallet integration
5. Deploy to Railway/Render
6. Start with `--live` flag

## Monitoring

Logs are written to `logs/wolf_YYYY-MM-DD.jsonl`:
- Every trade (executed or rejected)
- Every guardrail check
- Portfolio snapshots
- AI decisions

Daily reports sent via Telegram (configure in production).

## Next Steps

1. [ ] Test paper trading locally
2. [ ] Validate strategies against historical data
3. [ ] Tune guardrail parameters
4. [ ] Add Telegram alerts
5. [ ] Deploy to Railway
6. [ ] Run paper trading for 2-4 weeks
7. [ ] If profitable: proceed to Phase 2 (live)

## Commands for Jonathon

```bash
# Navigate to wolf directory
cd /Users/jonathonmilne/.openclaw/workspace/wolf

# Run one cycle (safe, no risk)
python3 -m wolf.cli cycle

# Check what Wolf would do
python3 -m wolf.cli status

# Run continuously (Ctrl+C to stop)
python3 -m wolf.cli start
```

---

*Wolf v0.1 - Phase 1 Paper Trading*
*Built: March 13, 2026*
