#!/usr/bin/env python3
"""
Stage 1: High-Volume Extraction
Model: Qwen3 8B (local, free)
Purpose: Bulk scrape and extract raw data from multiple sources
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Add shared utils
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))

def call_qwen3_extraction(supplier_name: str, source_urls: List[str]) -> Dict[str, Any]:
    """
    Call Qwen3 8B via Ollama for local extraction.
    Then use financial-data-extractor skill for structured metrics.
    """
    
    print(f"[Qwen3 8B] Extracting data for: {supplier_name}")
    print(f"[Qwen3 8B] Processing {len(source_urls)} sources...")
    
    # Build extraction prompt
    urls_text = "\n".join(f"- {url}" for url in source_urls)
    
    prompt = f"""Extract structured intelligence about {supplier_name} from the following sources.

SOURCES TO ANALYZE:
{urls_text}

Extract and return JSON with these fields:
- financial_snippets: list of financial facts (revenue, profit, debt, etc.)
- news_mentions: list of recent news items
- leadership: list of key executives and tenure
- capabilities: list of business capabilities and strengths
- confidence_scores: object with 0-1 scores for each category
- unstructured_notes: list of additional observations

Return ONLY valid JSON."""

    try:
        import subprocess
        import ollama
        
        # Call Ollama
        response = ollama.chat(
            model="qwen3:8b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1}
        )
        
        # Parse JSON from response
        content = response['message']['content']
        # Handle potential markdown code blocks
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0]
        elif '```' in content:
            content = content.split('```')[1].split('```')[0]
        
        extracted = json.loads(content.strip())
        
        # Now use financial-data-extractor skill for structured financials
        print(f"[Financial Extractor] Running skill for structured metrics...")
        skill_script = Path(__file__).parent.parent.parent / "skills" / "financial-data-extractor" / "scripts" / "extract.py"
        
        if skill_script.exists():
            # Create temp file with extracted text for the skill
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write(content)
                temp_text_file = f.name
            
            # Call financial-data-extractor skill
            skill_result = subprocess.run(
                ['python3', str(skill_script), 
                 '--source', temp_text_file,
                 '--format', 'text',
                 '--supplier', supplier_name],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            import os
            os.unlink(temp_text_file)
            
            if skill_result.returncode == 0:
                try:
                    financials = json.loads(skill_result.stdout)
                    print(f"[Financial Extractor] ✓ Extracted {len([v for v in financials.values() if v])} metrics")
                except:
                    financials = {}
            else:
                financials = {}
        else:
            print(f"[Financial Extractor] ⚠ Skill not found at {skill_script}")
            financials = {}
        
        # Wrap in standard format
        extraction = {
            "supplier": supplier_name,
            "extracted_at": datetime.now().isoformat(),
            "model": "qwen3:8b-local",
            "cost": 0.0,
            "sources_processed": len(source_urls),
            "raw_extractions": {
                "financial_snippets": extracted.get("financial_snippets", []),
                "news_mentions": extracted.get("news_mentions", []),
                "leadership": extracted.get("leadership", []),
                "capabilities": extracted.get("capabilities", [])
            },
            "confidence_scores": extracted.get("confidence_scores", {
                "financial": 0.7,
                "news": 0.6,
                "leadership": 0.7,
                "capabilities": 0.6
            }),
            "unstructured_notes": extracted.get("unstructured_notes", []),
            "structured_financials": financials  # Add skill output
        }
        
        return extraction
        
    except ImportError:
        print("[Qwen3 8B] ⚠ Ollama not installed. Install with: brew install ollama && ollama pull qwen3:8b")
        print("[Qwen3 8B] Falling back to mock extraction...")
        return _mock_extraction(supplier_name, source_urls)
        
    except Exception as e:
        print(f"[Qwen3 8B] ⚠ Ollama error: {e}")
        print("[Qwen3 8B] Falling back to mock extraction...")
        return _mock_extraction(supplier_name, source_urls)

def _mock_extraction(supplier_name: str, source_urls: List[str]) -> Dict[str, Any]:
    """Fallback mock extraction when Ollama unavailable."""
    return {
        "supplier": supplier_name,
        "extracted_at": datetime.now().isoformat(),
        "model": "qwen3:8b-local (MOCK FALLBACK)",
        "cost": 0.0,
        "sources_processed": len(source_urls),
        "raw_extractions": {
            "financial_snippets": [f"[MOCK] Financial data for {supplier_name}"],
            "news_mentions": [f"[MOCK] Recent news about {supplier_name}"],
            "leadership": [f"[MOCK] Leadership info for {supplier_name}"],
            "capabilities": [f"[MOCK] Capabilities of {supplier_name}"]
        },
        "confidence_scores": {"financial": 0.5, "news": 0.5, "leadership": 0.5, "capabilities": 0.5},
        "unstructured_notes": ["[MOCK] Ollama not available - using fallback"]
    }

def run_extraction(supplier_name: str, source_urls: List[str], output_path: Path = None) -> Path:
    """Run extraction stage and save output."""
    
    result = call_qwen3_extraction(supplier_name, source_urls)
    
    # Default output path
    if output_path is None:
        output_path = Path(__file__).parent / "output" / f"{supplier_name.lower().replace(' ', '_')}_extracted.json"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"[Qwen3 8B] ✓ Extraction complete: {output_path}")
    print(f"[Qwen3 8B] Cost: $0.00 (local inference)")
    print(f"[Qwen3 8B] Confidence: {result['confidence_scores']}")
    
    return output_path

if __name__ == "__main__":
    # Example usage
    supplier = "Boskalis"
    urls = [
        "https://www.boskalis.com/investors",
        "https://www.boskalis.com/news",
        "https://www.linkedin.com/company/boskalis"
    ]
    
    output = run_extraction(supplier, urls)
    print(f"\nNext: Run 02_score/score.py with {output}")
