{
  "name": "Aiden Knowledge Base",
  "version": "1.0.0",
  "last_updated": "2026-04-04",
  "stats": {
    "total_articles": 22,
    "concepts": 7,
    "products": 3,
    "agents": 9,
    "learnings": 3
  },
  "articles": {
    "concepts": [
      {"id": "agent-pipeline", "title": "Agent Pipeline", "category": "Technical"},
      {"id": "circuit-breaker", "title": "Circuit Breaker", "category": "Technical"},
      {"id": "retry-logic", "title": "Retry Logic", "category": "Technical"},
      {"id": "health-monitoring", "title": "Health Monitoring", "category": "Technical"},
      {"id": "product-1", "title": "Product 1", "category": "Manu Forti"},
      {"id": "product-2", "title": "Product 2", "category": "Manu Forti"},
      {"id": "product-3", "title": "Product 3", "category": "Manu Forti"}
    ],
    "agents": [
      {"id": "vetter", "title": "Vetter Agent", "category": "Manu Forti", "products": ["Product 1"]},
      {"id": "researcher", "title": "Researcher Agent", "category": "Manu Forti", "products": ["Product 1", "Product 2"]},
      {"id": "venture", "title": "Venture Agent", "category": "Manu Forti", "products": ["Product 1", "Product 2", "Product 3"]},
      {"id": "validator", "title": "Validator Agent", "category": "Manu Forti", "products": ["Product 1", "Product 2", "Product 3"]},
      {"id": "analyst", "title": "Analyst Agent", "category": "Manu Forti", "products": ["Product 2"]},
      {"id": "strategist", "title": "Strategist Agent", "category": "Manu Forti", "products": ["Product 2"]},
      {"id": "monitor", "title": "Monitor Agent", "category": "Manu Forti", "products": ["Product 3"]},
      {"id": "analyzer", "title": "Analyzer Agent", "category": "Manu Forti", "products": ["Product 3"]},
      {"id": "reporter", "title": "Reporter Agent", "category": "Manu Forti", "products": ["Product 3"]}
    ],
    "products": [
      {"id": "product1", "title": "Product 1: Supplier Analysis", "price": "€249-499", "status": "Active"},
      {"id": "product2", "title": "Product 2: Procurement Academy", "price": "€2,000-12,000", "status": "Active"},
      {"id": "product3", "title": "Product 3: Media Monitoring", "price": "€35-105+/mo", "status": "Active"}
    ],
    "learnings": [
      {"id": "wins", "title": "Wins", "type": "successes"},
      {"id": "patterns", "title": "Patterns", "type": "best_practices"},
      {"id": "mistakes", "title": "Mistakes", "type": "corrections"}
    ]
  },
  "backlinks": {
    "Agent Pipeline": ["Circuit Breaker", "Retry Logic", "Health Monitoring", "Vetter Agent", "Researcher Agent", "Validator Agent"],
    "Product 1": ["Vetter Agent", "Researcher Agent", "Venture Agent", "Validator Agent", "Product 2", "Product 3"],
    "Product 2": ["Analyst Agent", "Strategist Agent", "Product 1", "Product 3"],
    "Product 3": ["Monitor Agent", "Analyzer Agent", "Reporter Agent", "Product 1", "Product 2"]
  },
  "raw_sources": {
    "conversations": 5,
    "manuforti": 32,
    "statkraft": 12,
    "technical": 14,
    "venture": 2,
    "total": 65
  }
}
