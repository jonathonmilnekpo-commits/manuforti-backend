#!/usr/bin/env python3
"""
Pipeline Orchestrator
Runs the 3-stage cascade: Qwen3 → Kimi → Sonnet
"""

import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime

def run_pipeline(supplier_name: str, source_urls: list, skip_extract: bool = False, skip_score: bool = False):
    """
    Run the full 3-stage pipeline.
    
    Args:
        supplier_name: Name of supplier to analyze
        source_urls: List of URLs to scrape
        skip_extract: If True, assume extraction already done
        skip_score: If True, assume scoring already done
    """
    
    pipeline_dir = Path(__file__).parent
    start_time = datetime.now()
    
    print("=" * 60)
    print(f"🚀 Pipeline Start: {supplier_name}")
    print(f"⏰ {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    costs = {"qwen3": 0.0, "kimi": 0.0, "sonnet": 0.0}
    
    # === STAGE 1: Extraction (Qwen3 8B Local) ===
    extract_output = pipeline_dir / "01_extract" / "output" / f"{supplier_name.lower().replace(' ', '_')}_extracted.json"
    
    if not skip_extract:
        print("\n📦 STAGE 1: Extraction (Qwen3 8B - Local/Free)")
        print("-" * 40)
        
        # Import and run extraction directly
        sys.path.insert(0, str(pipeline_dir / "01_extract"))
        from extract import run_extraction
        
        result_path = run_extraction(supplier_name, source_urls, extract_output)
        if not result_path:
            print("❌ Extraction failed")
            return None
        
        costs["qwen3"] = 0.0  # Local = free
    else:
        print("\n⏭️  STAGE 1: Skipped (using existing extraction)")
    
    # === STAGE 2: Scoring (Kimi K2.5) ===
    score_output = pipeline_dir / "02_score" / "output" / f"{supplier_name.lower().replace(' ', '_')}_scored.json"
    
    if not skip_score:
        print("\n📊 STAGE 2: Scoring (Kimi K2.5 - Cheap)")
        print("-" * 40)
        
        sys.path.insert(0, str(pipeline_dir / "02_score"))
        from score import run_scoring
        
        result_path = run_scoring(extract_output, score_output)
        if not result_path:
            print("❌ Scoring failed")
            return None
        
        costs["kimi"] = 0.004
    else:
        print("\n⏭️  STAGE 2: Skipped (using existing scoring)")
    
    # === STAGE 3: Generation (Sonnet 4.6) ===
    print("\n✨ STAGE 3: Generation (Sonnet 4.6 - Premium)")
    print("-" * 40)
    
    sys.path.insert(0, str(pipeline_dir / "03_generate"))
    from generate import run_generation
    
    output_dir = pipeline_dir / "03_generate" / "output"
    result_path = run_generation(score_output, output_dir)
    
    if not result_path:
        print("❌ Generation failed or data quality too low")
        return None
    
    costs["sonnet"] = 0.045
    
    # === Summary ===
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    total_cost = sum(costs.values())
    
    print("\n" + "=" * 60)
    print("📋 PIPELINE COMPLETE")
    print("=" * 60)
    print(f"\n💰 Cost Breakdown:")
    print(f"   Qwen3 8B (Local):  ${costs['qwen3']:.3f} (FREE)")
    print(f"   Kimi K2.5:         ${costs['kimi']:.3f}")
    print(f"   Sonnet 4.6:        ${costs['sonnet']:.3f}")
    print(f"   ─────────────────────────")
    print(f"   TOTAL:             ${total_cost:.3f}")
    print(f"\n⏱️  Duration: {duration:.1f}s")
    print(f"📁 Outputs in: {pipeline_dir}/03_generate/output/")
    
    # Cost comparison
    print(f"\n💡 vs. Using Sonnet for everything: ~$0.15 (3x more expensive)")
    print(f"   Savings: {(0.15 - total_cost):.3f} per report ({((0.15 - total_cost) / 0.15 * 100):.0f}% cheaper)")
    
    return {
        "supplier": supplier_name,
        "costs": costs,
        "total_cost": total_cost,
        "duration": duration,
        "outputs": {
            "extract": str(extract_output),
            "score": str(score_output),
            "report": str(pipeline_dir / "03_generate" / "output" / f"{supplier_name.lower().replace(' ', '_')}_report.json")
        }
    }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run 3-stage supplier analysis pipeline")
    parser.add_argument("--supplier", "-s", default="Boskalis", help="Supplier name")
    parser.add_argument("--urls", "-u", nargs="+", default=[
        "https://example.com/supplier"
    ], help="Source URLs")
    parser.add_argument("--skip-extract", action="store_true", help="Skip extraction stage")
    parser.add_argument("--skip-score", action="store_true", help="Skip scoring stage")
    
    args = parser.parse_args()
    
    result = run_pipeline(
        supplier_name=args.supplier,
        source_urls=args.urls,
        skip_extract=args.skip_extract,
        skip_score=args.skip_score
    )
    
    if result:
        # Save run log
        log_path = Path(__file__).parent / "pipeline_runs.jsonl"
        with open(log_path, 'a') as f:
            f.write(json.dumps({
                "timestamp": datetime.now().isoformat(),
                **result
            }) + "\n")
