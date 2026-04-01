"""
Wolf Trading Engine
Main orchestrator for paper trading
"""

import time
import logging
from datetime import datetime, timedelta
from typing import List, Optional, Dict
import json

from wolf.core.config import (
    Portfolio, Guardrails, Logger, Trade,
    MAX_TRADES_PER_DAY, MAX_OPEN_POSITIONS
)
from wolf.core.polymarket_client import PolymarketClient
from wolf.strategies.base import StrategyManager

logger = logging.getLogger(__name__)

class WolfEngine:
    """
    Main trading engine for Wolf
    Phase 1: Paper trading (no real money)
    """

    def __init__(self, initial_bankroll: float = 500.0, api_key: Optional[str] = None):
        # Core components
        self.portfolio = Portfolio(initial_bankroll)
        self.guardrails = Guardrails(self.portfolio)
        self.logger = Logger()
        self.client = PolymarketClient(api_key)
        self.strategies = StrategyManager(include_btc_arb=True)

        # State
        self.running = False
        self.last_scan = None
        self.trades_today = 0
        self.last_day = datetime.now().day

        # Correlation tracking
        self.correlation_groups = {}
        self.market_to_group = {}

        logger.info(f"🐺 Wolf Engine initialized with ${initial_bankroll:.2f} bankroll")

    def _detect_correlations(self, markets: List[Dict]) -> None:
        """Detect and group mutually exclusive markets"""
        from collections import defaultdict
        event_groups = defaultdict(list)

        for market in markets:
            market_id = market.get('conditionId') or market.get('id')
            question = market.get('question', '')

            if 'Stanley Cup' in question:
                event_groups['nhl_stanley_cup'].append(market_id)
            elif 'NBA Finals' in question or 'NBA Championship' in question:
                event_groups['nba_finals'].append(market_id)
            elif 'World Cup' in question:
                event_groups['fifa_world_cup'].append(market_id)
            elif 'Super Bowl' in question:
                event_groups['super_bowl'].append(market_id)
            elif 'presidential election' in question.lower():
                event_groups['presidential_election'].append(market_id)

        for group_id, market_ids in event_groups.items():
            if len(market_ids) > 1:
                self.correlation_groups[group_id] = set(market_ids)
                for mid in market_ids:
                    self.market_to_group[mid] = group_id

    def _execute_opportunity(self, opportunity, strategy, market_data: Dict) -> Optional[dict]:
        """Execute a single trade opportunity"""
        size = strategy.calculate_position_size(opportunity, self.portfolio)
        if size < 10:
            return None

        from wolf.core.polymarket_client import PolymarketClient
        client = PolymarketClient()
        price = client.get_price(market_data, "Yes" if 'yes' in opportunity.side else "No")
        if price is None:
            return None

        trade = Trade(
            market_id=opportunity.market_id,
            market_title=opportunity.market_title,
            side=opportunity.side,
            size=size,
            price=price,
            timestamp=datetime.now(),
            strategy=strategy.name,
            expected_value=opportunity.expected_return,
            confidence=opportunity.confidence
        )

        allowed, reason = self.guardrails.check_all(trade)
        self.logger.log_guardrail('pre_trade', allowed, reason or 'passed')

        if not allowed:
            self.logger.log_trade(trade, f"rejected: {reason}")
            return None

        self._paper_execute(trade, opportunity)
        self.logger.log_trade(trade, "executed")

        return {
            'market': opportunity.market_title[:50],
            'side': opportunity.side,
            'size': size,
            'strategy': strategy.name
        }

    def _paper_execute(self, trade: Trade, opportunity):
        """Execute a paper trade"""
        from wolf.core.config import Position
        self.portfolio.bankroll -= trade.size
        position = Position(
            market_id=trade.market_id,
            market_title=trade.market_title,
            side='yes' if 'yes' in trade.side else 'no',
            size=trade.size,
            entry_price=trade.price,
            entry_time=trade.timestamp,
            strategy=trade.strategy
        )
        self.portfolio.positions[trade.market_id] = position
        self.portfolio.trades_today += 1
        self.trades_today += 1
        self.portfolio.total_trades += 1

    def _new_day(self):
        """Reset daily counters"""
        self.portfolio.reset_daily()
        self.trades_today = 0
        self.last_day = datetime.now().day
        logger.info("🌅 New day started")

    def run_cycle(self) -> dict:
        """Execute one full trading cycle"""
        current_day = datetime.now().day
        if current_day != self.last_day:
            self._new_day()

        self.logger.log_portfolio(self.portfolio)

        if self.guardrails.halted:
            return {'status': 'halted', 'reason': self.guardrails.halt_reason, 'bankroll': self.portfolio.bankroll}

        # Fetch markets
        logger.info("Fetching markets...")
        markets = self.client.get_active_markets(limit=200)
        if not markets:
            return {'status': 'no_markets', 'bankroll': self.portfolio.bankroll}

        # Filter for 5-min BTC or short-term markets
        now = datetime.now()
        max_30 = now + timedelta(days=30)

        crypto_5m = []
        short_term = []

        for m in markets:
            q = m.get('question', '')
            if '5 minute' in q.lower() and ('bitcoin' in q.lower() or 'btc' in q.lower()):
                crypto_5m.append(m)
            else:
                end = m.get('endDate')
                if end:
                    try:
                        d = datetime.fromisoformat(end.replace('Z', '+00:00').replace('+00:00', ''))
                        if now <= d <= max_30:
                            short_term.append(m)
                    except:
                        pass

        if crypto_5m:
            target = crypto_5m
            logger.info(f"Found {len(crypto_5m)} 5-min BTC markets")
        elif short_term:
            target = short_term
        else:
            return {'status': 'no_suitable_markets', 'bankroll': self.portfolio.bankroll}

        self._detect_correlations(target)

        opportunities = self.strategies.analyze_all(target, self.portfolio)
        if not opportunities:
            return {'status': 'no_opportunities', 'markets_scanned': len(target), 'bankroll': self.portfolio.bankroll}

        # Execute with correlation check
        executed = []
        executed_groups = set()

        for opp, strategy, mkt_data in opportunities:
            if self.trades_today >= MAX_TRADES_PER_DAY or len(self.portfolio.positions) >= MAX_OPEN_POSITIONS or len(executed) >= 10:
                break

            mid = opp.market_id
            gid = self.market_to_group.get(mid)
            if gid and gid in executed_groups:
                continue

            result = self._execute_opportunity(opp, strategy, mkt_data)
            if result:
                executed.append(result)
                if gid:
                    executed_groups.add(gid)

                # BTC arb: also execute other side
                if strategy.name == "BTC5MinArbitrage":
                    from wolf.strategies.base import Opportunity
                    opp2 = Opportunity(
                        market_id=opp.market_id,
                        market_title=opp.market_title,
                        side='buy_no' if 'yes' in opp.side else 'buy_yes',
                        confidence=opp.confidence,
                        expected_return=opp.expected_return,
                        rationale=opp.rationale + " (second side)",
                        urgency=opp.urgency
                    )
                    result2 = self._execute_opportunity(opp2, strategy, mkt_data)
                    if result2:
                        executed.append(result2)

        return {
            'status': 'success',
            'markets_scanned': len(target),
            'opportunities_found': len(opportunities),
            'trades_executed': len(executed),
            'open_positions': len(self.portfolio.positions),
            'bankroll': self.portfolio.bankroll
        }

    def get_status(self) -> dict:
        """Get current engine status"""
        return {
            'running': self.running,
            'halted': self.guardrails.halted,
            'bankroll': self.portfolio.bankroll,
            'open_positions': len(self.portfolio.positions),
            'trades_today': self.trades_today
        }

__all__ = ['WolfEngine']
