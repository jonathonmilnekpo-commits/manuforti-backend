"""
Polymarket API Client using py-clob-client
Read-only for Phase 1 (paper trading)
"""

import requests
import time
from typing import List, Dict, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class PolymarketClient:
    """
    Client for Polymarket APIs
    Phase 1: Read-only using py-clob-client and Gamma API
    """

    GAMMA_API_URL = "https://gamma-api.polymarket.com"
    CLOB_HOST = "https://clob.polymarket.com"

    def __init__(self, api_key: Optional[str] = None, chain_id: int = 137):
        self.api_key = api_key
        self.chain_id = chain_id
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

        # Initialize CLOB client if py-clob-client is available
        self.clob_client = None
        try:
            from py_clob_client.client import ClobClient
            self.clob_client = ClobClient(host=self.CLOB_HOST, chain_id=chain_id)
            logger.info("CLOB client initialized")
        except ImportError:
            logger.warning("py-clob-client not available, using REST API only")

        self._cache = {}
        self._cache_ttl = 60  # seconds
        self._last_request_time = 0
        self._min_request_interval = 0.2  # 200ms between requests

    def _rate_limit(self):
        """Enforce rate limiting"""
        elapsed = time.time() - self._last_request_time
        if elapsed < self._min_request_interval:
            time.sleep(self._min_request_interval - elapsed)
        self._last_request_time = time.time()

    def _get(self, url: str, params: Optional[dict] = None, use_cache: bool = True) -> dict:
        """Make GET request with caching and rate limiting"""
        cache_key = f"{url}:{str(params)}"

        # Check cache
        if use_cache and cache_key in self._cache:
            cached_time, cached_data = self._cache[cache_key]
            if time.time() - cached_time < self._cache_ttl:
                return cached_data

        # Rate limit
        self._rate_limit()

        # Make request
        response = self.session.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Cache result
        if use_cache:
            self._cache[cache_key] = (time.time(), data)

        return data

    def get_markets(self, active: bool = True, limit: int = 100, offset: int = 0) -> List[Dict]:
        """
        Fetch markets from Polymarket Gamma API
        """
        url = f"{self.GAMMA_API_URL}/markets"
        params = {
            "closed": "false" if active else "true",
            "limit": min(limit, 100),
            "offset": offset
        }

        try:
            data = self._get(url, params)
            # Gamma API returns list directly
            if isinstance(data, list):
                markets = data
            else:
                markets = data.get("markets", [])
            logger.info(f"Fetched {len(markets)} markets from Polymarket")
            return markets
        except Exception as e:
            logger.error(f"Failed to fetch markets: {e}")
            return []

    def get_active_markets(self, limit: int = 50) -> List[Dict]:
        """
        Fetch currently active markets (not closed, not resolved)
        """
        markets = self.get_markets(limit=limit * 2)

        now = datetime.now()
        active = []

        for market in markets:
            # Skip if explicitly closed
            if market.get('closed') or market.get('archived'):
                continue

            # Check end date is in the future
            end_date = market.get('endDate')
            if end_date:
                try:
                    end = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
                    if end > now:
                        active.append(market)
                except:
                    # If we can't parse date, include it (might be active)
                    active.append(market)
            else:
                # No end date, might be active
                active.append(market)

            if len(active) >= limit:
                break

        logger.info(f"Found {len(active)} active markets")
        return active

    def get_market(self, market_id: str) -> Optional[Dict]:
        """
        Fetch detailed info for a specific market
        """
        try:
            url = f"{self.GAMMA_API_URL}/markets/{market_id}"
            return self._get(url, use_cache=False)
        except Exception as e:
            logger.warning(f"Market {market_id} not found: {e}")
            return None

    def get_price(self, market: Dict, outcome: str = "Yes") -> Optional[float]:
        """
        Get current price for a market outcome
        """
        import json

        outcomes_raw = market.get("outcomes", "[]")
        prices_raw = market.get("outcomePrices", "[]")

        # Parse JSON strings
        try:
            if isinstance(outcomes_raw, str):
                outcomes = json.loads(outcomes_raw)
            else:
                outcomes = outcomes_raw

            if isinstance(prices_raw, str):
                prices = json.loads(prices_raw)
            else:
                prices = prices_raw
        except json.JSONDecodeError:
            return None

        if not outcomes or not prices:
            return None

        try:
            idx = outcomes.index(outcome)
            if idx < len(prices):
                price = prices[idx]
                return float(price) if isinstance(price, (int, float, str)) else None
        except (ValueError, IndexError):
            pass

        return None

    def get_liquid_markets(self, min_volume: float = 10000, limit: int = 50) -> List[Dict]:
        """
        Fetch active markets with sufficient liquidity
        """
        markets = self.get_active_markets(limit=limit * 2)

        liquid = []
        for market in markets:
            volume = market.get("volume", 0)
            if isinstance(volume, str):
                try:
                    volume = float(volume)
                except:
                    volume = 0

            if volume >= min_volume:
                liquid.append(market)
            if len(liquid) >= limit:
                break

        return liquid

    def get_orderbook(self, token_id: str) -> Optional[Dict]:
        """
        Fetch order book using CLOB client
        """
        if not self.clob_client:
            logger.warning("CLOB client not available")
            return None

        try:
            return self.clob_client.get_order_book(token_id)
        except Exception as e:
            logger.error(f"Failed to fetch orderbook: {e}")
            return None

    def clear_cache(self):
        """Clear the request cache"""
        self._cache.clear()
        logger.info("Cache cleared")

# Convenience function
def get_client(api_key: Optional[str] = None) -> PolymarketClient:
    """Get a configured Polymarket client"""
    return PolymarketClient(api_key)

# Export
__all__ = ['PolymarketClient', 'get_client']
