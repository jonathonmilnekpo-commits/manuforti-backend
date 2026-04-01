#!/usr/bin/env python3
"""
Stock/crypto price history using Alpha Vantage API
"""

import os
import sys
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def get_crypto_history(symbol, market="USD", months=4):
    """Get crypto price history"""
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        print("Error: ALPHA_VANTAGE_API_KEY not set")
        return None
    
    cc = CryptoCurrencies(key=api_key, output_format='pandas')
    try:
        # Get daily data
        data, meta = cc.get_digital_currency_daily(symbol=symbol, market=market)
        # Get last N days (approx 4 months = 120 days)
        recent = data.head(120)
        return recent
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

def get_stock_history(symbol, months=4):
    """Get stock price history"""
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        return None
    
    ts = TimeSeries(key=api_key, output_format='pandas')
    try:
        # Get daily data
        data, meta = ts.get_daily(symbol=symbol, outputsize='full')
        # Get last N days
        recent = data.head(120)
        return recent
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

def format_history(data, symbol):
    """Format price history for display"""
    if data is None or data.empty:
        return "No data available"
    
    # Get first and last prices
    first_price = float(data.iloc[-1].get('4a. close (USD)', data.iloc[-1].get('4. close', 0)))
    last_price = float(data.iloc[0].get('4a. close (USD)', data.iloc[0].get('4. close', 0)))
    
    change = last_price - first_price
    change_pct = (change / first_price) * 100 if first_price else 0
    
    # Get high and low over period
    if '2a. high (USD)' in data.columns:
        high = data['2a. high (USD)'].astype(float).max()
        low = data['3a. low (USD)'].astype(float).min()
    else:
        high = data['2. high'].astype(float).max()
        low = data['3. low'].astype(float).min()
    
    result = f"📈 {symbol} - 4 Month History\n"
    result += f"=" * 40 + "\n"
    result += f"Start Price: ${first_price:,.2f}\n"
    result += f"Current Price: ${last_price:,.2f}\n"
    result += f"Change: ${change:,.2f} ({change_pct:+.2f}%)\n"
    result += f"Period High: ${high:,.2f}\n"
    result += f"Period Low: ${low:,.2f}\n"
    
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 price_history.py <SYMBOL> [crypto|stock]")
        print("Example: python3 price_history.py BTC crypto")
        print("Example: python3 price_history.py AAPL stock")
        sys.exit(1)
    
    symbol = sys.argv[1].upper()
    asset_type = sys.argv[2].lower() if len(sys.argv) > 2 else "crypto"
    
    print(f"Fetching 4-month history for {symbol}...\n")
    
    if asset_type == "crypto":
        data = get_crypto_history(symbol)
    else:
        data = get_stock_history(symbol)
    
    print(format_history(data, symbol))
