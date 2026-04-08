#!/usr/bin/env python3
"""
KB Visualization Generator
Creates charts and figures for Mission Control dashboard
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np
from datetime import datetime
from pathlib import Path
import json

# Output directory
VIZ_DIR = Path.home() / ".openclaw" / "workspace" / "mission-control" / "assets" / "viz"
VIZ_DIR.mkdir(parents=True, exist_ok=True)

def save_figure(fig, filename):
    """Save figure to viz directory"""
    filepath = VIZ_DIR / filename
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved: {filepath}")
    return filepath

def generate_agent_timeline():
    """Timeline of Manu Forti development"""
    fig, ax = plt.subplots(figsize=(14, 4))
    
    events = [
        (datetime(2026, 2, 18), "Manu Forti\nStarted", '#ff6b6b'),
        (datetime(2026, 3, 15), "Product 1\nPipeline", '#4ecdc4'),
        (datetime(2026, 3, 30), "SVP Decision\nPivot to MF", '#ffe66d'),
        (datetime(2026, 4, 3), "All 15 Agents\nComplete", '#95e1d3'),
        (datetime(2026, 4, 4), "KB\nImplementation", '#f38181'),
    ]
    
    for i, (date, label, color) in enumerate(events):
        ax.scatter(date, 0, s=300, c=color, zorder=3, edgecolors='black', linewidth=2)
        ax.text(date, 0.15 + (i % 2) * 0.15, label, ha='center', fontsize=9, 
                bbox=dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.7))
    
    ax.plot([e[0] for e in events], [0]*len(events), 'k-', linewidth=2, zorder=1)
    ax.set_ylim(-0.3, 0.5)
    ax.set_xlabel('Date (2026)', fontsize=11, fontweight='bold')
    ax.set_title('Manu Forti Development Timeline', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_yticks([])
    
    return save_figure(fig, 'timeline-development.png')

def generate_pipeline_product1():
    """Product 1 Supplier Analysis Pipeline"""
    fig, ax = plt.subplots(figsize=(14, 3))
    
    stages = [
        ("Vetter", "🔒", "#ff9999", "Security"),
        ("Researcher", "🔍", "#66b3ff", "Data"),
        ("Venture", "📊", "#99ff99", "Generation"),
        ("Validator", "✅", "#ffcc99", "QA"),
        ("Aiden", "🤝", "#ff99cc", "Review")
    ]
    
    for i, (stage, emoji, color, role) in enumerate(stages):
        # Box
        rect = FancyBboxPatch((i*2.6, 0.3), 2.2, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # Stage name
        ax.text(i*2.6+1.1, 1.1, stage, ha='center', va='center', 
                fontweight='bold', fontsize=11)
        # Role
        ax.text(i*2.6+1.1, 0.6, role, ha='center', va='center', 
                fontsize=9, style='italic')
        
        # Arrow
        if i < len(stages)-1:
            ax.annotate('', xy=(i*2.6+2.4, 0.9), xytext=(i*2.6+2.2, 0.9),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    ax.set_xlim(-0.3, 13.5)
    ax.set_ylim(0, 2)
    ax.set_title('Product 1: Supplier Analysis Pipeline', fontsize=14, fontweight='bold', pad=10)
    ax.axis('off')
    
    return save_figure(fig, 'pipeline-product1.png')

def generate_pipeline_product2():
    """Product 2 Category Strategy Pipeline"""
    fig, ax = plt.subplots(figsize=(14, 3))
    
    stages = [
        ("Intake", "📥", "#c7ceea", "Receipt"),
        ("Analyst", "📊", "#b5ead7", "Analysis"),
        ("Strategist", "🎯", "#ffdac1", "Strategy"),
        ("Validator", "✅", "#ff9aa2", "QA"),
        ("Aiden", "🤝", "#cdb4db", "Review")
    ]
    
    for i, (stage, emoji, color, role) in enumerate(stages):
        rect = FancyBboxPatch((i*2.6, 0.3), 2.2, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        ax.text(i*2.6+1.1, 1.1, stage, ha='center', va='center', 
                fontweight='bold', fontsize=11)
        ax.text(i*2.6+1.1, 0.6, role, ha='center', va='center', 
                fontsize=9, style='italic')
        
        if i < len(stages)-1:
            ax.annotate('', xy=(i*2.6+2.4, 0.9), xytext=(i*2.6+2.2, 0.9),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    ax.set_xlim(-0.3, 13.5)
    ax.set_ylim(0, 2)
    ax.set_title('Product 2: Category Strategy Pipeline', fontsize=14, fontweight='bold', pad=10)
    ax.axis('off')
    
    return save_figure(fig, 'pipeline-product2.png')

def generate_pipeline_product3():
    """Product 3 Media Monitoring Pipeline"""
    fig, ax = plt.subplots(figsize=(14, 3))
    
    stages = [
        ("Monitor", "📡", "#a8e6cf", "Collection"),
        ("Analyzer", "📈", "#dcedc1", "Sentiment"),
        ("Reporter", "📝", "#ffd3b6", "Reports"),
        ("Validator", "✅", "#ffaaa5", "QA"),
        ("Aiden", "🤝", "#ff8b94", "Review")
    ]
    
    for i, (stage, emoji, color, role) in enumerate(stages):
        rect = FancyBboxPatch((i*2.6, 0.3), 2.2, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        ax.text(i*2.6+1.1, 1.1, stage, ha='center', va='center', 
                fontweight='bold', fontsize=11)
        ax.text(i*2.6+1.1, 0.6, role, ha='center', va='center', 
                fontsize=9, style='italic')
        
        if i < len(stages)-1:
            ax.annotate('', xy=(i*2.6+2.4, 0.9), xytext=(i*2.6+2.2, 0.9),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    ax.set_xlim(-0.3, 13.5)
    ax.set_ylim(0, 2)
    ax.set_title('Product 3: Media Monitoring Pipeline', fontsize=14, fontweight='bold', pad=10)
    ax.axis('off')
    
    return save_figure(fig, 'pipeline-product3.png')

def generate_product_comparison():
    """Product comparison radar chart"""
    categories = ['Complexity', 'Price\nPoint', 'Automation', 'Client\nValue', 'Scalability']
    N = len(categories)
    
    # Scores 1-5
    products = {
        'Product 1': [3, 2, 4, 4, 3],
        'Product 2': [4, 5, 5, 5, 4],
        'Product 3': [2, 1, 4, 3, 5]
    }
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    for i, (product, values) in enumerate(products.items()):
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=product, color=colors[i])
        ax.fill(angles, values, alpha=0.15, color=colors[i])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8)
    ax.set_title('Product Comparison Matrix', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=10)
    ax.grid(True, alpha=0.3)
    
    return save_figure(fig, 'product-comparison-radar.png')

def generate_agent_health_status():
    """Agent health status dashboard"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Agent System Health Dashboard', fontsize=16, fontweight='bold')
    
    # Chart 1: Agent Status Distribution
    ax1 = axes[0, 0]
    statuses = ['Healthy', 'Warning', 'Critical']
    counts = [15, 0, 0]
    colors = ['#22c55e', '#f59e0b', '#ef4444']
    bars = ax1.bar(statuses, counts, color=colors, alpha=0.8, edgecolor='black')
    ax1.set_ylabel('Number of Agents', fontweight='bold')
    ax1.set_title('Agent Health Status', fontweight='bold')
    ax1.set_ylim(0, 20)
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Chart 2: Products by Pipeline Stage
    ax2 = axes[0, 1]
    stages = ['Research', 'Analysis', 'Generation', 'QA', 'Review']
    product1 = [1, 1, 1, 1, 1]
    product2 = [1, 1, 1, 1, 1]
    product3 = [1, 1, 1, 1, 1]
    
    x = np.arange(len(stages))
    width = 0.25
    
    ax2.bar(x - width, product1, width, label='Product 1', color='#ff9999')
    ax2.bar(x, product2, width, label='Product 2', color='#66b3ff')
    ax2.bar(x + width, product3, width, label='Product 3', color='#99ff99')
    
    ax2.set_ylabel('Active', fontweight='bold')
    ax2.set_title('Pipeline Coverage', fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(stages, rotation=45, ha='right')
    ax2.legend()
    ax2.set_ylim(0, 1.5)
    
    # Chart 3: KB Growth
    ax3 = axes[1, 0]
    dates = ['Mar 15', 'Mar 30', 'Apr 3', 'Apr 4']
    docs = [10, 25, 45, 65]
    ax3.plot(dates, docs, 'o-', linewidth=2, markersize=8, color='#3b82f6')
    ax3.fill_between(dates, docs, alpha=0.2, color='#3b82f6')
    ax3.set_ylabel('Raw Documents', fontweight='bold')
    ax3.set_title('KB Document Growth', fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Chart 4: Agent Types
    ax4 = axes[1, 1]
    types = ['Product\nAgents', 'Shared\nAgents', 'KB\nAgents']
    type_counts = [9, 3, 3]
    colors4 = ['#c7ceea', '#b5ead7', '#ffdac1']
    bars = ax4.bar(types, type_counts, color=colors4, alpha=0.8, edgecolor='black')
    ax4.set_ylabel('Count', fontweight='bold')
    ax4.set_title('Agent Distribution', fontweight='bold')
    ax4.set_ylim(0, 12)
    for bar, count in zip(bars, type_counts):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    
    return save_figure(fig, 'agent-health-dashboard.png')

def generate_kb_growth():
    """KB growth over time"""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    dates = ['Feb 18', 'Mar 2', 'Mar 15', 'Mar 30', 'Apr 3', 'Apr 4']
    raw_docs = [2, 8, 15, 35, 50, 65]
    wiki_pages = [0, 0, 5, 12, 22, 28]
    
    ax.plot(dates, raw_docs, 'o-', linewidth=2, markersize=8, 
            label='Raw Documents', color='#3b82f6')
    ax.plot(dates, wiki_pages, 's-', linewidth=2, markersize=8, 
            label='Wiki Pages', color='#22c55e')
    
    ax.fill_between(dates, raw_docs, alpha=0.1, color='#3b82f6')
    ax.fill_between(dates, wiki_pages, alpha=0.1, color='#22c55e')
    
    ax.set_xlabel('Date (2026)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Count', fontsize=11, fontweight='bold')
    ax.set_title('Knowledge Base Growth', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 80)
    
    plt.tight_layout()
    
    return save_figure(fig, 'kb-growth-chart.png')

def generate_all():
    """Generate all visualizations"""
    print("Generating KB visualizations...")
    print(f"Output directory: {VIZ_DIR}")
    print()
    
    generate_agent_timeline()
    generate_pipeline_product1()
    generate_pipeline_product2()
    generate_pipeline_product3()
    generate_product_comparison()
    generate_agent_health_status()
    generate_kb_growth()
    
    print()
    print("✅ All visualizations generated!")
    print(f"Location: {VIZ_DIR}")
    
    # List files
    print("\nFiles created:")
    for f in sorted(VIZ_DIR.glob('*.png')):
        print(f"  - {f.name}")

if __name__ == "__main__":
    generate_all()
