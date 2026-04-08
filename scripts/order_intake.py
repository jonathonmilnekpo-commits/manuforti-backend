#!/usr/bin/env python3
"""
Order Intake System for Manu Forti
Triggers agent pipelines when new orders are received
"""

import json
import os
import re
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

# Configuration
ORDERS_DIR = Path.home() / ".openclaw" / "workspace" / "orders"
INTAKE_LOG = Path.home() / ".openclaw" / "workspace" / "memory" / "order_intake.log"
PIPELINE_TRIGGER = Path.home() / ".openclaw" / "workspace" / "scripts" / "trigger_pipeline.sh"

# Ensure directories exist
ORDERS_DIR.mkdir(parents=True, exist_ok=True)
INTAKE_LOG.parent.mkdir(parents=True, exist_ok=True)

class OrderIntake:
    """Manages order intake and triggers agent pipelines"""
    
    def __init__(self):
        self.orders_dir = ORDERS_DIR
        self.processed_orders = set()
        self._load_processed()
    
    def _load_processed(self):
        """Load list of already processed orders"""
        if INTAKE_LOG.exists():
            with open(INTAKE_LOG, 'r') as f:
                for line in f:
                    if '|' in line:
                        order_id = line.split('|')[0].strip()
                        self.processed_orders.add(order_id)
    
    def _log_intake(self, order_id: str, product: str, status: str, message: str = ""):
        """Log order intake"""
        timestamp = datetime.now().isoformat()
        with open(INTAKE_LOG, 'a') as f:
            f.write(f"{order_id} | {timestamp} | {product} | {status} | {message}\n")
    
    def create_order(self, product: str, customer: Dict, requirements: Dict) -> str:
        """Create a new order and trigger pipeline"""
        # Generate order ID
        order_id = f"MF-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        
        # Create order structure
        order = {
            "orderId": order_id,
            "product": product,
            "status": "received",
            "createdAt": datetime.now().isoformat(),
            "customer": customer,
            "requirements": requirements,
            "pipeline": self._get_pipeline(product),
            "currentStage": "intake",
            "stages": {}
        }
        
        # Save order
        order_dir = self.orders_dir / order_id
        order_dir.mkdir(parents=True, exist_ok=True)
        
        with open(order_dir / "order.json", 'w') as f:
            json.dump(order, f, indent=2)
        
        # Create handoff directory
        (order_dir / "handoffs").mkdir(exist_ok=True)
        
        # Log intake
        self._log_intake(order_id, product, "received", "Order created, triggering pipeline")
        
        # Trigger pipeline
        self._trigger_pipeline(order_id, product)
        
        return order_id
    
    def _get_pipeline(self, product: str) -> list:
        """Get pipeline stages for product"""
        pipelines = {
            "product1": ["Vetter", "Researcher", "Venture", "Validator", "Aiden"],
            "product2": ["Intake", "Analyst", "Strategist", "Validator", "Aiden"],
            "product3": ["Monitor", "Analyzer", "Reporter", "Validator", "Aiden"]
        }
        return pipelines.get(product.lower().replace(" ", ""), ["Venture", "Aiden"])
    
    def _trigger_pipeline(self, order_id: str, product: str):
        """Trigger the agent pipeline for an order"""
        pipeline = self._get_pipeline(product)
        first_agent = pipeline[0]
        
        # Create initial handoff
        handoff = {
            "version": "1.0",
            "handoffId": str(uuid.uuid4()),
            "from": "Intake",
            "to": first_agent,
            "timestamp": datetime.now().isoformat(),
            "orderId": order_id,
            "context": {
                "taskDescription": f"Process {product} order",
                "priority": "normal",
                "pipeline": pipeline
            },
            "deliverables": [
                {
                    "name": "order.json",
                    "type": "data",
                    "location": f"orders/{order_id}/order.json"
                }
            ],
            "status": "in_progress"
        }
        
        # Save handoff
        handoff_path = self.orders_dir / order_id / "handoffs" / f"intake_{first_agent.lower()}.json"
        with open(handoff_path, 'w') as f:
            json.dump(handoff, f, indent=2)
        
        # Log trigger
        self._log_intake(order_id, product, "triggered", f"Spawned {first_agent}")
        
        # Print instructions for spawning agent
        print(f"\n{'='*60}")
        print(f"🚀 ORDER INTAKE COMPLETE")
        print(f"{'='*60}")
        print(f"Order ID: {order_id}")
        print(f"Product: {product}")
        print(f"Pipeline: {' → '.join(pipeline)}")
        print(f"\nNext Action: Spawn {first_agent} agent")
        print(f"Handoff: {handoff_path}")
        print(f"{'='*60}\n")
        
        return handoff_path
    
    def scan_for_orders(self) -> list:
        """Scan orders directory for new/processing orders"""
        orders = []
        
        for order_dir in self.orders_dir.iterdir():
            if order_dir.is_dir():
                order_file = order_dir / "order.json"
                if order_file.exists():
                    with open(order_file, 'r') as f:
                        order = json.load(f)
                        orders.append(order)
        
        return orders
    
    def get_order_status(self, order_id: str) -> Optional[Dict]:
        """Get status of a specific order"""
        order_file = self.orders_dir / order_id / "order.json"
        
        if not order_file.exists():
            return None
        
        with open(order_file, 'r') as f:
            order = json.load(f)
        
        # Check for handoffs
        handoffs_dir = self.orders_dir / order_id / "handoffs"
        if handoffs_dir.exists():
            handoffs = list(handoffs_dir.glob("*.json"))
            order["handoffs_count"] = len(handoffs)
            order["handoffs"] = [h.name for h in handoffs]
        
        return order
    
    def list_active_orders(self) -> list:
        """List all active (non-completed) orders"""
        orders = self.scan_for_orders()
        return [o for o in orders if o.get("status") not in ["completed", "cancelled"]]


def main():
    """CLI entry point"""
    import sys
    
    intake = OrderIntake()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python order_intake.py create <product> <customer_email> [supplier_name]")
        print("  python order_intake.py status <order_id>")
        print("  python order_intake.py list")
        print("")
        print("Examples:")
        print("  python order_intake.py create product1 jon@example.com 'Nel ASA'")
        print("  python order_intake.py create product2 jon@example.com 'Category: Solar Panels'")
        print("  python order_intake.py create product3 jon@example.com 'Target: Statkraft'")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "create" and len(sys.argv) >= 4:
        product = sys.argv[2]
        customer_email = sys.argv[3]
        requirements = sys.argv[4] if len(sys.argv) > 4 else ""
        
        customer = {
            "email": customer_email,
            "name": customer_email.split('@')[0]
        }
        
        reqs = {
            "description": requirements,
            "tier": "Standard"
        }
        
        order_id = intake.create_order(product, customer, reqs)
        print(f"Created order: {order_id}")
    
    elif command == "status" and len(sys.argv) >= 3:
        order_id = sys.argv[2]
        status = intake.get_order_status(order_id)
        if status:
            print(json.dumps(status, indent=2))
        else:
            print(f"Order not found: {order_id}")
    
    elif command == "list":
        orders = intake.list_active_orders()
        if orders:
            print(f"{'Order ID':<25} {'Product':<15} {'Status':<15} {'Created'}")
            print("-" * 80)
            for order in orders:
                created = order['createdAt'][:19].replace('T', ' ')
                print(f"{order['orderId']:<25} {order['product']:<15} {order['status']:<15} {created}")
        else:
            print("No active orders")
    
    else:
        print("Unknown command")
        sys.exit(1)


if __name__ == "__main__":
    main()
