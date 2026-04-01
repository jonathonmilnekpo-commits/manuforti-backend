"""
Wolf - Autonomous Polymarket Trading Agent
Phase 1: Paper Trading Architecture
"""

import os
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
import json

# Configuration
POLYMARKET_API_BASE = "https://clob.polymarket.com"
DEFAULT_BANKROLL = 500.0  # USD
MIN_BANKROLL = 100.0

# Guardrails (Hard Limits)
MAX_POSITION_PCT = 0.05  # 5% of bankroll
MAX_DAILY_LOSS_PCT = 0.10  # 10% daily loss halt
MAX_DRAWDOWN_PCT = 0.25  # 25% drawdown kill switch
MAX_TRADES_PER_DAY = 50
MAX_OPEN_POSITIONS = 20
MIN_MARKET_LIQUIDITY = 10000  # $10k daily volume
MIN_TIME_TO_RESOLUTION_HOURS = 24

@dataclass
class Trade:
    """Represents a single trade"""
    market_id: str
    market_title: str
    side: str  # 'buy_yes', 'buy_no', 'sell_yes', 'sell_no'
    size: float  # USD
    price: float  # 0.0 to 1.0
    timestamp: datetime
    strategy: str
    expected_value: float
    confidence: float
    
    def to_dict(self) -> dict:
        return {
            'market_id': self.market_id,
            'market_title': self.market_title,
            'side': self.side,
            'size': self.size,
            'price': self.price,
            'timestamp': self.timestamp.isoformat(),
            'strategy': self.strategy,
            'expected_value': self.expected_value,
            'confidence': self.confidence
        }

@dataclass  
class Position:
    """Represents an open position"""
    market_id: str
    market_title: str
    side: str  # 'yes' or 'no'
    size: float  # USD invested
    entry_price: float
    entry_time: datetime
    strategy: str
    current_price: Optional[float] = None
    
    @property
    def unrealized_pnl(self) -> float:
        if self.current_price is None:
            return 0.0
        if self.side == 'yes':
            return self.size * (self.current_price - self.entry_price) / self.entry_price
        else:  # 'no'
            return self.size * ((1 - self.current_price) - (1 - self.entry_price)) / (1 - self.entry_price)

@dataclass
class Portfolio:
    """Tracks bankroll, positions, and performance"""
    bankroll: float
    peak_bankroll: float
    positions: Dict[str, Position]
    trades_today: int
    daily_pnl: float
    total_trades: int
    winning_trades: int
    losing_trades: int
    
    def __init__(self, initial_bankroll: float = DEFAULT_BANKROLL):
        self.bankroll = initial_bankroll
        self.peak_bankroll = initial_bankroll
        self.positions = {}
        self.trades_today = 0
        self.daily_pnl = 0.0
        self.total_trades = 0
        self.winning_trades = 0
        self.losing_trades = 0
    
    @property
    def total_exposure(self) -> float:
        return sum(pos.size for pos in self.positions.values())
    
    @property
    def drawdown_pct(self) -> float:
        if self.peak_bankroll == 0:
            return 0.0
        return (self.peak_bankroll - self.bankroll) / self.peak_bankroll
    
    def update_peak(self):
        if self.bankroll > self.peak_bankroll:
            self.peak_bankroll = self.bankroll
    
    def reset_daily(self):
        self.trades_today = 0
        self.daily_pnl = 0.0

class Guardrails:
    """Enforces hard trading limits. Cannot be overridden."""
    
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
        self.halted = False
        self.halt_reason = None
    
    def check_all(self, proposed_trade: Trade) -> tuple[bool, Optional[str]]:
        """Returns (allowed, reason_if_denied)"""
        
        if self.halted:
            return False, f"Trading halted: {self.halt_reason}"
        
        # Check daily loss limit
        if self.portfolio.daily_pnl < -self.portfolio.bankroll * MAX_DAILY_LOSS_PCT:
            self.halt(f"Daily loss limit hit: {self.portfolio.daily_pnl:.2f}")
            return False, self.halt_reason
        
        # Check drawdown
        if self.portfolio.drawdown_pct > MAX_DRAWDOWN_PCT:
            self.halt(f"Max drawdown hit: {self.portfolio.drawdown_pct:.1%}")
            return False, self.halt_reason
        
        # Check minimum bankroll
        if self.portfolio.bankroll < MIN_BANKROLL:
            self.halt(f"Bankroll below minimum: ${self.portfolio.bankroll:.2f}")
            return False, self.halt_reason
        
        # Check max trades per day
        if self.portfolio.trades_today >= MAX_TRADES_PER_DAY:
            return False, f"Max trades per day ({MAX_TRADES_PER_DAY}) reached"
        
        # Check max open positions
        if len(self.portfolio.positions) >= MAX_OPEN_POSITIONS:
            return False, f"Max open positions ({MAX_OPEN_POSITIONS}) reached"
        
        # Check position size
        if proposed_trade.size > self.portfolio.bankroll * MAX_POSITION_PCT:
            max_size = self.portfolio.bankroll * MAX_POSITION_PCT
            return False, f"Position size ${proposed_trade.size:.2f} exceeds max ${max_size:.2f}"
        
        # Check total exposure
        new_exposure = self.portfolio.total_exposure + proposed_trade.size
        if new_exposure > self.portfolio.bankroll * 0.5:  # 50% max deployed
            return False, f"Total exposure would exceed 50% of bankroll"
        
        return True, None
    
    def halt(self, reason: str):
        """Emergency halt. Requires manual reset."""
        self.halted = True
        self.halt_reason = reason
        # TODO: Send alert to Jonathon
        print(f"🛑 GUARDRAIL HALT: {reason}")
    
    def reset(self, password: str) -> bool:
        """Reset halt. Requires confirmation."""
        # In production, this would require SMS confirmation
        if password == "WOLF_RESET":  # Placeholder
            self.halted = False
            self.halt_reason = None
            return True
        return False

class Logger:
    """Structured logging for all Wolf activity"""
    
    def __init__(self, log_dir: str = "/Users/jonathonmilne/.openclaw/workspace/wolf/logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.session_start = datetime.now()
        self.session_id = self.session_start.strftime("%Y%m%d_%H%M%S")
    
    def log_trade(self, trade: Trade, status: str):
        """Log a trade execution"""
        entry = {
            'type': 'trade',
            'status': status,
            'data': trade.to_dict()
        }
        self._append(entry)
    
    def log_decision(self, market_id: str, decision: str, reasoning: str):
        """Log an AI decision"""
        entry = {
            'type': 'decision',
            'market_id': market_id,
            'decision': decision,
            'reasoning': reasoning,
            'timestamp': datetime.now().isoformat()
        }
        self._append(entry)
    
    def log_guardrail(self, check: str, passed: bool, message: str):
        """Log guardrail check"""
        entry = {
            'type': 'guardrail',
            'check': check,
            'passed': passed,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        self._append(entry)
    
    def log_portfolio(self, portfolio: Portfolio):
        """Log portfolio snapshot"""
        entry = {
            'type': 'portfolio',
            'bankroll': portfolio.bankroll,
            'peak_bankroll': portfolio.peak_bankroll,
            'drawdown_pct': portfolio.drawdown_pct,
            'open_positions': len(portfolio.positions),
            'total_exposure': portfolio.total_exposure,
            'daily_pnl': portfolio.daily_pnl,
            'timestamp': datetime.now().isoformat()
        }
        self._append(entry)
    
    def _append(self, entry: dict):
        """Append to daily log file"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(self.log_dir, f"wolf_{date_str}.jsonl")
        with open(filepath, 'a') as f:
            f.write(json.dumps(entry) + '\n')

# Export
__all__ = [
    'Trade', 'Position', 'Portfolio', 'Guardrails', 'Logger',
    'DEFAULT_BANKROLL', 'MIN_BANKROLL',
    'MAX_POSITION_PCT', 'MAX_DAILY_LOSS_PCT', 'MAX_DRAWDOWN_PCT',
    'MAX_TRADES_PER_DAY', 'MAX_OPEN_POSITIONS'
]
