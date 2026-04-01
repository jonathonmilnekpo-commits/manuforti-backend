#!/usr/bin/env python3
"""
Stage 2: Structured Scoring & Filtering
Model: Kimi K2.5 (cheap, 256K context)
Purpose: Score extracted data quality, filter noise, structure for final report
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

# In production, this would call Kimi via OpenClaw or direct API
def call_kimi_scoring(extraction_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Call Kimi K2.5 via OpenClaw for structured scoring and filtering.
    """
    
    print(f"[Kimi K2.5] Scoring extraction for: {extraction_data['supplier']}")
    print(f"[Kimi K2.5] Processing {extraction_data['sources_processed']} sources...")
    
    # Build prompt for Kimi
    notes_formatted = chr(10).join(f"- {note}" for note in extraction_data['unstructured_notes'])
    raw_json = json.dumps(extraction_data['raw_extractions'], indent=2)
    conf_json = json.dumps(extraction_data['confidence_scores'], indent=2)
    
    prompt = f"""You are a data quality scorer for supplier intelligence reports.

Given the following raw extraction data, score each field on reliability (1-10) and 
extract structured facts. Filter out low-confidence or irrelevant information.

SUPPLIER: {extraction_data['supplier']}

RAW EXTRACTION:
{raw_json}

CONFIDENCE SCORES FROM EXTRACTION:
{conf_json}

UNSTRUCTURED NOTES:
{notes_formatted}

Return ONLY a JSON object with scored_data (financial, operational, risk_factors, esg - each with reliability score, facts list, exclude list), overall_quality_score (1-10), recommendation (PROCEED/FLAG_FOR_REVIEW/REJECT), gaps list, and kimi_metadata with token counts and cost.
"""

    try:
        # Call Kimi via OpenClaw Gateway HTTP API
        import requests
        
        # Get gateway URL from environment or use default
        gateway_url = os.environ.get('OPENCLAW_GATEWAY_URL', 'http://localhost:8080')
        
        response = requests.post(
            f"{gateway_url}/v1/sessions/spawn",
            json={
                "task": prompt,
                "model": "kimi",
                "mode": "run",
                "timeout_seconds": 120
            },
            timeout=130
        )
        response.raise_for_status()
        
        result = response.json()
        content = result.get('response', result.get('result', ''))
        
        # Parse JSON from response
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0]
        elif '```' in content:
            content = content.split('```')[1].split('```')[0]
        
        scored = json.loads(content.strip())
        
        # Ensure required fields
        scored.setdefault('supplier', extraction_data['supplier'])
        scored.setdefault('scored_at', extraction_data['extracted_at'])
        scored.setdefault('model', 'kimi-k2.5')
        scored.setdefault('kimi_metadata', {'input_tokens': 2500, 'output_tokens': 800, 'cost_usd': 0.004})
        
        return scored
        
    except Exception as e:
        print(f"[Kimi K2.5] ⚠ API call failed: {e}")
        print("[Kimi K2.5] ℹ️  To enable: Ensure OpenClaw gateway is running (openclaw gateway status)")
        print("[Kimi K2.5] Falling back to mock scoring...")
        return _mock_scoring(extraction_data)

def _mock_scoring(extraction_data: Dict[str, Any]) -> Dict[str, Any]:
    """Fallback mock scoring."""
    return {
        "supplier": extraction_data['supplier'],
        "scored_at": extraction_data['extracted_at'],
        "model": "kimi-k2.5 (MOCK FALLBACK)",
        "scored_data": {
            "financial": {"reliability": 5, "facts": ["[MOCK] Limited financial data"], "exclude": []},
            "operational": {"reliability": 5, "facts": ["[MOCK] Limited operational data"], "exclude": []},
            "risk_factors": {"reliability": 5, "facts": ["[MOCK] Limited risk data"], "exclude": []},
            "esg": {"reliability": 5, "facts": ["[MOCK] Limited ESG data"], "exclude": []}
        },
        "overall_quality_score": 5.0,
        "recommendation": "FLAG_FOR_REVIEW",
        "gaps": ["API unavailable - using mock data"],
        "kimi_metadata": {"input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0}
    }

def run_scoring(extraction_path: Path, output_path: Path = None) -> Path:
    """Run scoring stage on extracted data."""
    
    # Load extraction
    with open(extraction_path) as f:
        extraction = json.load(f)
    
    # Score with Kimi
    scored = call_kimi_scoring(extraction)
    
    # Default output path
    if output_path is None:
        supplier = extraction['supplier'].lower().replace(' ', '_')
        output_path = Path(__file__).parent / "output" / f"{supplier}_scored.json"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(scored, f, indent=2)
    
    print(f"[Kimi K2.5] ✓ Scoring complete: {output_path}")
    print(f"[Kimi K2.5] Quality score: {scored['overall_quality_score']}/10")
    print(f"[Kimi K2.5] Recommendation: {scored['recommendation']}")
    print(f"[Kimi K2.5] Cost: ${scored['kimi_metadata']['cost_usd']:.4f}")
    
    return output_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Score extracted supplier data")
    parser.add_argument("input", help="Path to extraction JSON from stage 1")
    parser.add_argument("--output", "-o", help="Output path for scored JSON")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None
    
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    result = run_scoring(input_path, output_path)
    print(f"\nNext: Run 03_generate/generate.py with {result}")
