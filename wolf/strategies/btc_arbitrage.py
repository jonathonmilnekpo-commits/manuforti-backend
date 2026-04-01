"""
5-Minute BTC Arbitrage Strategy
Buy both YES and NO when combined price < $0.985
"""

from typing import Dict, Optional
from wolf.strategies.base import BaseStrategy, Opportunity
from wolf.core.config import Portfolio

class BTCArbitrageStrategy(BaseStrategy):
    """
    Strategy: 5-Minute BTC Market Arbitrage
    
    When YES price + NO price < $0.985:
    - Buy YES at market price
    - Buy NO at market price  
    - Guaranteed $1.00 payout (one side wins)
    - Profit = $1.00 - (YES_price + NO_price)
    """
    
    def __init__(self, max_position: float = 15.0, arb_threshold: float = 0.985):
        super().__init__("BTC5MinArbitrage", min_confidence=0.99)
        self.max_position = max_position
        self.arb_threshold = arb_threshold
    
    def analyze(self, market: Dict, portfolio: Portfolio) -> Optional[Opportunity]:
        """
        Check for arbitrage opportunity in 5-min BTC market
        """
        question = market.get('question', '')
        
        # Only trade 5-minute BTC markets
        if not ('5 minute' in question.lower() and 
                ('bitcoin' in question.lower() or 'btc' in question.lower())):
            return None
        
        market_id = market.get('conditionId') or market.get('id')
        
        # Get YES and NO prices
        from wolf.core.polymarket_client import PolymarketClient
        client = PolymarketClient()
        
        yes_price = client.get_price(market, "Yes")
        no_price = client.get_price(market, "No")
        
        if yes_price is None or no_price is None:
            return None
        
        combined = yes_price + no_price
        
        # Check for arbitrage opportunity
        if combined < self.arb_threshold:
            # Calculate profit
            profit_per_dollar = 1.0 - combined
            profit_pct = profit_per_dollar / combined * 100
            
            return Opportunity(
                market_id=market_id,
                market_title=question,
                side='buy_yes',  # Will execute both sides
                confidence=0.99,  # Near-certain profit
                expected_return=profit_pct,
                rationale=f"Arbitrage: YES {yes_price:.3f} + NO {no_price:.3f} = {combined:.3f} (< {self.arb_threshold}). Profit: {profit_pct:.2f}%",
                urgency='immediate'
            )
        
        return None
    
    def calculate_position_size(self, opportunity: Opportunity, portfolio: Portfolio) -> float:
        """
        Fixed position size for arbitrage: max $15 per side
        """
        return min(self.max_position, portfolio.bankroll * 0.05)

# Export
__all__ = ['BTCArbitrageStrategy']
