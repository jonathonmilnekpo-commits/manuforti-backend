#!/usr/bin/env python3
"""
MCDM_CALCULATOR.py
Manu Forti Intelligence | March 2026

AHP Consistency Check + TOPSIS 7-Step Calculation + Sensitivity Analysis
"""

import numpy as np
from typing import List, Tuple, Dict

def ahp_consistency_check(pairwise_matrix: np.ndarray) -> Tuple[float, bool, str]:
    """
    Calculate AHP Consistency Ratio (CR)
    
    Args:
        pairwise_matrix: n x n pairwise comparison matrix
        
    Returns:
        (CR value, pass/fail boolean, detailed message)
    """
    n = pairwise_matrix.shape[0]
    
    # Step 1: Calculate column sums
    col_sums = np.sum(pairwise_matrix, axis=0)
    print(f"Step 1: Column Sums = {col_sums}")
    
    # Step 2: Normalize the matrix (divide each entry by its column sum)
    normalized = pairwise_matrix / col_sums
    print(f"Step 2: Normalized Matrix =\n{np.round(normalized, 4)}")
    
    # Step 3: Calculate row averages (priority vector/weights)
    weights = np.mean(normalized, axis=1)
    print(f"Step 3: Priority Vector (Weights) = {np.round(weights, 4)}")
    
    # Step 4: Calculate weighted sum vector
    weighted_sum = pairwise_matrix @ weights
    print(f"Step 4: Weighted Sum Vector = {np.round(weighted_sum, 4)}")
    
    # Step 5: Calculate lambda_max (principal eigenvalue approximation)
    lambda_max = np.mean(weighted_sum / weights)
    print(f"Step 5: Lambda Max = {lambda_max:.4f}")
    
    # Step 6: Calculate Consistency Index (CI)
    ci = (lambda_max - n) / (n - 1)
    print(f"Step 6: Consistency Index (CI) = {ci:.4f}")
    
    # Step 7: Calculate Consistency Ratio (CR)
    # Random Index values for n=1 to 10
    ri_values = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 
                 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    ri = ri_values.get(n, 1.49)
    cr = ci / ri
    
    print(f"Step 7: Random Index (RI) for n={n} = {ri}")
    print(f"Step 7: Consistency Ratio (CR) = {cr:.4f}")
    
    # Check if CR < 0.10
    passed = cr < 0.10
    status = "PASS" if passed else "FAIL"
    message = f"CR = {cr:.4f} (< 0.10 = {status})"
    
    print(f"\n{'='*50}")
    print(f"AHP CONSISTENCY CHECK: {status}")
    print(f"{'='*50}")
    print(f"Consistency Ratio (CR) = {cr:.4f}")
    print(f"Threshold: CR < 0.10")
    print(f"Result: {message}")
    
    return cr, passed, message

def topsis_calculate(options_matrix: np.ndarray, weights: np.ndarray, 
                     option_names: List[str], criteria_names: List[str]) -> Dict:
    """
    Perform full 7-step TOPSIS calculation
    
    Args:
        options_matrix: m x n matrix (m options, n criteria)
        weights: n weights (normalized, sum to 1)
        option_names: list of m option names
        criteria_names: list of n criteria names
        
    Returns:
        Dictionary with full results
    """
    m, n = options_matrix.shape
    
    print(f"\n{'='*60}")
    print("TOPSIS CALCULATION - 7 STEP PROCESS")
    print(f"{'='*60}")
    print(f"Options: {option_names}")
    print(f"Criteria: {criteria_names}")
    print(f"Weights: {np.round(weights, 4)}")
    print(f"\nOriginal Decision Matrix:\n{options_matrix}")
    
    # Step 1: Normalize the decision matrix
    print(f"\n{'-'*60}")
    print("STEP 1: NORMALIZE THE DECISION MATRIX")
    print(f"{'-'*60}")
    print("Formula: r_ij = x_ij / sqrt(sum(x_ij^2))")
    
    col_sums_sq = np.sqrt(np.sum(options_matrix**2, axis=0))
    print(f"Column sqrt(sum of squares): {np.round(col_sums_sq, 4)}")
    
    normalized_matrix = options_matrix / col_sums_sq
    print(f"Normalized Matrix:\n{np.round(normalized_matrix, 4)}")
    
    # Step 2: Calculate weighted normalized matrix
    print(f"\n{'-'*60}")
    print("STEP 2: CALCULATE WEIGHTED NORMALIZED MATRIX")
    print(f"{'-'*60}")
    print("Formula: v_ij = w_j * r_ij")
    
    weighted_matrix = normalized_matrix * weights
    print(f"Weighted Normalized Matrix:\n{np.round(weighted_matrix, 4)}")
    
    # Step 3: Determine positive ideal solution (PIS)
    print(f"\n{'-'*60}")
    print("STEP 3: DETERMINE POSITIVE IDEAL SOLUTION (PIS)")
    print(f"{'-'*60}")
    print("PIS = max for benefit criteria, min for cost criteria")
    print("(Assuming all criteria are benefit-type for this example)")
    
    pis = np.max(weighted_matrix, axis=0)
    print(f"Positive Ideal Solution (A+): {np.round(pis, 4)}")
    
    # Step 4: Determine negative ideal solution (NIS)
    print(f"\n{'-'*60}")
    print("STEP 4: DETERMINE NEGATIVE IDEAL SOLUTION (NIS)")
    print(f"{'-'*60}")
    print("NIS = min for benefit criteria, max for cost criteria")
    
    nis = np.min(weighted_matrix, axis=0)
    print(f"Negative Ideal Solution (A-): {np.round(nis, 4)}")
    
    # Step 5: Calculate Euclidean distance from PIS
    print(f"\n{'-'*60}")
    print("STEP 5: CALCULATE DISTANCE FROM PIS")
    print(f"{'-'*60}")
    print("Formula: D+ = sqrt(sum((v_ij - A+_j)^2))")
    
    dist_pis = np.sqrt(np.sum((weighted_matrix - pis)**2, axis=1))
    for i, name in enumerate(option_names):
        print(f"  D+({name}) = {dist_pis[i]:.4f}")
    
    # Step 6: Calculate Euclidean distance from NIS
    print(f"\n{'-'*60}")
    print("STEP 6: CALCULATE DISTANCE FROM NIS")
    print(f"{'-'*60}")
    print("Formula: D- = sqrt(sum((v_ij - A-_j)^2))")
    
    dist_nis = np.sqrt(np.sum((weighted_matrix - nis)**2, axis=1))
    for i, name in enumerate(option_names):
        print(f"  D-({name}) = {dist_nis[i]:.4f}")
    
    # Step 7: Calculate TOPSIS score
    print(f"\n{'-'*60}")
    print("STEP 7: CALCULATE TOPSIS SCORE")
    print(f"{'-'*60}")
    print("Formula: C = D- / (D+ + D-)")
    
    topsis_scores = dist_nis / (dist_pis + dist_nis)
    print(f"\nTOPSIS Scores:")
    for i, name in enumerate(option_names):
        print(f"  C({name}) = {topsis_scores[i]:.4f}")
    
    # Rank options
    rankings = np.argsort(-topsis_scores) + 1  # 1-based ranking
    
    print(f"\n{'='*60}")
    print("FINAL RANKINGS")
    print(f"{'='*60}")
    
    results = []
    for i in range(m):
        results.append({
            'option': option_names[i],
            'score': topsis_scores[i],
            'rank': rankings[i],
            'dist_pis': dist_pis[i],
            'dist_nis': dist_nis[i]
        })
    
    # Sort by rank
    results.sort(key=lambda x: x['rank'])
    
    for r in results:
        interpretation = ""
        if r['score'] >= 0.80:
            interpretation = "Clearly superior"
        elif r['score'] >= 0.60:
            interpretation = "Strong performer"
        elif r['score'] >= 0.40:
            interpretation = "Moderate"
        else:
            interpretation = "Weak"
        print(f"  Rank {r['rank']}: {r['option']} (Score: {r['score']:.4f}) - {interpretation}")
    
    winner = results[0]['option']
    print(f"\nWINNER: {winner}")
    
    return {
        'normalized_matrix': normalized_matrix,
        'weighted_matrix': weighted_matrix,
        'pis': pis,
        'nis': nis,
        'dist_pis': dist_pis,
        'dist_nis': dist_nis,
        'scores': topsis_scores,
        'rankings': rankings,
        'results': results,
        'winner': winner
    }

def sensitivity_analysis(base_weights: np.ndarray, options_matrix: np.ndarray,
                        option_names: List[str], criteria_names: List[str],
                        delta: float = 0.10) -> Dict:
    """
    Perform sensitivity analysis by varying weights +/- delta
    
    Args:
        base_weights: original weights
        options_matrix: options scoring matrix
        option_names: list of option names
        criteria_names: list of criteria names
        delta: weight variation (+/- 10% default)
        
    Returns:
        Stability report
    """
    print(f"\n{'='*60}")
    print("SENSITIVITY ANALYSIS")
    print(f"{'='*60}")
    print(f"Testing weight variations of +/- {delta*100:.0f}%")
    
    n = len(base_weights)
    base_result = topsis_calculate(options_matrix, base_weights, option_names, criteria_names)
    base_winner = base_result['winner']
    
    print(f"\nBase case winner: {base_winner}")
    print(f"\nTesting weight sensitivity per criterion:\n")
    
    stability_report = {
        'base_winner': base_winner,
        'stable': True,
        'variations': []
    }
    
    for i, crit in enumerate(criteria_names):
        # Increase weight by delta
        increased_weights = base_weights.copy()
        increased_weights[i] = min(base_weights[i] * (1 + delta), 1.0)
        increased_weights = increased_weights / np.sum(increased_weights)  # Renormalize
        
        result_plus = topsis_calculate(options_matrix, increased_weights, option_names, criteria_names)
        
        # Decrease weight by delta
        decreased_weights = base_weights.copy()
        decreased_weights[i] = max(base_weights[i] * (1 - delta), 0.01)
        decreased_weights = decreased_weights / np.sum(decreased_weights)  # Renormalize
        
        result_minus = topsis_calculate(options_matrix, decreased_weights, option_names, criteria_names)
        
        plus_stable = result_plus['winner'] == base_winner
        minus_stable = result_minus['winner'] == base_winner
        
        variation = {
            'criterion': crit,
            'plus_winner': result_plus['winner'],
            'minus_winner': result_minus['winner'],
            'stable': plus_stable and minus_stable
        }
        stability_report['variations'].append(variation)
        
        status = "STABLE" if variation['stable'] else "UNSTABLE"
        print(f"  {crit}: {status}")
        print(f"    +{delta*100:.0f}%: Winner = {result_plus['winner']}")
        print(f"    -{delta*100:.0f}%: Winner = {result_minus['winner']}")
        
        if not variation['stable']:
            stability_report['stable'] = False
    
    print(f"\n{'='*60}")
    print("SENSITIVITY ANALYSIS SUMMARY")
    print(f"{'='*60}")
    
    if stability_report['stable']:
        print("Result: STABLE - Winner remains unchanged across all weight variations")
    else:
        print("Result: UNSTABLE - Winner changes with weight variations")
        print("Recommendation: Review criteria weights carefully or gather more data")
    
    return stability_report

def main():
    """Example run with default weights and sample data"""
    print("="*70)
    print("MCDM CALCULATOR - Manu Forti Intelligence")
    print("AHP Consistency Check + TOPSIS Ranking + Sensitivity Analysis")
    print("="*70)
    
    # Default AHP weights (from methodology)
    # Cost 30%, Resilience 25%, Risk 20%, Strategic 15%, Ease 10%
    criteria_names = ["Cost Reduction", "Supply Resilience", "Risk Reduction", 
                      "Strategic Alignment", "Implementation Ease"]
    
    # Sample pairwise comparison matrix (approximates the 30/25/20/15/10 weights)
    pairwise_matrix = np.array([
        [1.00, 1.20, 1.50, 2.00, 3.00],  # Cost
        [0.83, 1.00, 1.25, 1.67, 2.50],  # Resilience
        [0.67, 0.80, 1.00, 1.33, 2.00],  # Risk
        [0.50, 0.60, 0.75, 1.00, 1.50],  # Strategic
        [0.33, 0.40, 0.50, 0.67, 1.00],  # Ease
    ])
    
    print("\n" + "="*70)
    print("PART 1: AHP CONSISTENCY CHECK")
    print("="*70)
    
    cr, passed, message = ahp_consistency_check(pairwise_matrix)
    
    # Extract weights from normalized matrix
    col_sums = np.sum(pairwise_matrix, axis=0)
    normalized = pairwise_matrix / col_sums
    weights = np.mean(normalized, axis=1)
    
    print("\nFinal AHP Weights:")
    for i, crit in enumerate(criteria_names):
        print(f"  {crit}: {weights[i]:.2%}")
    
    # Sample options scoring matrix (options x criteria, 1-10 scale)
    option_names = ["Status Quo", "Single Source", "Dual Source", "Spot/Tender", "Strategic Alliance"]
    options_matrix = np.array([
        [5, 4, 3, 5, 8],  # Status Quo
        [8, 6, 5, 7, 6],  # Single Source
        [6, 8, 8, 6, 5],  # Dual Source
        [7, 5, 4, 4, 7],  # Spot/Tender
        [5, 7, 6, 9, 4],  # Strategic Alliance
    ])
    
    print("\n" + "="*70)
    print("PART 2: TOPSIS CALCULATION")
    print("="*70)
    
    topsis_result = topsis_calculate(options_matrix, weights, option_names, criteria_names)
    
    print("\n" + "="*70)
    print("PART 3: SENSITIVITY ANALYSIS")
    print("="*70)
    
    sensitivity = sensitivity_analysis(weights, options_matrix, option_names, criteria_names, delta=0.10)
    
    print("\n" + "="*70)
    print("CALCULATION COMPLETE")
    print("="*70)
    print(f"Recommended Option: {topsis_result['winner']}")
    print(f"AHP Consistency: {'PASS' if passed else 'FAIL'} (CR = {cr:.4f})")
    print(f"Sensitivity: {'STABLE' if sensitivity['stable'] else 'UNSTABLE'}")

if __name__ == "__main__":
    main()
