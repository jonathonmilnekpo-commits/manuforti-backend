"""
Wolf CLI and Telegram Interface
Control and monitor Wolf via command line and Telegram
"""

import argparse
import json
import sys
from datetime import datetime

from wolf.core.engine import WolfEngine

class WolfCLI:
    """Command line interface for Wolf"""
    
    def __init__(self):
        self.engine = None
    
    def cmd_start(self, bankroll: float = 500.0, interval: int = 300):
        """Start Wolf in continuous mode"""
        print(f"🐺 Starting Wolf with ${bankroll:.2f} bankroll...")
        self.engine = WolfEngine(initial_bankroll=bankroll)
        self.engine.run_continuous(interval_seconds=interval)
    
    def cmd_cycle(self, bankroll: float = 500.0):
        """Run single trading cycle"""
        print("🐺 Running single cycle...")
        self.engine = WolfEngine(initial_bankroll=bankroll)
        result = self.engine.run_cycle()
        print(json.dumps(result, indent=2))
    
    def cmd_status(self):
        """Get current status"""
        if not self.engine:
            print("❌ Wolf not running")
            return
        
        status = self.engine.get_status()
        print("\n🐺 WOLF STATUS")
        print("=" * 40)
        print(f"Running: {status['running']}")
        print(f"Halted: {status['halted']}")
        if status['halt_reason']:
            print(f"Halt reason: {status['halt_reason']}")
        print(f"\nBankroll: ${status['bankroll']:.2f}")
        print(f"Peak: ${status['peak_bankroll']:.2f}")
        print(f"Drawdown: {status['drawdown_pct']:.1%}")
        print(f"\nOpen positions: {status['open_positions']}")
        print(f"Total exposure: ${status['total_exposure']:.2f}")
        print(f"Daily P&L: ${status['daily_pnl']:.2f}")
        print(f"\nTrades today: {status['trades_today']}")
        print(f"Total trades: {status['total_trades']}")
        print(f"Win rate: {status['win_rate']:.1%}")
        
        if status['last_scan']:
            print(f"\nLast scan: {status['last_scan']}")
    
    def cmd_stop(self):
        """Stop Wolf"""
        if self.engine:
            self.engine.stop()
            print("🐺 Wolf stopped")
        else:
            print("❌ Wolf not running")
    
    def cmd_halt(self, reason: str = "Manual halt"):
        """Emergency halt"""
        if self.engine:
            self.engine.guardrails.halt(reason)
            print(f"🛑 Wolf halted: {reason}")
        else:
            print("❌ Wolf not running")
    
    def cmd_reset(self):
        """Reset halt (requires confirmation)"""
        if not self.engine:
            print("❌ Wolf not running")
            return
        
        confirm = input("Type 'WOLF_RESET' to confirm: ")
        if self.engine.guardrails.reset(confirm):
            print("✅ Wolf reset and ready to trade")
        else:
            print("❌ Reset failed - incorrect confirmation")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='🐺 Wolf - Autonomous Polymarket Trading Agent')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start continuous trading')
    start_parser.add_argument('--bankroll', type=float, default=500.0, help='Initial bankroll (default: 500)')
    start_parser.add_argument('--interval', type=int, default=300, help='Cycle interval in seconds (default: 300)')
    
    # Cycle command
    cycle_parser = subparsers.add_parser('cycle', help='Run single trading cycle')
    cycle_parser.add_argument('--bankroll', type=float, default=500.0, help='Initial bankroll (default: 500)')
    
    # Status command
    subparsers.add_parser('status', help='Get current status')
    
    # Stop command
    subparsers.add_parser('stop', help='Stop trading')
    
    # Halt command
    halt_parser = subparsers.add_parser('halt', help='Emergency halt')
    halt_parser.add_argument('--reason', default='Manual halt', help='Halt reason')
    
    # Reset command
    subparsers.add_parser('reset', help='Reset halt (requires confirmation)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    cli = WolfCLI()
    
    if args.command == 'start':
        cli.cmd_start(args.bankroll, args.interval)
    elif args.command == 'cycle':
        cli.cmd_cycle(args.bankroll)
    elif args.command == 'status':
        cli.cmd_status()
    elif args.command == 'stop':
        cli.cmd_stop()
    elif args.command == 'halt':
        cli.cmd_halt(args.reason)
    elif args.command == 'reset':
        cli.cmd_reset()

if __name__ == '__main__':
    main()
