#!/usr/bin/env python3
"""
Agent Health Monitor
Industry-standard observability and health tracking for multi-agent systems
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

# Configuration
HEALTH_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "agent_health"
HEALTH_FILE = HEALTH_DIR / "system_health.json"
METRICS_FILE = HEALTH_DIR / "metrics.json"
ALERTS_FILE = HEALTH_DIR / "alerts.json"

# Thresholds
ALERT_THRESHOLDS = {
    "consecutive_failures": 2,
    "error_rate": 0.25,  # 25%
    "latency_ms": 30000,  # 30 seconds
    "token_usage_1h": 100000,  # 100K tokens/hour
}

class AgentHealthMonitor:
    """Monitor and track agent health metrics"""
    
    def __init__(self):
        self.health_dir = HEALTH_DIR
        self.health_dir.mkdir(parents=True, exist_ok=True)
        self.health_data = self._load_health()
        self.metrics_data = self._load_metrics()
        
    def _load_health(self) -> Dict:
        """Load health data from file"""
        if HEALTH_FILE.exists():
            with open(HEALTH_FILE, 'r') as f:
                return json.load(f)
        return {
            "agents": {},
            "last_updated": datetime.now().isoformat(),
            "system_status": "healthy"
        }
    
    def _load_metrics(self) -> Dict:
        """Load metrics data from file"""
        if METRICS_FILE.exists():
            with open(METRICS_FILE, 'r') as f:
                return json.load(f)
        return {
            "hourly": [],
            "daily": [],
            "last_updated": datetime.now().isoformat()
        }
    
    def _save_health(self):
        """Save health data to file"""
        self.health_data["last_updated"] = datetime.now().isoformat()
        with open(HEALTH_FILE, 'w') as f:
            json.dump(self.health_data, f, indent=2)
    
    def _save_metrics(self):
        """Save metrics data to file"""
        self.metrics_data["last_updated"] = datetime.now().isoformat()
        with open(METRICS_FILE, 'w') as f:
            json.dump(self.metrics_data, f, indent=2)
    
    def record_run(self, agent_name: str, status: str, duration_ms: int, 
                   tokens_used: int, error_type: Optional[str] = None):
        """Record a single agent run"""
        timestamp = datetime.now().isoformat()
        
        if agent_name not in self.health_data["agents"]:
            self.health_data["agents"][agent_name] = {
                "runs": [],
                "consecutive_failures": 0,
                "total_runs": 0,
                "successful_runs": 0,
                "failed_runs": 0,
                "avg_duration_ms": 0,
                "avg_tokens": 0,
                "last_run": None,
                "status": "healthy"
            }
        
        agent = self.health_data["agents"][agent_name]
        
        # Update run history (keep last 100)
        agent["runs"].append({
            "timestamp": timestamp,
            "status": status,
            "duration_ms": duration_ms,
            "tokens_used": tokens_used,
            "error_type": error_type
        })
        agent["runs"] = agent["runs"][-100:]  # Keep last 100
        
        # Update counters
        agent["total_runs"] += 1
        agent["last_run"] = timestamp
        
        if status == "success":
            agent["successful_runs"] += 1
            agent["consecutive_failures"] = 0
        else:
            agent["failed_runs"] += 1
            agent["consecutive_failures"] += 1
        
        # Update averages
        runs = agent["runs"]
        agent["avg_duration_ms"] = sum(r["duration_ms"] for r in runs) / len(runs)
        agent["avg_tokens"] = sum(r["tokens_used"] for r in runs) / len(runs)
        
        # Update agent status
        agent["status"] = self._calculate_agent_status(agent)
        
        # Check for alerts
        self._check_alerts(agent_name, agent)
        
        self._save_health()
    
    def _calculate_agent_status(self, agent: Dict) -> str:
        """Calculate agent health status"""
        # Critical: 3+ consecutive failures
        if agent["consecutive_failures"] >= 3:
            return "critical"
        
        # Warning: 2 consecutive failures or high error rate
        error_rate = agent["failed_runs"] / max(agent["total_runs"], 1)
        if agent["consecutive_failures"] >= 2 or error_rate > 0.25:
            return "warning"
        
        return "healthy"
    
    def _check_alerts(self, agent_name: str, agent: Dict):
        """Check for alert conditions"""
        alerts = []
        
        # Check consecutive failures
        if agent["consecutive_failures"] >= ALERT_THRESHOLDS["consecutive_failures"]:
            alerts.append({
                "severity": "high",
                "type": "consecutive_failures",
                "message": f"{agent_name} has {agent['consecutive_failures']} consecutive failures",
                "timestamp": datetime.now().isoformat()
            })
        
        # Check error rate
        error_rate = agent["failed_runs"] / max(agent["total_runs"], 1)
        if error_rate > ALERT_THRESHOLDS["error_rate"]:
            alerts.append({
                "severity": "medium",
                "type": "high_error_rate",
                "message": f"{agent_name} error rate: {error_rate:.1%}",
                "timestamp": datetime.now().isoformat()
            })
        
        # Save alerts
        if alerts:
            self._save_alerts(alerts)
    
    def _save_alerts(self, alerts: List[Dict]):
        """Save alerts to file"""
        existing = []
        if ALERTS_FILE.exists():
            with open(ALERTS_FILE, 'r') as f:
                existing = json.load(f)
        
        existing.extend(alerts)
        # Keep last 100 alerts
        existing = existing[-100:]
        
        with open(ALERTS_FILE, 'w') as f:
            json.dump(existing, f, indent=2)
    
    def get_system_health(self) -> Dict:
        """Get overall system health summary"""
        agents = self.health_data["agents"]
        
        if not agents:
            return {"status": "unknown", "agents": {}}
        
        critical = sum(1 for a in agents.values() if a["status"] == "critical")
        warning = sum(1 for a in agents.values() if a["status"] == "warning")
        healthy = sum(1 for a in agents.values() if a["status"] == "healthy")
        
        if critical > 0:
            system_status = "critical"
        elif warning > 0:
            system_status = "warning"
        else:
            system_status = "healthy"
        
        return {
            "status": system_status,
            "summary": {
                "total_agents": len(agents),
                "healthy": healthy,
                "warning": warning,
                "critical": critical
            },
            "agents": {
                name: {
                    "status": data["status"],
                    "last_run": data["last_run"],
                    "consecutive_failures": data["consecutive_failures"],
                    "total_runs": data["total_runs"],
                    "error_rate": data["failed_runs"] / max(data["total_runs"], 1)
                }
                for name, data in agents.items()
            },
            "last_updated": self.health_data["last_updated"]
        }
    
    def get_agent_report(self, agent_name: str) -> Optional[Dict]:
        """Get detailed report for a specific agent"""
        if agent_name not in self.health_data["agents"]:
            return None
        
        agent = self.health_data["agents"][agent_name]
        
        # Calculate trends
        recent_runs = agent["runs"][-10:]  # Last 10 runs
        recent_error_rate = sum(1 for r in recent_runs if r["status"] != "success") / max(len(recent_runs), 1)
        
        return {
            "agent": agent_name,
            "status": agent["status"],
            "summary": {
                "total_runs": agent["total_runs"],
                "successful_runs": agent["successful_runs"],
                "failed_runs": agent["failed_runs"],
                "error_rate": agent["failed_runs"] / max(agent["total_runs"], 1),
                "recent_error_rate": recent_error_rate,
                "consecutive_failures": agent["consecutive_failures"]
            },
            "performance": {
                "avg_duration_ms": agent["avg_duration_ms"],
                "avg_tokens": agent["avg_tokens"]
            },
            "recent_runs": agent["runs"][-5:]  # Last 5 runs
        }
    
    def generate_dashboard_html(self) -> str:
        """Generate HTML dashboard"""
        health = self.get_system_health()
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Agent Health Dashboard</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 20px; background: #f5f5f5; }}
        .header {{ background: #002147; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .status {{ display: inline-block; padding: 4px 12px; border-radius: 12px; font-weight: bold; }}
        .healthy {{ background: #22c55e; color: white; }}
        .warning {{ background: #f59e0b; color: white; }}
        .critical {{ background: #ef4444; color: white; }}
        .agent-card {{ background: white; padding: 16px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        .metric {{ display: inline-block; margin-right: 20px; }}
        .metric-value {{ font-size: 24px; font-weight: bold; color: #002147; }}
        .metric-label {{ font-size: 12px; color: #666; }}
        .alerts {{ background: #fef3c7; padding: 12px; border-radius: 6px; margin-top: 20px; }}
        .alert-critical {{ color: #ef4444; }}
        .alert-warning {{ color: #f59e0b; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 Agent Health Dashboard</h1>
        <p>System Status: <span class="status {health['status']}">{health['status'].upper()}</span></p>
        <p>Last Updated: {health['last_updated']}</p>
    </div>
    
    <div class="summary">
        <div class="metric">
            <div class="metric-value">{health['summary']['total_agents']}</div>
            <div class="metric-label">Total Agents</div>
        </div>
        <div class="metric">
            <div class="metric-value">{health['summary']['healthy']}</div>
            <div class="metric-label">Healthy</div>
        </div>
        <div class="metric">
            <div class="metric-value">{health['summary']['warning']}</div>
            <div class="metric-label">Warning</div>
        </div>
        <div class="metric">
            <div class="metric-value">{health['summary']['critical']}</div>
            <div class="metric-label">Critical</div>
        </div>
    </div>
"""
        
        # Add agent cards
        for name, data in health['agents'].items():
            html += f"""
    <div class="agent-card">
        <h3>{name} <span class="status {data['status']}">{data['status']}</span></h3>
        <p>Total Runs: {data['total_runs']} | Error Rate: {data['error_rate']:.1%} | 
           Consecutive Failures: {data['consecutive_failures']}</p>
        <p>Last Run: {data['last_run'] or 'Never'}</p>
    </div>
"""
        
        html += """
</body>
</html>
"""
        return html
    
    def export_dashboard(self, output_path: Optional[str] = None):
        """Export dashboard to HTML file"""
        if output_path is None:
            output_path = self.health_dir / "dashboard.html"
        
        html = self.generate_dashboard_html()
        with open(output_path, 'w') as f:
            f.write(html)
        
        return output_path


def main():
    """CLI entry point"""
    monitor = AgentHealthMonitor()
    
    import sys
    if len(sys.argv) < 2:
        # Print system health
        health = monitor.get_system_health()
        print(json.dumps(health, indent=2))
        return
    
    command = sys.argv[1]
    
    if command == "record" and len(sys.argv) >= 6:
        # record <agent> <status> <duration_ms> <tokens>
        monitor.record_run(
            sys.argv[2],
            sys.argv[3],
            int(sys.argv[4]),
            int(sys.argv[5]),
            sys.argv[6] if len(sys.argv) > 6 else None
        )
        print(f"Recorded run for {sys.argv[2]}")
    
    elif command == "report" and len(sys.argv) >= 3:
        # report <agent>
        report = monitor.get_agent_report(sys.argv[2])
        print(json.dumps(report, indent=2))
    
    elif command == "dashboard":
        # dashboard
        path = monitor.export_dashboard()
        print(f"Dashboard exported to: {path}")
    
    else:
        print("Usage:")
        print("  python agent_health.py [record <agent> <status> <duration_ms> <tokens> [error]]")
        print("  python agent_health.py [report <agent>]")
        print("  python agent_health.py [dashboard]")


if __name__ == "__main__":
    main()
