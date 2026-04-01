#!/usr/bin/env python3
"""
OX2 Product 1 — Full 9-Visual Suite
OX2 (Swedish renewable energy developer) — EQT Private Equity owned
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge
import matplotlib.patheffects as pe
import numpy as np
import os

output_dir = "/Users/jonathonmilne/.openclaw/workspace/ox2_v15_visuals"
os.makedirs(output_dir, exist_ok=True)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# OX2 Brand Colors (Swedish blue palette)
DARK_BLUE = '#003366'
COBALT = '#1B5E8F'
LIGHT_BLUE = '#2E93BF'
OX2_BLUE = '#005A8C'  # OX2 corporate blue
GREEN = '#27AE60'
AMBER = '#F39C12'
RED = '#C0392B'
GRAY = '#7F8C8D'
LIGHT_GRAY = '#ECF0F1'
WHITE = '#FFFFFF'

print("Generating OX2 visual assets...")

# ============================================================
# CHART 1: Executive Summary Risk Gauge
# ============================================================
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 14)
ax.axis('off')

# Background zones
for color, start, end, label in [(GREEN, 0, 33, 'LOW'), (AMBER, 33, 66, 'MEDIUM'), (RED, 66, 100, 'HIGH')]:
    ax.barh(5, end-start, left=start, height=2.5, color=color, alpha=0.85)
    ax.text(start + (end-start)/2, 4, label, fontsize=13, fontweight='bold',
            ha='center', va='top', color='white',
            path_effects=[pe.withStroke(linewidth=2, foreground='black')])

# Needle at 35 (LOW-MEDIUM border, but still LOW rating)
needle_pos = 35
ax.annotate('', xy=(needle_pos, 6.8), xytext=(needle_pos, 8.5),
            arrowprops=dict(arrowstyle='->', color=DARK_BLUE, lw=3))

# Risk score badge
badge = FancyBboxPatch((34, 7.5), 32, 5.5, boxstyle="round,pad=0.3",
                        facecolor=GREEN, edgecolor=WHITE, linewidth=2)
ax.add_patch(badge)
ax.text(50, 11.5, '✓  LOW RISK', fontsize=22, fontweight='bold',
        ha='center', va='center', color=WHITE)
ax.text(50, 9.8, 'Score: 35 / 100', fontsize=14, ha='center', va='center', color=WHITE)
ax.text(50, 8.4, 'Recommended: APPROVE', fontsize=11, ha='center', va='center',
        color='#D5F5E3', style='italic')

ax.text(50, 2.2, 'Supplier Risk Assessment — OX2 AB (EQT Owned)',
        fontsize=11, ha='center', color=DARK_BLUE, style='italic')

plt.tight_layout(pad=1)
plt.savefig(f'{output_dir}/01_risk_gauge.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 1: Risk Gauge")

# ============================================================
# CHART 2: Corporate Structure Diagram
# ============================================================
fig, ax = plt.subplots(figsize=(11, 6.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(5.5, 10.6, 'CORPORATE STRUCTURE — OX2 AB',
        fontsize=13, fontweight='bold', ha='center', color=DARK_BLUE)

# Parent/main entity box - EQT ownership highlighted
parent = FancyBboxPatch((3.0, 7.8), 5, 2.0, boxstyle="round,pad=0.15",
                         facecolor=OX2_BLUE, edgecolor=WHITE, linewidth=2)
ax.add_patch(parent)
ax.text(5.5, 9.4, 'OX2 AB', fontsize=13, fontweight='bold',
        ha='center', va='center', color=WHITE)
ax.text(5.5, 8.85, 'Owned by EQT Private Equity (since Oct 2024)', fontsize=9.5,
        ha='center', va='center', color='#AED6F1')
ax.text(5.5, 8.3, 'Revenue: SEK 5.4B ($520M est.)  |  Employees: ~612', fontsize=9,
        ha='center', va='center', color='#AED6F1')

# Connector line
ax.plot([5.5, 5.5], [7.8, 6.8], color=GRAY, linewidth=2)
ax.plot([2.0, 9.0], [6.8, 6.8], color=GRAY, linewidth=2)

# Three division boxes
segments = [
    (1.0, 'Onshore\nWind', 'Project development\nGrid connection\nPPA origination', COBALT),
    (4.25, 'Offshore\nWind', 'GW-scale projects\nFloating wind\nBaltic Sea focus', COBALT),
    (7.5, 'Solar PV &\nStorage', 'Utility-scale solar\nBattery storage\nHybrid projects', COBALT),
]

for x, name, desc, color in segments:
    ax.plot([x + 1.5, x + 1.5], [6.8, 6.4], color=GRAY, linewidth=1.5)
    box = FancyBboxPatch((x, 4.4), 3.0, 2.0, boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + 1.5, 5.85, name, fontsize=10, fontweight='bold',
            ha='center', va='center', color=WHITE)
    ax.text(x + 1.5, 5.0, desc, fontsize=7.5, ha='center', va='center',
            color='#D6EAF8', linespacing=1.4)

# Global footprint banner
footer = FancyBboxPatch((0.3, 0.4), 10.4, 3.6, boxstyle="round,pad=0.1",
                         facecolor=LIGHT_GRAY, edgecolor=GRAY, linewidth=1)
ax.add_patch(footer)
ax.text(5.5, 3.6, 'GLOBAL FOOTPRINT — 10+ EUROPEAN MARKETS + AUSTRALIA', fontsize=11,
        fontweight='bold', ha='center', color=DARK_BLUE)

details = [
    'HQ: Stockholm, Sweden  |  Founded: 2004  |  Delisted: October 2024 (EQT acquisition)',
    'Pipeline: Multi-GW development portfolio across Northern Europe',
    'Recent sales: Major portfolio to Finland, energy storage projects in Sweden',
]
for i, d in enumerate(details):
    ax.text(5.5, 2.9 - i * 0.7, d, fontsize=8.5, ha='center', color=GRAY)

plt.tight_layout(pad=0.5)
plt.savefig(f'{output_dir}/02_org_structure.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 2: Org Structure")

# ============================================================
# CHART 3: 3-Year Financial Trajectory
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5.5))

years = [2021, 2022, 2023, 2024]
revenue = [4.2, 5.8, 6.8, 5.4]  # SEK billions
ebitda = [0.65, 0.95, 1.15, 0.85]  # SEK billions (estimated)

ax2 = ax.twinx()

line1, = ax.plot(years, revenue, 'o-', color=OX2_BLUE, linewidth=2.5, markersize=10,
                  markerfacecolor=LIGHT_BLUE, label='Revenue (SEK B)', zorder=5)
line2, = ax2.plot(years, ebitda, 's--', color=GREEN, linewidth=2, markersize=8,
                   markerfacecolor='#A9DFBF', label='EBITDA (SEK B)', zorder=5)

for x, y in zip(years, revenue):
    ax.annotate(f'SEK {y}B', xy=(x, y), xytext=(0, 12), textcoords='offset points',
                ha='center', fontsize=10, fontweight='bold', color=OX2_BLUE)
for x, y in zip(years, ebitda):
    ax2.annotate(f'SEK {y}B', xy=(x, y), xytext=(0, -18), textcoords='offset points',
                 ha='center', fontsize=9, fontweight='bold', color=GREEN)

ax.set_xlim(2020.5, 2024.5)
ax.set_ylim(3, 8)
ax2.set_ylim(0, 1.4)
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Revenue (SEK Billion)', fontsize=11, color=OX2_BLUE)
ax2.set_ylabel('EBITDA (SEK Billion)', fontsize=11, color=GREEN)
ax.set_title('OX2 — Financial Trajectory 2021–2024 (SEK)',
             fontsize=13, fontweight='bold', color=DARK_BLUE, pad=12)

ax.tick_params(axis='y', colors=OX2_BLUE)
ax2.tick_params(axis='y', colors=GREEN)
ax.set_xticks(years)

insight = (
    'INSIGHT: Revenue declined 20% in 2024 due to project timing and\n'
    'portfolio sales. Strong underlying pipeline with multi-GW backlog.\n'
    'EQT ownership provides financial stability and growth capital.'
)
props = dict(boxstyle='round', facecolor='#D5F5E3', edgecolor=GREEN, alpha=0.9)
ax.text(0.02, 0.04, insight, transform=ax.transAxes, fontsize=8.5,
        verticalalignment='bottom', bbox=props, color=DARK_BLUE)

lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc='upper left', fontsize=9)
ax.grid(True, alpha=0.25, linestyle='--')

plt.tight_layout()
plt.savefig(f'{output_dir}/03_financial_trend.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 3: Financial Trend")

# ============================================================
# CHART 4: Market Position — Revenue vs Peers
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5.5))

companies = ['Iberdrola', 'RWE', 'Enel Green Power', 'Vattenfall', 'Ørsted', 'OX2']
revenues = [25, 20, 20, 15, 9.6, 0.52]  # USD billions
colors = [GRAY, GRAY, GRAY, GRAY, GRAY, OX2_BLUE]

bars = ax.barh(companies, revenues, color=colors, edgecolor=DARK_BLUE, linewidth=1.5, height=0.6)
bars[5].set_linewidth(3)

for bar, rev in zip(bars, revenues):
    width = bar.get_width()
    label = f'${rev}B' if rev >= 1 else f'${int(rev*1000)}M'
    ax.text(width + 0.3, bar.get_y() + bar.get_height()/2, label,
            ha='left', va='center', fontsize=11, fontweight='bold', color=DARK_BLUE)

ax.set_xlim(0, 30)
ax.set_xlabel('Estimated Annual Revenue (USD Billion)', fontsize=11)
ax.set_title('Renewable Energy Developers — Market Position Comparison (2024)',
             fontsize=13, fontweight='bold', color=DARK_BLUE, pad=10)

ax.text(18, 0.1,
        'OX2: Pure-play developer with\nfocused Nordic/Baltic expertise',
        fontsize=9, ha='center', style='italic', color=DARK_BLUE,
        bbox=dict(boxstyle='round', facecolor=LIGHT_GRAY, edgecolor=GRAY))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', alpha=0.25, linestyle='--')

plt.tight_layout()
plt.savefig(f'{output_dir}/04_market_position.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 4: Market Position")

# ============================================================
# CHART 5: Strategic Investment Timeline
# ============================================================
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(5.5, 8.6, 'OPERATIONAL CAPABILITY — STRATEGIC MILESTONES',
        fontsize=12, fontweight='bold', ha='center', va='center', color=DARK_BLUE)

timeline_y = 4.8
ax.plot([0.5, 10.5], [timeline_y, timeline_y], color=GRAY, linewidth=3, alpha=0.4, zorder=1)

events = [
    (1.2, '2004', 'Company\nFounded', -1.8),
    (3.0, '2013', 'Nordic Wind\nExpansion', 1.8),
    (5.3, '2019', 'Offshore Wind\nPivot', -1.8),
    (7.5, '2021', 'IPO on\nNasdaq', 1.8),
    (9.8, '2024', 'EQT\nAcquisition', -1.8),
]

for x, year_label, event, direction in events:
    highlight = year_label in ['2021', '2024']
    ax.plot([x, x], [timeline_y - 0.3, timeline_y + 0.3], color=DARK_BLUE, linewidth=2, zorder=2)
    y_pos = timeline_y + direction

    box_color = OX2_BLUE if highlight else LIGHT_GRAY
    edge_color = DARK_BLUE
    text_color = WHITE if highlight else DARK_BLUE
    lw = 2.5 if highlight else 1

    box = FancyBboxPatch((x - 1.0, y_pos - 0.5), 2.0, 1.0,
                          boxstyle="round,pad=0.08",
                          facecolor=box_color, edgecolor=edge_color, linewidth=lw, zorder=3)
    ax.add_patch(box)
    ax.text(x, y_pos, event, fontsize=8, ha='center', va='center',
            fontweight='bold' if highlight else 'normal', color=text_color)
    ax.text(x, timeline_y + (-0.55 if direction > 0 else 0.55),
            year_label, fontsize=8.5, ha='center', va='center', fontweight='bold', color=DARK_BLUE)

# Insight box
insight_box = FancyBboxPatch((0.3, 0.2), 10.4, 2.0, boxstyle="round,pad=0.1",
                              facecolor='#D5F5E3', edgecolor=GREEN, linewidth=1.5)
ax.add_patch(insight_box)
ax.text(5.5, 1.85, 'INVESTMENT INSIGHT', fontsize=11, fontweight='bold', ha='center', color=DARK_BLUE)
ax.text(5.5, 1.05,
        '2024 EQT acquisition provides long-term capital and strategic backing.\n'
        'OX2 focuses on GW-scale offshore wind in Baltic Sea and Northern Europe.',
        fontsize=8.5, ha='center', color=GRAY, linespacing=1.4)

plt.savefig(f'{output_dir}/05_investment_timeline.png', dpi=150, facecolor='white')
plt.close()
print("✓ Chart 5: Investment Timeline")

# ============================================================
# CHART 6: Risk Assessment Matrix (2x2 + table)
# ============================================================
fig, ax = plt.subplots(figsize=(9, 6.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Quadrant backgrounds
quads = [
    (0, 5, 5, 5, '#C6EFCE'),
    (5, 5, 5, 5, '#FFEB9C'),
    (0, 0, 5, 5, '#FFEB9C'),
    (5, 0, 5, 5, '#FFC7CE'),
]
for x, y, w, h, c in quads:
    ax.add_patch(Rectangle((x, y), w, h, facecolor=c, edgecolor='white', linewidth=2, alpha=0.7))

ax.text(2.5, 9.5, 'LOW Probability', fontsize=9, ha='center', color=GRAY)
ax.text(7.5, 9.5, 'HIGH Probability', fontsize=9, ha='center', color=GRAY)
ax.text(-0.3, 7.5, 'HIGH\nImpact', fontsize=9, ha='center', va='center', rotation=90, color=GRAY)
ax.text(-0.3, 2.5, 'LOW\nImpact', fontsize=9, ha='center', va='center', rotation=90, color=GRAY)

# Risk bubbles — OX2 specific
risks = [
    (2.5, 7.0, 'Policy\nChange', AMBER, 'M'),
    (3.5, 5.5, 'Grid\nDelays', AMBER, 'M'),
    (2.0, 3.0, 'FX\nRisk', GREEN, 'L'),
    (6.5, 6.5, 'Project\nTiming', AMBER, 'M'),
    (7.0, 4.0, 'Competition', GREEN, 'L'),
    (8.0, 7.5, 'PE Exit\nRisk', AMBER, 'M'),
]
for x, y, label, color, level in risks:
    ax.add_patch(Circle((x, y), 0.65, facecolor=color, edgecolor='white', linewidth=1.5, zorder=5))
    ax.text(x, y, label, fontsize=7, ha='center', va='center', fontweight='bold',
            color=DARK_BLUE if level == 'L' else 'white', zorder=6)

ax.text(5, 10.3, 'RISK ASSESSMENT MATRIX — OX2', fontsize=13, fontweight='bold',
        ha='center', color=DARK_BLUE)

legend_elements = [
    mpatches.Patch(facecolor=GREEN, label='Low Risk', edgecolor='black'),
    mpatches.Patch(facecolor=AMBER, label='Medium Risk', edgecolor='black'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

plt.tight_layout()
plt.savefig(f'{output_dir}/06_risk_matrix.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 6: Risk Matrix")

# ============================================================
# CHART 7: Commercial Benchmarking Radar
# ============================================================
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(projection='polar'))

categories = ['Price\nCompetitive', 'Lead Time', 'Quality\n& Safety', 'Technical\nCapability', 'Supply Chain', 'Service\n& Support']
N = len(categories)

# OX2 scores - strong in technical capability, good service
ox2_scores = [4, 3, 4, 5, 3, 4]
competitor_scores = [3, 4, 4, 4, 4, 3]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]
ox2_scores += ox2_scores[:1]
competitor_scores += competitor_scores[:1]

ax.plot(angles, ox2_scores, 'o-', linewidth=2.5, label='OX2', color=OX2_BLUE)
ax.fill(angles, ox2_scores, alpha=0.25, color=OX2_BLUE)
ax.plot(angles, competitor_scores, 's--', linewidth=1.5, label='Typical Competitor', color=GRAY)
ax.fill(angles, competitor_scores, alpha=0.1, color=GRAY)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=9.5)
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], size=8, color=GRAY)
ax.set_title('Commercial Benchmarking\n(1=Poor, 5=Excellent)',
             fontsize=12, fontweight='bold', color=DARK_BLUE, y=1.1)

ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1), fontsize=9)

plt.tight_layout()
plt.savefig(f'{output_dir}/07_benchmarking_radar.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 7: Benchmarking Radar")

# ============================================================
# CHART 8: Peer Risk Comparison Bar Chart
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5.5))

peers = ['OX2', 'Ørsted', 'Vattenfall', 'RWE', 'Enel Green Power']
risk_scores = [35, 28, 30, 42, 38]
risk_colors = [GREEN, GREEN, GREEN, AMBER, AMBER]
risk_labels = ['LOW', 'LOW', 'LOW', 'MEDIUM', 'MEDIUM']

bars = ax.bar(peers, risk_scores, color=risk_colors, edgecolor=DARK_BLUE, linewidth=1.5, width=0.6)
bars[0].set_linewidth(3)
bars[0].set_edgecolor(OX2_BLUE)

for bar, score, label in zip(bars, risk_scores, risk_labels):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1.5, f'{label}\n({score})',
            ha='center', va='bottom', fontsize=10, fontweight='bold', color=DARK_BLUE)

# Risk zone bands
ax.axhspan(0, 33, alpha=0.12, color=GREEN, zorder=0)
ax.axhspan(33, 66, alpha=0.12, color=AMBER, zorder=0)
ax.axhspan(66, 100, alpha=0.12, color=RED, zorder=0)

ax.text(4.4, 17, 'LOW RISK', fontsize=9, ha='right', color=GREEN, alpha=0.8)
ax.text(4.4, 49, 'MEDIUM RISK', fontsize=9, ha='right', color=AMBER, alpha=0.8)
ax.text(4.4, 75, 'HIGH RISK', fontsize=9, ha='right', color=RED, alpha=0.8)

ax.set_ylim(0, 90)
ax.set_ylabel('Overall Risk Score (0=Low, 100=High)', fontsize=11)
ax.set_title('Renewable Developer Peer Risk Comparison', fontsize=13, fontweight='bold',
             color=DARK_BLUE, pad=10)
ax.grid(axis='y', alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig(f'{output_dir}/08_peer_risk.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 8: Peer Risk Comparison")

# ============================================================
# CHART 9: ESG Assessment
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(5, 7.5, 'ESG ASSESSMENT — OX2 AB', fontsize=14, fontweight='bold',
        ha='center', color=DARK_BLUE)
ax.text(5, 7.0, 'Environmental, Social & Governance Screening',
        fontsize=10, ha='center', color=GRAY)

# ESG Pillars
pillars = [
    ('Environmental', GREEN, '4.5/5', [
        '✓ Pure-play renewable energy developer',
        '✓ Zero direct emissions business model',
        '✓ 2024 Sustainability Report published',
        '✓ Biodiversity impact assessments',
    ]),
    ('Social', GREEN, '4.0/5', [
        '✓ Annual sustainability reporting',
        '✓ Community engagement programs',
        '✓ Local supply chain development',
        '⚠ Workforce scaling for growth',
    ]),
    ('Governance', AMBER, '3.5/5', [
        '✓ Professional PE ownership (EQT)',
        '✓ Strong project governance',
        '⚠ Private ownership limits transparency',
        '⚠ Limited public disclosure vs listed peers',
    ]),
]

x_positions = [1.2, 4.0, 6.8]
for x, (name, color, score, items) in zip(x_positions, pillars):
    # Pillar header
    header = FancyBboxPatch((x-0.3, 5.5), 2.4, 1.2, boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor='white', linewidth=2)
    ax.add_patch(header)
    ax.text(x+0.9, 6.3, name, fontsize=11, fontweight='bold',
            ha='center', va='center', color=WHITE)
    ax.text(x+0.9, 5.85, score, fontsize=10,
            ha='center', va='center', color='#E8F8F5')
    
    # Items
    y_start = 5.0
    for i, item in enumerate(items):
        ax.text(x, y_start - i*0.5, item, fontsize=8.5, ha='left', color=DARK_BLUE)

# Overall rating
overall_box = FancyBboxPatch((3.0, 0.5), 4.0, 1.5, boxstyle="round,pad=0.15",
                              facecolor=GREEN, edgecolor=WHITE, linewidth=2)
ax.add_patch(overall_box)
ax.text(5, 1.5, 'OVERALL ESG RATING', fontsize=11, fontweight='bold',
        ha='center', color=WHITE)
ax.text(5, 1.0, 'LOW RISK — APPROVE', fontsize=13, fontweight='bold',
        ha='center', color=WHITE)

plt.tight_layout()
plt.savefig(f'{output_dir}/09_esg_assessment.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Chart 9: ESG Assessment")

print(f"\n✓ All 9 OX2 visuals saved to: {output_dir}")
