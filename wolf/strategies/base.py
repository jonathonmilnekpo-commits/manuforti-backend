"""
Strategy Base Class and Implementations
Phase 1: Paper trading simulation
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import random
import logging

from wolf.core.config import Trade, Portfolio

logger = logging.getLogger(__name__)

@dataclass
class Opportunity:
    """A potential trade opportunity identified by a strategy"""
    market_id: str
    market_title: str
    side: str  # 'buy_yes', 'buy_no'
    confidence: float  # 0.0 to 1.0
    expected_return: float  # Expected return percentage
    rationale: str
    urgency: str  # 'immediate', 'high', 'medium', 'low'

class BaseStrategy(ABC):
    """Base class for all trading strategies"""
    
    def __init__(self, name: str, min_confidence: float = 0.6):
        self.name = name
        self.min_confidence = min_confidence
        self.trades_made = 0
        self.trades_profitable = 0
    
    @abstractmethod
    def analyze(self, market: Dict, portfolio: Portfolio) -> Optional[Opportunity]:
        """
        Analyze a market and return an opportunity if found
        
        Args:
            market: Market data from Polymarket
            portfolio: Current portfolio state
        
        Returns:
            Opportunity if strategy identifies edge, None otherwise
        """
        pass
    
    def calculate_position_size(self, opportunity: Opportunity, portfolio: Portfolio) -> float:
        """
        Calculate position size using Kelly criterion with fractional sizing
        
        Args:
            opportunity: The trade opportunity
            portfolio: Current portfolio
        
        Returns:
            Position size in USD
        """
        # Kelly fraction: f = (bp - q) / b
        # where b = odds, p = probability of win, q = probability of loss
        
        # Simplified: use confidence as edge proxy
        edge = opportunity.confidence - 0.5  # Assume 0.5 is fair price
        
        if edge <= 0:
            return 0.0
        
        # Kelly fraction (capped)
        kelly = edge / 0.5  # Simplified
        
        # Use half-Kelly for safety
        half_kelly = kelly * 0.5
        
        # Cap at 5% of bankroll (guardrail)
        max_position = portfolio.bankroll * 0.05
        
        position = portfolio.bankroll * half_kelly
        return min(position, max_position, 100.0)  # Also cap at $100 for Phase 1
    
    def record_result(self, profitable: bool):
        """Record trade outcome for strategy performance tracking"""
        self.trades_made += 1
        if profitable:
            self.trades_profitable += 1
    
    @property
    def win_rate(self) -> float:
        if self.trades_made == 0:
            return 0.0
        return self.trades_profitable / self.trades_made


class InformationArbitrageStrategy(BaseStrategy):
    """
    Strategy 1: Information Arbitrage
    
    Edge: Speed of information processing
    Trades on news/events before market fully prices them in
    """
    
    def __init__(self):
        super().__init__("InformationArbitrage", min_confidence=0.65)
        self.recent_news = {}  # Cache of recent news by market
    
    def analyze(self, market: Dict, portfolio: Portfolio) -> Optional[Opportunity]:
        """
        Analyze market for information arbitrage opportunities
        
        In Phase 1 (paper trading), this simulates the detection logic
        In production, this would integrate with news APIs, social sentiment, etc.
        """
        market_id = market.get("conditionId") or market.get("id")
        title = market.get("question", "") or market.get("title", "")
        
        # Skip markets without sufficient data
        if not market_id or not title:
            return None
        
        # Get volume
        volume = market.get("volume", 0)
        if isinstance(volume, str):
            try:
                volume = float(volume)
            except:
                volume = 0
        
        if volume < 50000:  # Need liquid markets
            return None
        
        # Simulate detecting an edge (in production, this would be real analysis)
        # Use market hash for deterministic "randomness"
        market_hash = hash(str(market_id)) % 100
        
        if market_hash < 10:  # 10% of markets show opportunity
            # Simulate confidence based on volume (higher volume = more confidence)
            confidence = 0.6 + (min(volume, 500000) / 500000) * 0.25
            
            # Determine side based on market characteristics
            side = 'buy_yes' if market_hash % 2 == 0 else 'buy_no'
            
            return Opportunity(
                market_id=market_id,
                market_title=title,
                side=side,
                confidence=min(confidence, 0.85),
                expected_return=0.15,  # 15% expected return
                rationale=f"Information edge detected in {title[:50]}... (simulated for paper trading)",
                urgency='high' if confidence > 0.75 else 'medium'
            )
        
        return None


class MispricingDetectionStrategy(BaseStrategy):
    """
    Strategy 2: Mispricing Detection
    
    Edge: Superior probabilistic reasoning
    Identifies when market price diverges from "true" probability
    """
    
    def __init__(self):
        super().__init__("MispricingDetection", min_confidence=0.6)
    
    def analyze(self, market: Dict, portfolio: Portfolio) -> Optional[Opportunity]:
        """
        Analyze market for mispricing
        
        In production: AI estimates true probability vs market price
        """
        market_id = market.get("conditionId") or market.get("id")
        title = market.get("question", "") or market.get("title", "")
        
        if not market_id:
            return None
        
        # Get current market price (Yes outcome)
        from wolf.core.polymarket_client import PolymarketClient
        client = PolymarketClient()
        yes_price = client.get_price(market, "Yes")
        
        if yes_price is None:
            yes_price = 0.5
        
        # Simulate AI probability estimate
        # In production: Claude would analyze market and estimate true probability
        
        # Use deterministic simulation
        market_hash = hash(str(market_id) + "misprice") % 100
        
        if market_hash < 15:  # 15% of markets show mispricing
            # Simulate AI estimate differing from market
            ai_estimate = 0.3 + (market_hash % 50) / 100  # 0.3 to 0.8
            
            # Calculate edge
            market_prob = float(yes_price)
            edge = abs(ai_estimate - market_prob)
            
            if edge > 0.1:  # Significant edge
                side = 'buy_yes' if ai_estimate > market_prob else 'buy_no'
                confidence = 0.55 + edge
                
                return Opportunity(
                    market_id=market_id,
                    market_title=title,
                    side=side,
                    confidence=min(confidence, 0.8),
                    expected_return=edge * 2,  # Rough estimate
                    rationale=f"Mispricing: AI estimates {ai_estimate:.0%} vs market {market_prob:.0%} (simulated)",
                    urgency='medium'
                )
        
        return None


class MarketMakingStrategy(BaseStrategy):
    """
    Strategy 3: Market Making (Limited)
    
    Edge: Providing liquidity in thin markets
    Captures spread between bid and ask
    """
    
    def __init__(self):
        super().__init__("MarketMaking", min_confidence=0.55)
        self.min_spread = 0.02  # 2% minimum spread
    
    def analyze(self, market: Dict, portfolio: Portfolio) -> Optional[Opportunity]:
        """
        Look for markets with wide spreads where we can capture edge
        """
        market_id = market.get("conditionId") or market.get("id")
        title = market.get("question", "") or market.get("title", "")
        
        if not market_id:
            return None
        
        # Get volume
        volume = market.get("volume", 0)
        if isinstance(volume, str):
            try:
                volume = float(volume)
            except:
                volume = 0
        
        # Only trade thin but not dead markets
        if volume < 10000 or volume > 100000:
            return None
        
        # Simulate spread detection
        market_hash = hash(str(market_id) + "mm") % 100
        
        if market_hash < 8:  # 8% of thin markets
            simulated_spread = 0.02 + (market_hash % 10) / 100  # 2-12% spread
            
            if simulated_spread > self.min_spread:
                return Opportunity(
                    market_id=market_id,
                    market_title=title,
                    side='buy_yes',  # Market maker buys at bid
                    confidence=0.6,
                    expected_return=simulated_spread / 2,
                    rationale=f"Wide spread ({simulated_spread:.1%}) in thin market (simulated)",
                    urgency='low'  # Market making is patient
                )
        
        return None


class CorrelationStrategy(BaseStrategy):
    """
    Strategy 4: Correlation Exploitation
    
    Edge: Understanding conditional probabilities
    Trades linked markets where one outcome implies another
    """
    
    def __init__(self):
        super().__init__("Correlation", min_confidence=0.6)
        self.market_pairs = []  # Would be populated with known correlations
    
    def analyze(self, market: Dict, portfolio: Portfolio) -> Optional[Opportunity]:
        """
        Look for correlation opportunities
        
        In production: maintain database of related markets
        """
        market_id = market.get("conditionId") or market.get("id")
        title = market.get("question", "") or market.get("title", "")
        
        if not market_id:
            return None
        
        # Simulate correlation detection
        # In production: check if this market is correlated to any we have positions in
        
        market_hash = hash(str(market_id) + "corr") % 100
        
        if market_hash < 5:  # 5% of markets show correlation edge
            return Opportunity(
                market_id=market_id,
                market_title=title,
                side='buy_yes' if market_hash % 2 == 0 else 'buy_no',
                confidence=0.65,
                expected_return=0.12,
                rationale="Conditional probability edge based on related market (simulated)",
                urgency='medium'
            )
        
        return None


class StrategyManager:
    """
    Manages all strategies and aggregates their signals
    """

    def __init__(self, include_btc_arb: bool = True):
        self.strategies = [
            InformationArbitrageStrategy(),
            MispricingDetectionStrategy(),
            MarketMakingStrategy(),
            CorrelationStrategy()
        ]

        # Add BTC arbitrage if requested
        if include_btc_arb:
            from wolf.strategies.btc_arbitrage import BTCArbitrageStrategy
            self.strategies.append(BTCArbitrageStrategy(max_position=15.0))
    
    def analyze_all(self, markets: List[Dict], portfolio: Portfolio) -> List[Tuple[Opportunity, BaseStrategy, Dict]]:
        """
        Run all strategies on all markets and return opportunities

        Returns:
            List of (opportunity, strategy, market_data) tuples, sorted by confidence
        """
        opportunities = []

        for market in markets:
            for strategy in self.strategies:
                try:
                    opp = strategy.analyze(market, portfolio)
                    if opp and opp.confidence >= strategy.min_confidence:
                        opportunities.append((opp, strategy, market))
                except Exception as e:
                    logger.error(f"Strategy {strategy.name} failed on {market.get('id')}: {e}")

        # Sort by confidence (highest first)
        opportunities.sort(key=lambda x: x[0].confidence, reverse=True)

        return opportunities
    
    def get_performance(self) -> Dict[str, dict]:
        """Get performance summary for all strategies"""
        return {
            s.name: {
                'trades': s.trades_made,
                'wins': s.trades_profitable,
                'win_rate': s.win_rate
            }
            for s in self.strategies
        }

# Export
__all__ = [
    'BaseStrategy', 'Opportunity', 'StrategyManager',
    'InformationArbitrageStrategy', 'MispricingDetectionStrategy',
    'MarketMakingStrategy', 'CorrelationStrategy'
]
