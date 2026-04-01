#!/usr/bin/env python3
"""
Stock price lookup using Alpha Vantage API
For Product 1 supplier financial research
"""

import os
import sys
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

def get_stock_quote(symbol):
    """Get current stock quote for a symbol"""
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        print("Error: ALPHA_VANTAGE_API_KEY not set")
        return None
    
    ts = TimeSeries(key=api_key, output_format='pandas')
    try:
        data, meta = ts.get_quote_endpoint(symbol)
        return data.to_dict('records')[0]
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

def get_company_overview(symbol):
    """Get company overview (market cap, P/E, etc.)"""
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        return None
    
    fd = FundamentalData(key=api_key, output_format='pandas')
    try:
        data, meta = fd.get_company_overview(symbol)
        return data.to_dict('records')[0] if not data.empty else None
    except Exception as e:
        print(f"Error fetching overview for {symbol}: {e}")
        return None

def format_stock_info(symbol, quote, overview=None):
    """Format stock info for display"""
    if not quote:
        return f"No data found for {symbol}"
    
    price = quote.get('05. price', 'N/A')
    change = quote.get('09. change', 'N/A')
    change_pct = quote.get('10. change percent', 'N/A')
    volume = quote.get('06. volume', 'N/A')
    
    result = f"📊 {symbol}\n"
    result += f"Price: ${price}\n"
    result += f"Change: {change} ({change_pct})\n"
    result += f"Volume: {volume}\n"
    
    if overview:
        market_cap = overview.get('MarketCapitalization', 'N/A')
        pe_ratio = overview.get('PERatio', 'N/A')
        sector = overview.get('Sector', 'N/A')
        industry = overview.get('Industry', 'N/A')
        
        result += f"\nMarket Cap: ${market_cap}\n"
        result += f"P/E Ratio: {pe_ratio}\n"
        result += f"Sector: {sector}\n"
        result += f"Industry: {industry}\n"
    
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 stock_lookup.py <SYMBOL>")
        print("Example: python3 stock_lookup.py AAPL")
        sys.exit(1)
    
    symbol = sys.argv[1].upper()
    print(f"Fetching data for {symbol}...\n")
    
    quote = get_stock_quote(symbol)
    overview = get_company_overview(symbol)
    
    print(format_stock_info(symbol, quote, overview))
