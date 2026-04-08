#!/usr/bin/env python3
"""
Circuit Breaker for Agent System
Prevents cascading failures when services are degraded
"""

import json
import time
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Optional, Callable, Any

# State file
CIRCUIT_STATE_FILE = Path.home() / ".openclaw" / "workspace" / "memory" / "agent_health" / "circuit_breakers.json"

class CircuitState(Enum):
    CLOSED = "closed"       # Normal operation
    OPEN = "open"          # Failing fast
    HALF_OPEN = "half_open"  # Testing recovery

class CircuitBreaker:
    """Circuit breaker for protecting agent calls"""
    
    def __init__(
        self,
        name: str,
        failure_threshold: int = 3,
        recovery_timeout: int = 300,  # 5 minutes
        half_open_max_calls: int = 1,
        expected_exception: type = Exception
    ):
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls
        self.expected_exception = expected_exception
        
        self.failures = 0
        self.last_failure_time: Optional[float] = None
        self.state = CircuitState.CLOSED
        self.half_open_calls = 0
        
        self._load_state()
    
    def _load_state(self):
        """Load circuit breaker state from disk"""
        if CIRCUIT_STATE_FILE.exists():
            try:
                with open(CIRCUIT_STATE_FILE, 'r') as f:
                    data = json.load(f)
                    if self.name in data:
                        state = data[self.name]
                        self.failures = state.get('failures', 0)
                        self.last_failure_time = state.get('last_failure_time')
                        self.state = CircuitState(state.get('state', 'closed'))
                        self.half_open_calls = state.get('half_open_calls', 0)
            except Exception:
                pass  # Start fresh if file is corrupted
    
    def _save_state(self):
        """Save circuit breaker state to disk"""
        CIRCUIT_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        data = {}
        if CIRCUIT_STATE_FILE.exists():
            try:
                with open(CIRCUIT_STATE_FILE, 'r') as f:
                    data = json.load(f)
            except Exception:
                pass
        
        data[self.name] = {
            'failures': self.failures,
            'last_failure_time': self.last_failure_time,
            'state': self.state.value,
            'half_open_calls': self.half_open_calls,
            'updated_at': datetime.now().isoformat()
        }
        
        with open(CIRCUIT_STATE_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    def can_execute(self) -> bool:
        """Check if execution is allowed"""
        if self.state == CircuitState.CLOSED:
            return True
        
        if self.state == CircuitState.OPEN:
            # Check if recovery timeout has passed
            if self.last_failure_time:
                elapsed = time.time() - self.last_failure_time
                if elapsed >= self.recovery_timeout:
                    self.state = CircuitState.HALF_OPEN
                    self.half_open_calls = 0
                    self._save_state()
                    return True
            return False
        
        if self.state == CircuitState.HALF_OPEN:
            return self.half_open_calls < self.half_open_max_calls
        
        return True
    
    def record_success(self):
        """Record a successful execution"""
        if self.state == CircuitState.HALF_OPEN:
            self.half_open_calls += 1
            if self.half_open_calls >= self.half_open_max_calls:
                # Success in half-open state, close the circuit
                self._reset()
        else:
            # In closed state, just reset failures on success
            if self.failures > 0:
                self.failures = 0
                self._save_state()
    
    def record_failure(self):
        """Record a failed execution"""
        self.failures += 1
        self.last_failure_time = time.time()
        
        if self.state == CircuitState.HALF_OPEN:
            # Failed in half-open state, go back to open
            self.state = CircuitState.OPEN
        elif self.failures >= self.failure_threshold:
            # Too many failures, open the circuit
            self.state = CircuitState.OPEN
        
        self._save_state()
    
    def _reset(self):
        """Reset circuit breaker to closed state"""
        self.failures = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
        self.half_open_calls = 0
        self._save_state()
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with circuit breaker protection"""
        if not self.can_execute():
            raise CircuitBreakerOpenException(
                f"Circuit breaker '{self.name}' is OPEN. "
                f"Failing fast to prevent cascade."
            )
        
        try:
            result = func(*args, **kwargs)
            self.record_success()
            return result
        except self.expected_exception as e:
            self.record_failure()
            raise
    
    @property
    def status(self) -> dict:
        """Get circuit breaker status"""
        return {
            "name": self.name,
            "state": self.state.value,
            "failures": self.failures,
            "threshold": self.failure_threshold,
            "last_failure": datetime.fromtimestamp(self.last_failure_time).isoformat() 
                if self.last_failure_time else None,
            "can_execute": self.can_execute()
        }


class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit breaker is open"""
    pass


# Pre-configured circuit breakers for common services
CIRCUIT_BREAKERS = {
    "kimi_api": CircuitBreaker(
        name="kimi_api",
        failure_threshold=3,
        recovery_timeout=300,  # 5 minutes
        expected_exception=Exception
    ),
    "claude_api": CircuitBreaker(
        name="claude_api",
        failure_threshold=3,
        recovery_timeout=300,
        expected_exception=Exception
    ),
    "web_search": CircuitBreaker(
        name="web_search",
        failure_threshold=5,
        recovery_timeout=180,  # 3 minutes
        expected_exception=Exception
    ),
    "file_operations": CircuitBreaker(
        name="file_operations",
        failure_threshold=10,
        recovery_timeout=60,  # 1 minute
        expected_exception=Exception
    )
}


def get_circuit_breaker(name: str) -> Optional[CircuitBreaker]:
    """Get a circuit breaker by name"""
    return CIRCUIT_BREAKERS.get(name)


def get_all_status() -> dict:
    """Get status of all circuit breakers"""
    return {
        name: cb.status 
        for name, cb in CIRCUIT_BREAKERS.items()
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        # Print all circuit breaker status
        print(json.dumps(get_all_status(), indent=2))
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "status":
        print(json.dumps(get_all_status(), indent=2))
    
    elif command == "reset" and len(sys.argv) >= 3:
        name = sys.argv[2]
        if name in CIRCUIT_BREAKERS:
            CIRCUIT_BREAKERS[name]._reset()
            print(f"Reset circuit breaker: {name}")
        else:
            print(f"Unknown circuit breaker: {name}")
    
    else:
        print("Usage:")
        print("  python circuit_breaker.py [status]")
        print("  python circuit_breaker.py [reset <name>]")
