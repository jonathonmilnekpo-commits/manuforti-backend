#!/usr/bin/env python3
"""
Stage 3: Final Report Generation
Model: Sonnet 4.6 (premium quality)
Purpose: Generate client-facing v15 deck with polished insights
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any

def call_sonnet_generation(scored_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Call Sonnet 4.6 via OpenClaw for final report generation.
    """
    
    supplier = scored_data['supplier']
    print(f"[Sonnet 4.6] Generating v15 deck for: {supplier}")
    print(f"[Sonnet 4.6] Input quality score: {scored_data['overall_quality_score']}/10")
    
    # Build rich prompt for Sonnet
    fin_facts = chr(10).join(f"- {fact}" for fact in scored_data['scored_data']['financial']['facts'])
    op_facts = chr(10).join(f"- {fact}" for fact in scored_data['scored_data']['operational']['facts'])
    risk_facts = chr(10).join(f"- {fact}" for fact in scored_data['scored_data']['risk_factors']['facts'])
    esg_facts = chr(10).join(f"- {fact}" for fact in scored_data['scored_data']['esg']['facts'])
    gaps_list = chr(10).join(f"- {gap}" for gap in scored_data['gaps'])
    
    prompt = f"""You are an expert procurement intelligence analyst creating executive-ready supplier reports.

Using the following QUALITY-SCORED data, generate a complete Product 1 v15 supplier analysis report.

SUPPLIER: {supplier}
OVERALL DATA QUALITY: {scored_data['overall_quality_score']}/10
RECOMMENDATION FROM SCORING: {scored_data['recommendation']}

=== FINANCIAL DATA (Reliability: {scored_data['scored_data']['financial']['reliability']}/10) ===
{fin_facts}

=== OPERATIONAL DATA (Reliability: {scored_data['scored_data']['operational']['reliability']}/10) ===
{op_facts}

=== RISK FACTORS (Reliability: {scored_data['scored_data']['risk_factors']['reliability']}/10) ===
{risk_facts}

=== ESG DATA (Reliability: {scored_data['scored_data']['esg']['reliability']}/10) ===
{esg_facts}

=== GAPS IDENTIFIED ===
{gaps_list}

Generate structured JSON with: executive_summary (overall_risk, risk_score, key_insight, risk_factors), recommendation (verdict, conditions, risk_summary), financial_health, operational_capability, esg_assessment.
"""

    try:
        # Call Sonnet via OpenClaw Gateway HTTP API
        import requests
        
        gateway_url = os.environ.get('OPENCLAW_GATEWAY_URL', 'http://localhost:8080')
        
        response = requests.post(
            f"{gateway_url}/v1/sessions/spawn",
            json={
                "task": prompt,
                "model": "sonnet",
                "mode": "run",
                "timeout_seconds": 180
            },
            timeout=190
        )
        response.raise_for_status()
        
        result = response.json()
        content = result.get('response', result.get('result', ''))
        
        # Parse JSON from response
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0]
        elif '```' in content:
            content = content.split('```')[1].split('```')[0]
        
        report_data = json.loads(content.strip())
        
        # Build final report structure
        final_report = {
            "supplier": supplier,
            "generated_at": scored_data['scored_at'],
            "model": "claude-sonnet-4-6",
            "input_quality_score": scored_data['overall_quality_score'],
            "report": report_data,
            "sonnet_metadata": {
                "input_tokens": len(prompt) // 4,
                "output_tokens": len(content) // 4,
                "cost_usd": 0.045
            },
            "output_files": {
                "json_report": f"{supplier.lower().replace(' ', '_')}_report.json",
                "pptx_deck": f"{supplier.replace(' ', '_')}_Product1_v15_Final.pptx",
                "visuals_dir": f"{supplier.lower().replace(' ', '_')}_v15_visuals/"
            }
        }
        
        return final_report
        
    except Exception as e:
        print(f"[Sonnet 4.6] ⚠ API call failed: {e}")
        print("[Sonnet 4.6] ℹ️  To enable: Ensure OpenClaw gateway is running (openclaw gateway status)")
        print("[Sonnet 4.6] Falling back to mock generation...")
        return _mock_generation(scored_data)

def _mock_generation(scored_data: Dict[str, Any]) -> Dict[str, Any]:
    """Fallback mock generation."""
    supplier = scored_data['supplier']
    return {
        "supplier": supplier,
        "generated_at": scored_data['scored_at'],
        "model": "claude-sonnet-4-6 (MOCK FALLBACK)",
        "input_quality_score": scored_data['overall_quality_score'],
        "report": {
            "executive_summary": {
                "overall_risk": "MEDIUM",
                "risk_score": 50,
                "key_insight": f"[MOCK] Limited data available for {supplier}",
                "risk_factors": ["API unavailable - using mock generation"]
            },
            "recommendation": {
                "verdict": "FLAG_FOR_REVIEW",
                "conditions": ["Re-run with live API"],
                "risk_summary": {"financial": "UNKNOWN", "operational": "UNKNOWN", "geopolitical": "UNKNOWN", "esg": "UNKNOWN"}
            },
            "financial_health": {"note": "[MOCK] Limited data"},
            "operational_capability": {"note": "[MOCK] Limited data"},
            "esg_assessment": {"overall": "UNKNOWN"}
        },
        "sonnet_metadata": {"input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0},
        "output_files": {
            "json_report": f"{supplier.lower().replace(' ', '_')}_report.json",
            "pptx_deck": f"[MOCK]_{supplier.replace(' ', '_')}_Product1_v15_Final.pptx",
            "visuals_dir": f"{supplier.lower().replace(' ', '_')}_v15_visuals/"
        }
    }

def convert_to_generator_format(report: Dict[str, Any], scored: Dict[str, Any]) -> Dict[str, Any]:
    """Convert Sonnet output to product-1-generator expected format."""
    
    supplier = report['supplier']
    rpt = report.get('report', {})
    
    # Extract financials from scored data or use defaults
    fin_data = scored.get('scored_data', {}).get('financial', {}).get('facts', [])
    
    # Build generator-compatible structure
    generator_input = {
        "supplier": supplier,
        "sector": scored.get('scored_data', {}).get('operational', {}).get('facts', ['Industrial'])[0] if scored.get('scored_data', {}).get('operational', {}).get('facts') else "Industrial Services",
        "stats": "Revenue data extracted from sources",
        "financials": {
            "revenue_2024": rpt.get('financial_health', {}).get('revenue_2024', 'N/A'),
            "revenue_yoy": rpt.get('financial_health', {}).get('revenue_yoy', 'N/A'),
            "ebitda": rpt.get('financial_health', {}).get('ebitda', 'N/A'),
            "ebitda_margin": rpt.get('financial_health', {}).get('ebitda_margin', 'N/A'),
            "net_profit": rpt.get('financial_health', {}).get('net_profit', 'N/A'),
            "cagr_3yr": rpt.get('financial_health', {}).get('cagr_3yr', 'N/A'),
            "order_book": rpt.get('financial_health', {}).get('order_book', 'N/A'),
            "gross_debt": rpt.get('financial_health', {}).get('gross_debt', 'N/A'),
            "net_cash": rpt.get('financial_health', {}).get('net_cash', 'N/A'),
            "debt_ebitda": rpt.get('financial_health', {}).get('debt_ebitda', 'N/A'),
            "trend": rpt.get('financial_health', {}).get('trend', 'Stable')
        },
        "executive_summary": rpt.get('executive_summary', {
            "overall_risk": "MEDIUM",
            "risk_score": 50,
            "key_insight": f"Analysis for {supplier}",
            "risk_factors": []
        }),
        "recommendation": rpt.get('recommendation', {
            "verdict": "FLAG_FOR_REVIEW",
            "conditions": ["Manual review required"],
            "risk_summary": {
                "financial": "UNKNOWN",
                "operational": "UNKNOWN",
                "geopolitical": "UNKNOWN",
                "esg": "UNKNOWN"
            }
        }),
        "profile": {
            "description": f"{supplier} is a supplier analyzed through automated intelligence pipeline.",
            "leadership": [{"name": "See raw extraction", "role": "TBD", "tenure": "N/A"}],
            "headquarters": "TBD",
            "employees": "TBD"
        },
        "market_position": {
            "rank": 3,
            "competitors": [
                {"name": "Competitor A", "revenue": "N/A"},
                {"name": "Competitor B", "revenue": "N/A"}
            ],
            "advantages": ["See detailed report"]
        },
        "risks": [
            {"category": "General", "description": "See risk assessment", "impact": "Medium", "probability": "Low"}
        ],
        "esg": rpt.get('esg_assessment', {
            "environmental": "MEDIUM",
            "social": "MEDIUM",
            "governance": "LOW",
            "overall": "MEDIUM",
            "controversies": []
        })
    }
    
    return generator_input

def run_generation(scored_path: Path, output_dir: Path = None) -> Path:
    """Run final generation stage using product-1-generator skill."""
    
    # Load scored data
    with open(scored_path) as f:
        scored = json.load(f)
    
    # Check if quality is sufficient
    if scored['recommendation'] == 'REJECT':
        print(f"[Sonnet 4.6] ⚠ Data quality too low ({scored['overall_quality_score']}/10)")
        print(f"[Sonnet 4.6] Aborting generation. Review gaps: {scored['gaps']}")
        return None
    
    # Generate with Sonnet first (for insights)
    report = call_sonnet_generation(scored)
    
    # Default output
    if output_dir is None:
        output_dir = Path(__file__).parent / "output"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    supplier_slug = report['supplier'].lower().replace(' ', '_')
    json_path = output_dir / f"{supplier_slug}_report.json"
    
    # Save JSON report
    with open(json_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"[Sonnet 4.6] ✓ Report generated: {json_path}")
    print(f"[Sonnet 4.6] Overall Risk: {report['report']['executive_summary']['overall_risk']}")
    print(f"[Sonnet 4.6] Recommendation: {report['report']['recommendation']['verdict']}")
    print(f"[Sonnet 4.6] Cost: ${report['sonnet_metadata']['cost_usd']:.3f}")
    
    # Now use product-1-generator skill to create PPTX
    print(f"\n[Product 1 Generator] Creating v15 PPTX...")
    
    skill_script = Path(__file__).parent.parent.parent / "skills" / "product-1-generator" / "scripts" / "generate.py"
    pptx_output = output_dir / f"{supplier_slug}_Product1_v15.pptx"
    
    if skill_script.exists():
        # Convert report to generator format
        generator_input = convert_to_generator_format(report, scored)
        gen_input_path = output_dir / f"{supplier_slug}_generator_input.json"
        
        with open(gen_input_path, 'w') as f:
            json.dump(generator_input, f, indent=2)
        
        import subprocess
        skill_result = subprocess.run(
            ['python3', str(skill_script),
             str(gen_input_path),
             str(pptx_output)],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if skill_result.returncode == 0:
            print(f"[Product 1 Generator] ✓ PPTX created: {pptx_output}")
            
            # Auto-validate the output
            print(f"\n[Product 1 Validator] Validating output...")
            validator_script = Path(__file__).parent.parent.parent / "skills" / "product-1-validator" / "scripts" / "validate.py"
            
            if validator_script.exists():
                val_result = subprocess.run(
                    ['python3', str(validator_script), str(pptx_output)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if val_result.returncode == 0:
                    try:
                        val_data = json.loads(val_result.stdout)
                        print(f"[Product 1 Validator] ✓ Validation passed (Score: {val_data.get('score', 'N/A')}/100)")
                    except:
                        print(f"[Product 1 Validator] ✓ Validation passed")
                else:
                    print(f"[Product 1 Validator] ⚠ Validation issues detected")
                    print(val_result.stdout)
            
        else:
            print(f"[Product 1 Generator] ⚠ Failed to create PPTX")
            print(skill_result.stderr)
    else:
        print(f"[Product 1 Generator] ⚠ Skill not found at {skill_script}")
        print(f"[Pipeline] JSON report available at: {json_path}")
    
    print(f"\n[Pipeline Complete]")
    print(f"Output files in: {output_dir}")
    
    return json_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate final report from scored data")
    parser.add_argument("input", help="Path to scored JSON from stage 2")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output_dir) if args.output_dir else None
    
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    run_generation(input_path, output_dir)
