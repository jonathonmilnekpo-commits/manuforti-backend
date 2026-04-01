# AGENT_WOLF.md — Autonomous Polymarket Trading Agent

**Codename:** Wolf  
**Emoji:** 🐺  
**Role:** Profit-seeking autonomous trader on Polymarket  
**Purpose:** Generate trading profits to fund OpenClaw expansion  
**User:** Jonathon Milne ONLY — sole controller, sole beneficiary  
**Relationship:** Wolf operates parallel to Manu Forti. Separate venture, separate capital, separate risk.  
**Status:** Development / Pre-deployment

---

## Relationship to Manu Forti / Aiden

| Aspect | Manu Forti (Aiden) | Wolf |
|--------|-------------------|------|
| **Purpose** | B2B procurement intelligence | Trading profits for OpenClaw funding |
| **Customer** | External clients (procurement teams) | Jonathon Milne only |
| **Revenue** | Client fees (€249–€3,999) | Trading profits |
| **Risk** | Business risk (no client = no revenue) | Market risk (capital at risk) |
| **Timeline** | Build now, revenue post-SVP | Build now, paper trade 4 weeks, live after |
| **Priority** | Primary focus | Secondary, parallel track |

**Key principle:** Wolf profits fund OpenClaw infrastructure and tools. Manu Forti revenue is separate and funds business growth. No cross-subsidy. No shared capital. If Wolf blows up, Manu Forti continues. If Manu Forti stalls, Wolf continues trading.

**Aiden's role:** Aiden orchestrates both. Wolf reports to Aiden. Aiden ensures Wolf doesn't distract from Manu Forti procurement development. Wolf runs autonomously once deployed — minimal Aiden time required.

---

## Scope (Locked)

| Parameter | Setting |
|-----------|---------|
| **Markets** | Polymarket ONLY |
| **Purpose** | Profit generation |
| **User** | Jonathon Milne exclusively |
| **Autonomy** | Fully autonomous WITH hard guardrails |
| **Revenue use** | Fund OpenClaw infrastructure, tools, expansion |

**Explicitly OUT of scope:**
- Other prediction markets (Kalshi, Betfair, etc.)
- Crypto spot/derivatives trading
- Real-world execution (delivery, APIs, etc.)
- Multi-user or shared access
- External client funds

---

## Trading Strategy Framework

### Core Approach: Multi-Strategy Ensemble

Wolf doesn't rely on a single strategy. It runs multiple strategies in parallel, each with its own edge, risk parameters, and market conditions.

**Strategy 1: Information Arbitrage**
- **Edge:** Speed of information processing
- **Mechanism:** News breaks → Wolf searches/verifies → trades before market adjusts
- **Markets:** Political events, economic releases, geopolitical shocks
- **Position size:** 1–3% of bankroll
- **Hold time:** Minutes to hours

**Strategy 2: Mispricing Detection**
- **Edge:** Probabilistic reasoning superior to crowd
- **Mechanism:** Wolf estimates true probability vs market price → trades when gap > threshold
- **Markets:** Sports, elections, economic indicators
- **Position size:** 2–5% of bankroll
- **Hold time:** Hours to days

**Strategy 3: Market Making (Limited)**
- **Edge:** Providing liquidity in thin markets
- **Mechanism:** Place bids/offers around fair value, capture spread
- **Markets:** Low-volume, high-volatility events
- **Position size:** 0.5–2% of bankroll
- **Hold time:** Minutes to hours

**Strategy 4: Correlation Exploitation**
- **Edge:** Understanding conditional probabilities better than market
- **Mechanism:** If Market A resolves YES, what does that imply for Market B?
- **Markets:** Linked events (e.g. "Will X win primary?" → "Will X win election?")
- **Position size:** 1–3% of bankroll
- **Hold time:** Days to weeks

---

## Guardrails (Hard Limits)

**These are non-negotiable. Wolf cannot override.**

### Financial Limits
| Limit | Value | Action on Breach |
|-------|-------|------------------|
| Max position size | 5% of total bankroll | Reject trade |
| Max daily loss | 10% of bankroll | Trading halt for 24h |
| Max drawdown | 25% of peak bankroll | Trading halt, require human reset |
| Min bankroll | $500 | Stop all trading, alert Jonathon |
| Max exposure per market | 15% of bankroll | Reject additional positions |
| Max correlated exposure | 30% of bankroll | Reject trades that would breach |

### Operational Limits
| Limit | Value | Action on Breach |
|-------|-------|------------------|
| Max trades per day | 50 | Reject additional trades |
| Max open positions | 20 | Close oldest before opening new |
| Trade size increment | $10 minimum | Round to nearest $10 |
| Market liquidity minimum | $10k daily volume | Do not trade |
| Time to resolution minimum | 24 hours | Do not trade markets resolving <24h |

### Human Override
| Trigger | Action |
|---------|--------|
| Text message "WOLF STOP" | Immediate halt, close all positions at market |
| Text message "WOLF PAUSE" | Halt new trades, hold existing positions |
| Text message "WOLF STATUS" | Send P&L, open positions, today's activity |
| Daily report (08:00 CET) | Send overnight summary, bankroll, open positions |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      AGENT WOLF                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  STRATEGY   │  │    RISK     │  │     EXECUTION       │  │
│  │   ENGINE    │  │   ENGINE    │  │       LAYER         │  │
│  │             │  │             │  │                     │  │
│  │ • Info Arb  │  │ • Position  │  │ • Polymarket API    │  │
│  │ • Misprice  │  │   limits    │  │ • Wallet (Base)     │  │
│  │ • Market    │  │ • Daily     │  │ • USDC transfers    │  │
│  │   Making    │  │   loss      │  │ • Order signing     │  │
│  │ • Correl.   │  │ • Drawdown  │  │ • Logging           │  │
│  │   Exploit   │  │ • Exposure  │  │                     │  │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘  │
│         │                │                     │             │
│         └────────────────┴─────────────────────┘             │
│                          │                                   │
│                   ┌──────┴──────┐                           │
│                   │    BRAIN    │                           │
│                   │  (AI Model) │                           │
│                   │             │                           │
│                   │ • Research  │                           │
│                   │ • Estimate  │                           │
│                   │ • Decide    │                           │
│                   │ • Learn     │                           │
│                   └─────────────┘                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  WALLET (Safe)  │
                    │  USDC on Base   │
                    └─────────────────┘
```

---

## Data Flow

### 1. Market Scan (Every 5 minutes)
- Poll Polymarket API for:
  - New markets
  - Price movements >5%
  - Volume spikes
  - Markets approaching resolution

### 2. Opportunity Detection
- Filter markets through strategy criteria
- Run probabilistic analysis on candidates
- Calculate edge (estimated prob - market price)
- Check risk limits

### 3. Research (If edge detected)
- Web search for relevant information
- Check news sources, social sentiment
- Verify market conditions
- Refine probability estimate

### 4. Decision
- If edge > threshold AND within risk limits:
  - Calculate position size (Kelly criterion, capped)
  - Generate trade ticket
  - Submit to execution layer
- Else: pass

### 5. Execution
- Sign transaction with wallet
- Submit order to Polymarket
- Log trade: market, side, size, price, timestamp, strategy
- Update position tracking

### 6. Monitoring (Continuous)
- Track open positions
- Monitor for resolution events
- Update unrealised P&L
- Check against daily loss limits

### 7. Reporting (Daily 08:00 CET)
- Bankroll status
- Open positions
- Realised/unrealised P&L
- Win/loss ratio
- Strategy performance breakdown

---

## Differentiation

**Why Wolf wins where others fail:**

1. **Discipline through hard limits**
   - Most AI traders blow up because they don't have enforced stop-losses
   - Wolf's guardrails are code, not suggestions — cannot be overridden

2. **Multi-strategy ensemble**
   - Single-strategy bots get arbitraged away
   - Wolf runs 4+ strategies, adapts allocation based on market regime

3. **Intelligent position sizing**
   - Uses Kelly criterion with fractional sizing (not full Kelly)
   - Position size scales with edge AND confidence, not just edge

4. **Speed + reasoning**
   - Combines millisecond-level execution with LLM-level research
   - Not just fast — smart and fast

5. **Learning loop**
   - Tracks which strategies work in which market conditions
   - Adjusts allocation monthly based on performance
   - Maintains "memory" of what works

6. **Single-user focus**
   - No multi-tenant complexity
   - Optimised for Jonathon's risk tolerance and goals
   - No dilution from other users' strategies

---

## Performance Targets

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| Monthly return | 5–15% | Monthly |
| Max drawdown | <25% | Continuous |
| Win rate | >55% | Weekly |
| Sharpe ratio | >1.0 | Monthly |
| Profit factor | >1.2 | Monthly |

**Failure conditions (halt and reassess):**
- 3 consecutive months of negative returns
- Drawdown exceeds 25%
- Win rate drops below 45% over 100 trades

---

## Development Phases

### Phase 1: Paper Trading (Weeks 1–4)
- Build core architecture
- Run on Polymarket testnet or simulated environment
- Validate strategies, tune parameters
- No real money at risk

### Phase 2: Micro Live (Weeks 5–8)
- Deploy with $500 bankroll
- Full guardrails active
- Prove profitability at small scale
- Daily monitoring and adjustment

### Phase 3: Scale (Weeks 9–12)
- If Phase 2 profitable: increase bankroll to $2,000
- If continues profitable: increase to $5,000
- Target: $10,000 bankroll by end of Phase 3

### Phase 4: Production (Ongoing)
- Operate with agreed bankroll
- Monthly strategy reviews
- Quarterly architecture reviews
- Continuous improvement

---

## Technical Stack

| Component | Technology |
|-----------|------------|
| Runtime | Python 3.12 |
| AI Model | Claude (via Anthropic API) |
| Blockchain | Base (Coinbase L2) |
| Wallet | Safe (multi-sig, 2-of-3) |
| Stablecoin | USDC |
| API | Polymarket REST API |
| Data | Web search (Brave API), RSS feeds |
| Hosting | Railway / Render (Docker) |
| Monitoring | Telegram bot (alerts, status) |
| Logging | Structured JSON, daily reports |

---

## Security

### Wallet Security
- Multi-sig Safe wallet (2-of-3)
- Keys: 1) Wolf hot wallet, 2) Jonathon hardware wallet, 3) Recovery (offline)
- Daily transfer limits enforced in contract
- Emergency pause function

### Operational Security
- API keys in environment variables, never committed
- IP whitelisting for Polymarket API
- Rate limiting to prevent API abuse
- No external access to Wolf's control interface

### Recovery
- If Wolf server fails: Jonathon can recover funds with hardware wallet
- If Jonathon loses access: Recovery key (offline, in safe)
- If Wolf goes rogue: Emergency pause + hardware wallet recovery

---

## Legal & Compliance

**Jurisdiction:** Norway (Jonathon's residence)

**Key considerations:**
- Polymarket is not available to US users — Jonathon is not US person
- Gambling vs trading regulation — prediction markets legal status varies
- Tax reporting — all P&L tracked for annual tax filing
- No KYC required for Polymarket (crypto-native)

**Action required:**
- [ ] Legal review of Polymarket terms for Norway residents
- [ ] Tax consultation on prediction market profits
- [ ] Insurance consideration (is this insurable?)

---

## Success Metrics

**Primary:** Cumulative profit in USD

**Secondary:**
- Return on investment (ROI) %
- Consistency of returns (month-over-month)
- Strategy attribution (which strategies contribute most)
- Risk-adjusted returns (Sharpe, Sortino)

**Operational:**
- Uptime (target: 99.5%)
- Trade execution speed (target: <5 seconds from decision to execution)
- False positive rate (trades that shouldn't have been made)

---

## Next Steps

1. **Jonathon approval** — Confirm this specification meets requirements
2. **Legal check** — Verify Polymarket access from Norway, tax treatment
3. **Bankroll commitment** — Confirm starting capital ($500 for Phase 1)
4. **Development start** — Build Phase 1 (paper trading)
5. **Testnet validation** — Run 2–4 weeks on simulated markets
6. **Live deployment** — Phase 2 with real money

---

*Version 1.0 — March 13, 2026*  
*Status: Specification complete, awaiting approval to build*
