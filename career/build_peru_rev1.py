"""
Peru BOS Market Analysis — Rev 1 (Infographic / Chart Edition)
Visual-first design: donut charts, bar charts, supplier scorecards,
supply-chain origin visuals. Less tables, more insight.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Arc, Wedge
import matplotlib.patheffects as pe
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os, io

OUT = '/tmp/peru_rev1'
os.makedirs(OUT, exist_ok=True)

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY    = '#0D1B2A'
NAVY_L  = '#162A44'
TEAL    = '#00B4D8'
AMBER   = '#F5A623'
GREEN   = '#2ECC71'
RED     = '#E74C3C'
WHITE   = '#FFFFFF'
GREY_L  = '#B0BEC5'
GREY_M  = '#546E7A'
PURPLE  = '#9B59B6'

def navy_fig(w=19.2, h=10.8, dpi=100):
    fig = plt.figure(figsize=(w, h), facecolor=NAVY, dpi=dpi)
    return fig

def save_slide(fig, n, name):
    path = f'{OUT}/slide_{n:02d}_{name}.jpg'
    fig.savefig(path, bbox_inches='tight', pad_inches=0,
                facecolor=NAVY, dpi=100)
    plt.close(fig)
    print(f'  Saved: {path}')
    return path

def add_header(fig, title, subtitle='', page=1, total=10):
    ax = fig.add_axes([0, 0.88, 1, 0.12], facecolor='#162A44')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0), 0.015, 1, color=TEAL, transform=ax.transAxes))
    ax.text(0.025, 0.62, title,    fontsize=22, color=WHITE,  fontweight='bold', va='center')
    ax.text(0.025, 0.22, subtitle, fontsize=11, color=GREY_L, fontstyle='italic', va='center')
    ax.text(0.99, 0.5,  f'STATKRAFT · CONFIDENTIAL  |  {page}/{total}',
            fontsize=9, color=GREY_M, ha='right', va='center')
    return ax

def add_footer(fig, label='Peru BOS/BOP Market Analysis — Rev 1 · Statkraft Procurement · February 2026'):
    ax = fig.add_axes([0, 0, 1, 0.035], facecolor='#162A44')
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.text(0.015, 0.5, label, fontsize=8.5, color=GREY_M, va='center')
    return ax

def donut(ax, sizes, labels, colors, title='', center_text=''):
    wedges, _ = ax.pie(sizes, colors=colors, startangle=90,
                       wedgeprops=dict(width=0.55, edgecolor=NAVY, linewidth=2))
    ax.set_facecolor(NAVY)
    if center_text:
        ax.text(0, 0, center_text, ha='center', va='center',
                fontsize=11, color=WHITE, fontweight='bold')
    if title:
        ax.set_title(title, color=TEAL, fontsize=11, fontweight='bold', pad=8)
    return wedges

def hbar(ax, labels, values, colors, title='', unit='%', max_val=None):
    ax.set_facecolor('#162A44')
    ax.spines[:].set_visible(False)
    ax.tick_params(colors=GREY_L, labelsize=9)
    ax.xaxis.label.set_color(GREY_L)
    if max_val is None:
        max_val = max(values) * 1.15
    y = range(len(labels))
    bars = ax.barh(list(y), values, color=colors, height=0.6, edgecolor='none')
    ax.set_xlim(0, max_val)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, color=WHITE, fontsize=9)
    ax.xaxis.set_visible(False)
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + max_val*0.01, bar.get_y() + bar.get_height()/2,
                f'{val}{unit}', va='center', ha='left', color=GREY_L, fontsize=9)
    if title:
        ax.set_title(title, color=TEAL, fontsize=10, fontweight='bold')
    ax.invert_yaxis()

def supplier_card(fig, ax_pos, name, tier, pct, note, color, recent=''):
    ax = fig.add_axes(ax_pos, facecolor='#162A44')
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0.94),1,0.06, color=color))
    ax.text(0.5, 0.97, tier, ha='center', va='center', fontsize=8, color=NAVY, fontweight='bold')
    ax.text(0.5, 0.80, name, ha='center', va='center', fontsize=13, color=WHITE, fontweight='bold')
    ax.text(0.5, 0.64, pct,  ha='center', va='center', fontsize=20, color=color, fontweight='bold')
    ax.text(0.5, 0.48, note, ha='center', va='center', fontsize=8,  color=GREY_L,
            multialignment='center', wrap=True)
    if recent:
        ax.add_patch(plt.Rectangle((0.05,0.08),0.9,0.30, color='#0D1B2A', alpha=0.8))
        ax.text(0.5, 0.27, 'Recent Peru project:', ha='center', va='center',
                fontsize=7, color=TEAL, fontweight='bold')
        ax.text(0.5, 0.14, recent, ha='center', va='center', fontsize=7.5, color=WHITE,
                multialignment='center')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — COVER
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
ax = fig.add_axes([0,0,1,1], facecolor=NAVY); ax.axis('off')
ax.add_patch(plt.Rectangle((0,0),0.025,1, color=TEAL, transform=ax.transAxes))
ax.add_patch(plt.Rectangle((0.025,0.52),0.975,0.004, color=TEAL))
ax.add_patch(plt.Rectangle((0.025,0.38),0.975,0.003, color=AMBER))

ax.text(0.05, 0.76, 'PERU RENEWABLE ENERGY — BOS MARKET ANALYSIS',
        fontsize=14, color=TEAL, fontweight='bold', transform=ax.transAxes)
ax.text(0.05, 0.60, 'Supplier Intelligence\n& Market Structure',
        fontsize=52, color=WHITE, fontweight='bold', transform=ax.transAxes, linespacing=1.1)
ax.text(0.05, 0.44, 'Balance of System  ·  Solar PV  ·  Modules · Inverters · Trackers · Civil',
        fontsize=16, color=GREY_L, fontstyle='italic', transform=ax.transAxes)
ax.text(0.05, 0.33, 'Rev 1 — Infographic Edition  ·  Statkraft Procurement International  ·  February 2026',
        fontsize=13, color=AMBER, fontweight='bold', transform=ax.transAxes)
ax.text(0.05, 0.26, 'Prepared by: Aiden  ·  For: Jonathon Milne, VP Procurement International',
        fontsize=12, color=GREY_L, transform=ax.transAxes)

save_slide(fig, 1, 'cover')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — PIPELINE & COST OVERVIEW (visual KPIs + bar chart)
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'Peru Market Context', 'Pipeline scale & BOS cost structure at a glance', 2, 10)
add_footer(fig)

# KPI row
kpis = [
    ('20,000+\nMW', 'Development\npipeline', TEAL),
    ('938 MW', 'Solar\noperational\n(2025)', AMBER),
    ('2,362 MW', 'Solar target\n(2026)', GREEN),
    ('$700–900', '/kW all-in\nsolar CAPEX', TEAL),
    ('40–55%', 'of CAPEX\nis BOS', AMBER),
]
for i, (val, lbl, col) in enumerate(kpis):
    ax = fig.add_axes([0.02 + i*0.196, 0.60, 0.175, 0.27], facecolor='#162A44')
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.94),1,0.06, color=col))
    ax.text(0.5, 0.62, val, ha='center', va='center', fontsize=20,
            color=col, fontweight='bold', multialignment='center')
    ax.text(0.5, 0.22, lbl, ha='center', va='center', fontsize=9,
            color=GREY_L, multialignment='center')

# Pipeline bar chart
ax2 = fig.add_axes([0.04, 0.10, 0.52, 0.44], facecolor='#162A44')
scenarios = ['Current\n(2025)', 'Base Case\n2026', 'Base Case\n2028', 'Full Potential\n2030']
solar = [938, 2362, 3337, 15185]
wind  = [1021, 1021, 1867, 9344]
x = np.arange(len(scenarios))
w = 0.35
b1 = ax2.bar(x - w/2, solar, w, color=AMBER, label='Solar PV', edgecolor='none')
b2 = ax2.bar(x + w/2, wind,  w, color=TEAL,  label='Wind',     edgecolor='none')
ax2.set_facecolor('#162A44')
ax2.spines[:].set_visible(False)
ax2.set_xticks(x); ax2.set_xticklabels(scenarios, color=GREY_L, fontsize=9)
ax2.tick_params(colors=GREY_L)
ax2.set_ylabel('MW Installed', color=GREY_L, fontsize=9)
ax2.yaxis.label.set_color(GREY_L)
ax2.set_title('Capacity Trajectory — Solar vs Wind (MW)', color=TEAL, fontsize=10, fontweight='bold')
for b in list(b1)+list(b2):
    h = b.get_height()
    if h > 2000:
        ax2.text(b.get_x()+b.get_width()/2, h+200, f'{h:,.0f}',
                 ha='center', color=WHITE, fontsize=7)
ax2.legend(facecolor='#0D1B2A', edgecolor='none', labelcolor=WHITE, fontsize=9)

# BOS cost donut
ax3 = fig.add_axes([0.60, 0.08, 0.38, 0.50], facecolor=NAVY)
sizes  = [32, 9, 12, 6, 7, 5, 10, 10, 9]
labels = ['PV Modules\n32%', 'Inverters\n9%', 'Trackers\n12%',
          'Cabling\n6%', 'Transformers\n7%', 'Switchgear\n5%',
          'Civil Works\n10%', 'Grid Conn.\n10%', 'SCADA+Other\n9%']
colors = [AMBER, TEAL, GREEN, '#3498DB', PURPLE, '#1ABC9C', '#E67E22', RED, GREY_M]
ax3.set_facecolor(NAVY)
wedges, _ = ax3.pie(sizes, colors=colors, startangle=90,
                    wedgeprops=dict(width=0.55, edgecolor=NAVY, linewidth=2))
ax3.text(0, 0, 'BOS\nCost\nSplit', ha='center', va='center',
         fontsize=10, color=WHITE, fontweight='bold')
ax3.set_title('BOS Cost as % of Total CAPEX', color=TEAL, fontsize=10, fontweight='bold', pad=8)
ax3.legend(wedges, labels, loc='lower center', bbox_to_anchor=(0.5,-0.3),
           ncol=3, facecolor='#162A44', edgecolor='none', labelcolor=WHITE, fontsize=7.5)

save_slide(fig, 2, 'market_context')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — PV MODULE SUPPLIERS (market share + Peru presence)
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'BOS Component 1: PV Modules', 'Global market share & Peru supplier landscape', 3, 10)
add_footer(fig)

# Donut — global module market share
ax1 = fig.add_axes([0.02, 0.08, 0.38, 0.78], facecolor=NAVY)
m_sizes  = [13, 11, 11, 11, 7, 6, 5, 36]
m_labels = ['JinkoSolar 13%', 'LONGi 11%', 'Trina Solar 11%', 'JA Solar 11%',
            'TW Solar 7%', 'Astronergy 6%', 'Canadian Solar 5%', 'Others 36%']
m_colors = [TEAL, AMBER, GREEN, RED, PURPLE, '#1ABC9C', '#E67E22', GREY_M]
ax1.set_facecolor(NAVY)
w1, _ = ax1.pie(m_sizes, colors=m_colors, startangle=90,
                wedgeprops=dict(width=0.52, edgecolor=NAVY, linewidth=2))
ax1.text(0, 0, 'Global\nModule\nMarket\n2025', ha='center', va='center',
         fontsize=9, color=WHITE, fontweight='bold', multialignment='center')
ax1.set_title('Global PV Module Market Share (2025)', color=TEAL, fontsize=11, fontweight='bold')
ax1.legend(w1, m_labels, loc='lower center', bbox_to_anchor=(0.5,-0.22),
           ncol=2, facecolor='#162A44', edgecolor='none', labelcolor=WHITE, fontsize=8.5)

# Supplier cards (right)
cards = [
    ('JinkoSolar', '★ TOP PICK', '~13%\nglobal share', 'Dominant in LatAm utility-scale\nlowest $/W pricing, wide range\nof bifacial products', TEAL,
     'Clemesí 204MW (Moquegua)\nMatarani 97MW (Arequipa)'),
    ('LONGi', 'STRONG', '~11%\nglobal share', 'Premium quality / reliability\nHi-MO series bifacial\npreferred by European developers', AMBER,
     'Multiple Ica projects\nVillacuri pipeline'),
    ('Trina Solar', 'ACTIVE', '~11%\nglobal share', 'Competitive on large utility\nVertex series leading\nStrong LatAm distribution', GREEN,
     'Active in Arequipa corridor\n209MW pipeline'),
    ('JA Solar', 'ACTIVE', '~11%\nglobal share', 'Price competitive\nDeep Pocket bifacial modules\nGrowing Peru channel', PURPLE,
     'Ica Valley projects\nSan Pedro pipeline'),
]
positions = [
    [0.43, 0.53, 0.135, 0.42],
    [0.575, 0.53, 0.135, 0.42],
    [0.43, 0.08, 0.135, 0.42],
    [0.575, 0.08, 0.135, 0.42],
]
for (name, tier, pct, note, col, recent), pos in zip(cards, positions):
    supplier_card(fig, pos, name, tier, pct, note, col, recent)

# Note box
ax_note = fig.add_axes([0.72, 0.08, 0.27, 0.87], facecolor='#162A44')
ax_note.axis('off'); ax_note.set_xlim(0,1); ax_note.set_ylim(0,1)
ax_note.add_patch(plt.Rectangle((0,0.97),1,0.03, color=AMBER))
ax_note.text(0.5, 0.91, 'PROCUREMENT\nINSIGHTS', ha='center', fontsize=11,
             color=AMBER, fontweight='bold', multialignment='center')

insights = [
    ('100%', 'Import dependent', TEAL),
    ('~80%', 'China-origin\n(all major OEMs)', AMBER),
    ('48.5%', 'Top 4 combined\nglobal share', GREEN),
    ('0–6%', 'Peru import duty\n(FTA advantage)', TEAL),
]
y = 0.80
for val, lbl, col in insights:
    ax_note.text(0.5, y,     val, ha='center', fontsize=22, color=col, fontweight='bold')
    ax_note.text(0.5, y-0.07, lbl, ha='center', fontsize=8.5, color=GREY_L, multialignment='center')
    y -= 0.19

ax_note.add_patch(plt.Rectangle((0.05,0.05),0.9,0.18, color='#0D1B2A'))
ax_note.text(0.5, 0.20, '⚠  FEOC / ESG WATCH', ha='center', fontsize=9,
             color=AMBER, fontweight='bold')
ax_note.text(0.5, 0.12, 'All top-4 suppliers are Chinese.\nEuropean lenders require Xinjiang\nattestation & due diligence.',
             ha='center', fontsize=8, color=GREY_L, multialignment='center')

save_slide(fig, 3, 'pv_modules')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — INVERTER SUPPLIERS
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'BOS Component 2: Inverters', 'Global market share — Huawei & Sungrow dominate LatAm', 4, 10)
add_footer(fig)

# Donut — inverter market share
ax1 = fig.add_axes([0.02, 0.10, 0.35, 0.75], facecolor=NAVY)
inv_sizes  = [30, 25, 10, 8, 6, 21]
inv_colors = [TEAL, AMBER, GREEN, PURPLE, RED, GREY_M]
ax1.set_facecolor(NAVY)
w1, _ = ax1.pie(inv_sizes, colors=inv_colors, startangle=90,
                wedgeprops=dict(width=0.52, edgecolor=NAVY, linewidth=2))
ax1.text(0, 0, '589 GWac\nShipped\n(2024)', ha='center', va='center',
         fontsize=9, color=WHITE, fontweight='bold', multialignment='center')
ax1.set_title('Global Inverter Market Share (2025, est.)', color=TEAL, fontsize=11, fontweight='bold')
labels_inv = ['Huawei 30%', 'Sungrow 25%', 'SMA 10%', 'Ginlong/SE 8%', 'ABB 6%', 'Others 21%']
ax1.legend(w1, labels_inv, loc='lower center', bbox_to_anchor=(0.5,-0.16),
           ncol=2, facecolor='#162A44', edgecolor='none', labelcolor=WHITE, fontsize=9)

# Supplier cards
inv_cards = [
    ('Huawei',   '★ MARKET LEADER', '~30%\nglobal', 'Dominant in LatAm & Peru\nSun2000 string inverters\nLowest $/W, AI-optimised',
     TEAL, 'Most Peru utility projects\n(Clemesí, Matarani, Ica Valley)'),
    ('Sungrow',  '★ TOP CONTENDER', '~25%\nglobal', 'Strong LatAm growth 2023–25\nUS market #1\nCompetitive with Huawei',
     AMBER, 'Growing Peru footprint\nSan Pedro pipeline'),
    ('SMA',      'EUROPEAN PREMIUM', '~10%\nglobal', 'German engineering pedigree\nPreferred by IFC-funded projects\nHigher $/W, better ESG profile',
     GREEN, 'Smaller Peru presence\nUsed on IDB-backed projects'),
    ('ABB/Hitachi','HV SPECIALIST', '~6%\nglobal', 'Strong on MV/HV integration\nGrid-connected skid packages\nTrusted by European developers',
     PURPLE, 'Substation scope on\nKallpa projects'),
]
positions_inv = [
    [0.40, 0.53, 0.145, 0.42],
    [0.555, 0.53, 0.145, 0.42],
    [0.40, 0.08, 0.145, 0.42],
    [0.555, 0.08, 0.145, 0.42],
]
for (name, tier, pct, note, col, recent), pos in zip(inv_cards, positions_inv):
    supplier_card(fig, pos, name, tier, pct, note, col, recent)

# LatAm context box
ax_r = fig.add_axes([0.72, 0.08, 0.27, 0.87], facecolor='#162A44')
ax_r.axis('off'); ax_r.set_xlim(0,1); ax_r.set_ylim(0,1)
ax_r.add_patch(plt.Rectangle((0,0.97),1,0.03, color=TEAL))
ax_r.text(0.5, 0.91, 'LATAM / PERU\nCONTEXT', ha='center', fontsize=11,
          color=TEAL, fontweight='bold', multialignment='center')

latam_pts = [
    ('55%', 'Huawei + Sungrow\ncombined global share', TEAL),
    ('10th', 'consecutive year\nboth led rankings\n(Wood Mac 2025)', AMBER),
    ('~40%', 'Huawei est. share\nin Peru market', GREEN),
]
y = 0.81
for val, lbl, col in latam_pts:
    ax_r.text(0.5, y,     val, ha='center', fontsize=22, color=col, fontweight='bold')
    ax_r.text(0.5, y-0.08, lbl, ha='center', fontsize=8, color=GREY_L, multialignment='center')
    y -= 0.22

ax_r.add_patch(plt.Rectangle((0.05,0.04),0.9,0.22, color='#0D1B2A'))
ax_r.text(0.5, 0.22, 'PROCUREMENT STRATEGY', ha='center', fontsize=8.5,
          color=AMBER, fontweight='bold')
ax_r.text(0.5, 0.13, 'Dual-source: Huawei primary\n+ SMA for IFC-funded scope.\nNever sole-source on\n>50MW projects.',
          ha='center', fontsize=8, color=GREY_L, multialignment='center')

save_slide(fig, 4, 'inverters')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — TRACKER & MOUNTING SUPPLIERS
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'BOS Component 3: Trackers & Mounting', 'Single-axis tracker market — Nextracker leads globally & in LatAm', 5, 10)
add_footer(fig)

# Donut — tracker share
ax1 = fig.add_axes([0.02, 0.10, 0.35, 0.75], facecolor=NAVY)
tr_sizes  = [38, 18, 10, 8, 8, 18]
tr_colors = [TEAL, AMBER, GREEN, PURPLE, '#E67E22', GREY_M]
ax1.set_facecolor(NAVY)
w1, _ = ax1.pie(tr_sizes, colors=tr_colors, startangle=90,
                wedgeprops=dict(width=0.52, edgecolor=NAVY, linewidth=2))
ax1.text(0, 0, 'Single-Axis\nTracker\nMarket', ha='center', va='center',
         fontsize=9, color=WHITE, fontweight='bold', multialignment='center')
ax1.set_title('Global Solar Tracker Market Share (2025)', color=TEAL, fontsize=11, fontweight='bold')
labels_tr = ['Nextracker ~38%', 'Array Tech ~18%', 'Soltec ~10%',
             'Arctech ~8%', 'PVHardware ~8%', 'Others ~18%']
ax1.legend(w1, labels_tr, loc='lower center', bbox_to_anchor=(0.5,-0.16),
           ncol=2, facecolor='#162A44', edgecolor='none', labelcolor=WHITE, fontsize=9)

# Cards
tr_cards = [
    ('Nextracker', '★ GLOBAL #1', '~38%\nglobal share', 'Strongest Latam footprint\nAI-enabled TrueCapture\nAcquired robotics co. 2025',
     TEAL, 'Active across Ica & Arequipa\nPreferred tracker in Peru'),
    ('Array Tech', '★ STRONG #2', '~18%\nglobal share', 'US-listed, Mexico mfg. base\nOmniTrack dual-row system\nCompetitive on large flat sites',
     AMBER, 'Growing Peru presence\nSan Pedro pipeline project'),
    ('Soltec',     'LATAM FOCUS', '~10%\nglobal share', 'Spanish, strong LatAm network\nSF7 bifacial-optimised\nGood local support in Peru',
     GREEN, 'Installed on Ica corridor\nprojects — solid references'),
    ('Fixed Tilt\n(Local Steel)', 'COST OPTION', 'Variable', 'Local fabricators in Arequipa\n& Lima. 15–20% cheaper.\nSuitable for flat terrain',
     GREY_M, 'Used on smaller\n<50MW projects'),
]
pos_tr = [
    [0.40, 0.53, 0.145, 0.42],
    [0.555, 0.53, 0.145, 0.42],
    [0.40, 0.08, 0.145, 0.42],
    [0.555, 0.08, 0.145, 0.42],
]
for (name, tier, pct, note, col, recent), pos in zip(tr_cards, pos_tr):
    supplier_card(fig, pos, name, tier, pct, note, col, recent)

# Insight box
ax_r = fig.add_axes([0.72, 0.08, 0.27, 0.87], facecolor='#162A44')
ax_r.axis('off'); ax_r.set_xlim(0,1); ax_r.set_ylim(0,1)
ax_r.add_patch(plt.Rectangle((0,0.97),1,0.03, color=GREEN))
ax_r.text(0.5, 0.91, 'TRACKER vs.\nFIXED TILT', ha='center', fontsize=11,
          color=GREEN, fontweight='bold', multialignment='center')

pts = [
    ('+8–12%', 'yield gain with\ntracker (Peru irradiance)', TEAL),
    ('+$60–80\n/kW', 'cost premium\nvs fixed-tilt', AMBER),
    ('4–5 yr', 'payback on\ntracker premium', GREEN),
]
y = 0.80
for val, lbl, col in pts:
    ax_r.text(0.5, y,     val, ha='center', fontsize=18, color=col, fontweight='bold', multialignment='center')
    ax_r.text(0.5, y-0.09, lbl, ha='center', fontsize=8, color=GREY_L, multialignment='center')
    y -= 0.22

ax_r.add_patch(plt.Rectangle((0.05,0.04),0.9,0.22, color='#0D1B2A'))
ax_r.text(0.5, 0.22, 'RECOMMENDATION', ha='center', fontsize=8.5,
          color=GREEN, fontweight='bold')
ax_r.text(0.5, 0.12, 'Tracker justified on flat sites\n>50MW in Peru (Ica, Arequipa).\nNextracker #1 default;\nSoltec for competitive tension.',
          ha='center', fontsize=7.5, color=GREY_L, multialignment='center')

save_slide(fig, 5, 'trackers')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — EPC CONTRACTORS (Peru-specific experience)
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'EPC Contractors — Peru Experience', 'Who has built what — recent project track record', 6, 10)
add_footer(fig)

contractors = [
    {
        'name': 'ACCIONA',
        'type': 'International EPC',
        'origin': 'Spain',
        'color': TEAL,
        'tier': '★ MOST RECENT AWARD',
        'projects': ['225MW La Joya, Arequipa\n(Kallpa Generación, 2024)', 'Multiple LatAm references\n(Chile, Mexico, Brazil)'],
        'strength': 'Full turnkey EPC. European\nprocurement standards.\nStrong on Arequipa region.',
        'pos': [0.02, 0.50, 0.23, 0.45],
    },
    {
        'name': 'Grenergy',
        'type': 'Spanish Developer/EPC',
        'origin': 'Spain',
        'color': AMBER,
        'tier': 'ACTIVE IN PERU',
        'projects': ['Matarani 97MW EPC\n(Yinson Renewables, 2024)', 'O&M contract retained\npost-construction'],
        'strength': 'Developer with EPC arm.\nDeep Peru knowledge.\nGood for sub-200MW.',
        'pos': [0.26, 0.50, 0.23, 0.45],
    },
    {
        'name': 'Cosapi',
        'type': 'Local Civil/BOP',
        'origin': 'Peru',
        'color': GREEN,
        'tier': '★ TOP LOCAL CONTRACTOR',
        'projects': ['Cupisnique wind farm\n(civil/BOP, Ica)', 'Talara wind farm\n(civil works)', 'Multiple solar civil scopes'],
        'strength': 'Peru\'s largest civil contractor.\nDeep local relationships.\nEssential for BOP civil scope.',
        'pos': [0.50, 0.50, 0.23, 0.45],
    },
    {
        'name': 'JJC Contratistas',
        'type': 'Local Civil',
        'origin': 'Peru',
        'color': PURPLE,
        'tier': 'ESTABLISHED LOCAL',
        'projects': ['Solar park civil works\n(Ica region, multiple)', 'Road & access works\nfor wind projects'],
        'strength': 'Strong in earthworks,\nfoundations, access roads.\nGood for competitive tension\nvs Cosapi.',
        'pos': [0.74, 0.50, 0.23, 0.45],
    },
    {
        'name': 'Mota-Engil',
        'type': 'International Civil',
        'origin': 'Portugal',
        'color': '#E67E22',
        'tier': 'REGIONAL PRESENCE',
        'projects': ['Active in Peru infra\n(roads, civil)', 'Energy sector entry\n(2024–25 pipeline)'],
        'strength': 'Portuguese group with\nAfrica/LatAm footprint.\nGood #3 option for\ncivil competition.',
        'pos': [0.02, 0.05, 0.23, 0.42],
    },
    {
        'name': 'Sacyr',
        'type': 'Spanish EPC',
        'origin': 'Spain',
        'color': '#1ABC9C',
        'tier': 'REGIONAL EPC',
        'projects': ['LatAm energy projects\n(Chile, Colombia)', 'Peru pipeline studies\n(2025)'],
        'strength': 'Strong civil EPC capability.\nGood on Chile model\n(transferable to Peru).',
        'pos': [0.26, 0.05, 0.23, 0.42],
    },
    {
        'name': 'Graña y Montero\n(GMD/Stracon)',
        'type': 'Local Mining/Civil',
        'origin': 'Peru',
        'color': RED,
        'tier': 'EMERGING ENERGY',
        'projects': ['Mining civil works\n(transferable skills)', 'Energy sector entry\n(Ica region 2024)'],
        'strength': 'Peru\'s largest industrial\ncontractor. Heavy civil\ncapability. Newer to\nrenewables.',
        'pos': [0.50, 0.05, 0.23, 0.42],
    },
]
for c in contractors:
    ax = fig.add_axes(c['pos'], facecolor='#162A44')
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.95),1,0.05, color=c['color']))
    ax.text(0.5, 0.97, c['tier'],   ha='center', va='center', fontsize=7.5, color=NAVY, fontweight='bold')
    ax.text(0.5, 0.87, c['name'],   ha='center', va='center', fontsize=13, color=WHITE, fontweight='bold', multialignment='center')
    ax.text(0.5, 0.79, f"{c['type']} · {c['origin']}", ha='center', fontsize=8, color=GREY_L)
    ax.add_patch(plt.Rectangle((0.03,0.55),0.94,0.22, color='#0D1B2A'))
    ax.text(0.5, 0.68, 'RECENT PROJECTS', ha='center', fontsize=7.5, color=c['color'], fontweight='bold')
    for i, proj in enumerate(c['projects'][:2]):
        ax.text(0.5, 0.61-i*0.08, proj, ha='center', fontsize=7, color=WHITE, multialignment='center')
    ax.text(0.5, 0.37, c['strength'], ha='center', fontsize=8, color=GREY_L, multialignment='center')

# Insight strip
ax_strip = fig.add_axes([0.74, 0.05, 0.25, 0.42], facecolor='#162A44')
ax_strip.axis('off'); ax_strip.set_xlim(0,1); ax_strip.set_ylim(0,1)
ax_strip.add_patch(plt.Rectangle((0,0.96),1,0.04, color=AMBER))
ax_strip.text(0.5, 0.88, 'STRATEGIC\nACTION', ha='center', fontsize=11,
              color=AMBER, fontweight='bold', multialignment='center')
tips = [
    '1.  Pre-qualify Cosapi & JJC\n    NOW — before pipeline unlocks',
    '2.  ACCIONA is the go-to\n    for full EPC on >100MW',
    '3.  Use Grenergy for mid-size\n    (their Peru track record is real)',
    '4.  Always dual-source civil\n    Cosapi + one other',
    '5.  Mota-Engil as #3 option\n    for competitive tension',
]
y = 0.77
for tip in tips:
    ax_strip.text(0.05, y, tip, fontsize=8, color=GREY_L, va='top')
    y -= 0.16

save_slide(fig, 6, 'epc_contractors')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — SUPPLY CHAIN ORIGIN (visual import map)
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'Supply Chain Origin & Import Dependency', 'Where does Peru\'s BOS equipment actually come from?', 7, 10)
add_footer(fig)

# Big horizontal bar chart — import dependency
ax_main = fig.add_axes([0.04, 0.10, 0.58, 0.80], facecolor='#162A44')
items = ['PV Modules', 'Wind Turbines', 'Inverters', 'SCADA/Controls',
         'MV/HV Transformers', 'Switchgear', 'Tracker Systems', 'HV Cabling',
         'DC/AC Cables', 'Civil Works', 'Concrete & Aggregate']
pcts  = [100, 100, 95, 90, 70, 70, 70, 60, 45, 12, 5]
cols  = [RED if p>=90 else AMBER if p>=55 else GREEN for p in pcts]
hbar(ax_main, items, pcts, cols, 'Import Dependency by Component  (% of value imported)',
     unit='%', max_val=115)

# Legend
leg_items = [
    (RED,   '≥90% imported — critical dependency'),
    (AMBER, '55–89% imported — moderate dependency'),
    (GREEN, '<55% imported — local capability exists'),
]
y_leg = 0.13
for col, lbl in leg_items:
    ax_main.add_patch(plt.Rectangle((2, y_leg*11-0.4), 4, 0.7, color=col, transform=ax_main.transData))
    ax_main.text(7, y_leg*11, lbl, color=WHITE, fontsize=8, va='center')
    y_leg += 0.07

# Origin breakdown (right)
origins = [
    ('China', 78, TEAL, 'Modules, inverters, cable, steel'),
    ('Europe', 12, AMBER, 'SCADA, transformers, switchgear'),
    ('USA', 6, GREEN, 'Tracker systems (Nextracker)'),
    ('Local (Peru)', 4, PURPLE, 'Civil, cable, basic fabrication'),
]
ax_orig = fig.add_axes([0.66, 0.45, 0.32, 0.45], facecolor=NAVY)
o_sizes = [o[1] for o in origins]
o_colors = [o[2] for o in origins]
ax_orig.set_facecolor(NAVY)
w2, _ = ax_orig.pie(o_sizes, colors=o_colors, startangle=90,
                    wedgeprops=dict(width=0.55, edgecolor=NAVY, linewidth=2))
ax_orig.text(0, 0, 'BOS\nOrigin\nMix', ha='center', va='center',
             fontsize=9, color=WHITE, fontweight='bold', multialignment='center')
ax_orig.set_title('Equipment Origin — Peru BOS', color=TEAL, fontsize=10, fontweight='bold')
ax_orig.legend(w2, [f"{o[0]} {o[1]}%" for o in origins],
               loc='lower center', bbox_to_anchor=(0.5,-0.22),
               ncol=2, facecolor='#162A44', edgecolor='none', labelcolor=WHITE, fontsize=8.5)

# Key risk callouts
risks_r = [
    ('FEOC Risk', 'Chinese supply chain\ndominance — requires\ndue diligence for EU\nlenders', AMBER),
    ('Lead Times', 'HV transformers:\n10–14 months globally.\nOrder at FID or earlier.', RED),
    ('Local Value', 'Civil works only.\n~12% local content\nrealistic maximum.', GREEN),
]
y_r = 0.08
for title, body, col in risks_r:
    ax_r = fig.add_axes([0.66, y_r, 0.32, 0.11], facecolor='#162A44')
    ax_r.axis('off'); ax_r.set_xlim(0,1); ax_r.set_ylim(0,1)
    ax_r.add_patch(plt.Rectangle((0,0),0.03,1, color=col))
    ax_r.text(0.05, 0.72, title, fontsize=10, color=col, fontweight='bold')
    ax_r.text(0.05, 0.28, body, fontsize=8, color=GREY_L, multialignment='left')
    y_r += 0.125

save_slide(fig, 7, 'supply_chain')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — RISK HEAT MAP
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'BOS Procurement Risk Matrix', 'Likelihood vs Impact — Peru solar projects', 8, 10)
add_footer(fig)

# Risk scatter (heat map style)
ax = fig.add_axes([0.05, 0.10, 0.58, 0.80], facecolor='#162A44')
ax.spines[:].set_visible(False)
ax.set_facecolor('#162A44')
ax.set_xlim(0, 6); ax.set_ylim(0, 6)
ax.set_xlabel('LIKELIHOOD →', color=GREY_L, fontsize=10, labelpad=8)
ax.set_ylabel('IMPACT →', color=GREY_L, fontsize=10, labelpad=8)
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(['Very Low', 'Low', 'Medium', 'High', 'Very High'],
                   color=GREY_L, fontsize=8)
ax.set_yticks([1,2,3,4,5])
ax.set_yticklabels(['Negligible','Minor','Moderate','Major','Critical'],
                   color=GREY_L, fontsize=8)
ax.tick_params(colors=GREY_M)

# Background zones
ax.add_patch(plt.Rectangle((0,0), 2.5, 2.5, color='#1A3A1A', alpha=0.4))
ax.add_patch(plt.Rectangle((2.5,0), 2.5, 2.5, color='#3A3A1A', alpha=0.4))
ax.add_patch(plt.Rectangle((0,2.5), 2.5, 2.5, color='#3A3A1A', alpha=0.4))
ax.add_patch(plt.Rectangle((2.5,2.5), 3.5, 3.5, color='#3A1A1A', alpha=0.4))

ax.text(1.2, 1.2, 'LOW\nRISK', ha='center', fontsize=9, color=GREEN, alpha=0.6, fontweight='bold')
ax.text(3.7, 1.2, 'WATCH', ha='center', fontsize=9, color=AMBER, alpha=0.6, fontweight='bold')
ax.text(1.2, 3.7, 'WATCH', ha='center', fontsize=9, color=AMBER, alpha=0.6, fontweight='bold')
ax.text(4.0, 4.0, 'CRITICAL\nRISK ZONE', ha='center', fontsize=9, color=RED, alpha=0.7, fontweight='bold', multialignment='center')

risks_scatter = [
    (4.5, 4.8, 'Grid connection\ndelay', RED, 'G'),
    (4.2, 4.5, 'HV transformer\nshortage', RED, 'T'),
    (4.3, 4.2, 'MINEM permitting\ndelay', RED, 'P'),
    (3.8, 3.5, 'Civil contractor\ncapacity', AMBER, 'C'),
    (3.5, 3.8, 'PPA unavailability', AMBER, 'PPA'),
    (3.0, 2.8, 'Customs delay', AMBER, 'CU'),
    (3.2, 2.5, 'PEN inflation\n(civil costs)', AMBER, '$'),
    (1.8, 3.5, 'FEOC/ESG\nscrutiny', GREEN, 'F'),
    (1.5, 2.0, 'Single-source OEM', GREEN, 'S'),
]
for x, y, lbl, col, code in risks_scatter:
    ax.scatter(x, y, s=300, color=col, zorder=5, edgecolors=NAVY, linewidth=1.5)
    ax.text(x, y+0.08, code, ha='center', fontsize=7, color=NAVY, fontweight='bold', zorder=6, va='bottom')
    ax.annotate(lbl, (x, y), xytext=(x+0.25, y+0.3),
                fontsize=7, color=WHITE,
                arrowprops=dict(arrowstyle='->', color=GREY_M, lw=0.8),
                multialignment='center')

ax.set_title('BOS/BOP Procurement Risk — Likelihood vs Impact', color=TEAL, fontsize=11, fontweight='bold')

# Legend / key
ax_leg = fig.add_axes([0.66, 0.10, 0.32, 0.80], facecolor='#162A44')
ax_leg.axis('off'); ax_leg.set_xlim(0,1); ax_leg.set_ylim(0,1)
ax_leg.add_patch(plt.Rectangle((0,0.96),1,0.04, color=RED))
ax_leg.text(0.5, 0.92, 'RISK KEY & MITIGATIONS', ha='center', fontsize=10,
            color=RED, fontweight='bold')

risk_keys = [
    ('G', RED,   'Grid connection delay',    'Owner-procure; 20% contingency'),
    ('T', RED,   'HV transformer shortage',  'Order at FID; frame ABB/Hitachi'),
    ('P', RED,   'MINEM permitting delay',   'Gate spend to final concession'),
    ('C', AMBER, 'Civil contractor capacity','Pre-qualify Cosapi/JJC now'),
    ('PPA',AMBER,'PPA unavailability',       'NTP-linked procurement structure'),
    ('CU',AMBER, 'Customs clearance delay',  'Specialist broker; buffer lead times'),
    ('$', AMBER, 'PEN inflation',            'CPI clauses on civil contracts'),
    ('F', GREEN, 'FEOC/ESG scrutiny',        'Attestations in pre-qual'),
    ('S', GREEN, 'Single-source OEM',        'Dual-source strategy at FID'),
]
y = 0.87
for code, col, name, mit in risk_keys:
    ax_leg.add_patch(plt.Circle((0.05, y-0.01), 0.028, color=col))
    ax_leg.text(0.065, y-0.01, code,  ha='center', va='center', fontsize=7, color=NAVY, fontweight='bold')
    ax_leg.text(0.12, y+0.01, name,  fontsize=8.5, color=WHITE, fontweight='bold')
    ax_leg.text(0.12, y-0.04, mit,   fontsize=7.5, color=GREY_L)
    ax_leg.plot([0.02, 0.98], [y-0.075, y-0.075], color=DIVIDER if 'DIVIDER' in dir() else '#1E3A5F', linewidth=0.4)
    y -= 0.098

save_slide(fig, 8, 'risk_matrix')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — MARKET SCORECARD (visual dot rating)
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'Market Scorecard & Strategic Summary', 'Peru BOS — Procurement readiness assessment', 9, 10)
add_footer(fig)

scores = [
    ('Market Growth Potential',      5, GREEN,  '20 GW pipeline; 15%+ CAGR; government-committed'),
    ('Module Supply Chain',           4, TEAL,   'Established import channels; 4 strong global OEMs'),
    ('Inverter Supply Chain',         4, TEAL,   'Huawei/Sungrow dominant; SMA for ESG-sensitive deals'),
    ('Tracker/Mounting Supply',       4, TEAL,   'Nextracker leads; Soltec for LatAm competition'),
    ('Local Civil Capability',        4, GREEN,  'Cosapi/JJC strong; capacity constraint as volume builds'),
    ('Grid Infrastructure',           2, RED,    'Transmission bottleneck; $430M plan insufficient'),
    ('PPA / Offtake Maturity',        2, RED,    'Underdeveloped; Law 32249 improving but slow'),
    ('Regulatory Environment',        3, AMBER,  'MINEM concession queue constrains deployment pace'),
    ('Procurement Complexity',        1, RED,    'HIGH: imports, grid risk, FX, contractor capacity'),
]

ax_scores = fig.add_axes([0.03, 0.08, 0.60, 0.82], facecolor='#162A44')
ax_scores.axis('off'); ax_scores.set_xlim(0,1); ax_scores.set_ylim(0,1)
ax_scores.add_patch(plt.Rectangle((0,0.96),1,0.04, color=TEAL))
ax_scores.text(0.02, 0.965, 'DIMENSION', fontsize=9, color=NAVY, fontweight='bold', va='center')
ax_scores.text(0.65, 0.965, 'RATING', fontsize=9, color=NAVY, fontweight='bold', va='center', ha='center')
ax_scores.text(0.79, 0.965, 'COMMENTARY', fontsize=9, color=NAVY, fontweight='bold', va='center')

y = 0.88
for i, (label, score, col, comment) in enumerate(scores):
    bg = '#10223A' if i%2==0 else '#162A44'
    ax_scores.add_patch(plt.Rectangle((0,y-0.085),1,0.09, color=bg))
    ax_scores.add_patch(plt.Rectangle((0,y-0.085),0.012,0.09, color=col))
    ax_scores.text(0.02, y-0.035, label, fontsize=10, color=WHITE, fontweight='bold', va='center')
    for d in range(5):
        fc = col if d < score else '#1E3A5F'
        ax_scores.add_patch(plt.Rectangle((0.60+d*0.04, y-0.065), 0.032, 0.05, color=fc))
    ax_scores.text(0.82, y-0.035, comment, fontsize=8, color=GREY_L, va='center')
    y -= 0.098

# Verdict box
ax_v = fig.add_axes([0.66, 0.08, 0.32, 0.82], facecolor='#162A44')
ax_v.axis('off'); ax_v.set_xlim(0,1); ax_v.set_ylim(0,1)
ax_v.add_patch(plt.Rectangle((0,0.96),1,0.04, color=TEAL))
ax_v.text(0.5, 0.89, 'OVERALL\nVERDICT', ha='center', fontsize=16,
          color=TEAL, fontweight='bold', multialignment='center')

ax_v.text(0.5, 0.77, '⭐⭐⭐⭐', ha='center', fontsize=24, color=AMBER)
ax_v.text(0.5, 0.70, 'Strong Opportunity\nHigh Complexity', ha='center', fontsize=12,
          color=WHITE, fontweight='bold', multialignment='center')

ax_v.add_patch(plt.Rectangle((0.05,0.52),0.9,0.15, color='#0D1B2A'))
ax_v.text(0.5, 0.63, 'PROCUREMENT WINDOW', ha='center', fontsize=9, color=AMBER, fontweight='bold')
ax_v.text(0.5, 0.56, 'Act now — before the\n20 GW pipeline unlocks\nand market tightens', ha='center',
          fontsize=9, color=GREY_L, multialignment='center')

actions = [
    ('1', 'Frame agreements:\nNextracker + Array Tech', TEAL),
    ('2', 'Pre-qualify: Cosapi,\nJJC, Mota-Engil', AMBER),
    ('3', 'Module shortlist:\nJinko + LONGi + Trina', GREEN),
    ('4', 'Inverter: Huawei primary\n+ SMA for IFC scope', TEAL),
    ('5', 'Owner-procure grid;\n20% cost contingency', RED),
]
y_a = 0.47
for num, txt, col in actions:
    ax_v.add_patch(plt.Rectangle((0.03, y_a-0.02), 0.14, 0.085, color=col))
    ax_v.text(0.10, y_a+0.022, num, ha='center', va='center', fontsize=14,
              color=NAVY, fontweight='bold')
    ax_v.text(0.22, y_a+0.025, txt, fontsize=8, color=WHITE, va='center')
    y_a -= 0.09

save_slide(fig, 9, 'scorecard')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — RECOMMENDATIONS
# ═══════════════════════════════════════════════════════════════════════════════
fig = navy_fig()
add_header(fig, 'Strategic Procurement Recommendations', 'Statkraft Peru BOS — Priority Actions for 2026', 10, 10)
add_footer(fig)

recs = [
    (TEAL,  '01', 'Establish Supplier Pre-Qualification Now',
     'Issue RFQs to module, inverter and tracker suppliers before pipeline pressure builds.\nJinkoSolar/LONGi (modules) · Huawei/SMA (inverters) · Nextracker/Soltec (trackers).\nInclusion of Xinjiang attestation and ESG questionnaire in pre-qual pack.',
     'Q1 2026'),
    (AMBER, '02', 'Frame Agreements: Trackers & Transformers First',
     'HV transformers are 10–14 month critical path items in global shortage. Lock supply now.\nNextracker and Array Tech have Latam coverage — early engagement = pricing leverage.\nTarget signed frame agreements before MINEM pipeline unlocks (est. mid-2026).',
     'Q1–Q2 2026'),
    (GREEN, '03', 'Pre-Qualify & Reserve Civil Contractor Capacity',
     'Cosapi and JJC are Peru\'s go-to civil contractors. ACCIONA and Grenergy for full EPC.\nCapacity will be absorbed quickly as 19+ projects break ground simultaneously.\nConsider early works contracts or LOIs to secure scheduling priority.',
     'Q2 2026'),
    (TEAL,  '04', 'Owner-Procure Grid Connection',
     'Grid connection is the highest-risk procurement item in Peru. Do not wrap in EPC.\nEngage REP/ISA/COES directly. Build 15–20% contingency into budget.\nGrid cost variance: $30/kW (near existing lines) to $150+/kW (remote sites).',
     'Immediate'),
    (RED,   '05', 'Gate All Procurement Spend to MINEM Concession',
     'With 95 of 114 projects still pending final concession, procurement risk is real.\nStructure NTP-linked procurement — no committed spend before final concession confirmed.\nKeep supplier relationships warm without financial commitments.',
     'Standing policy'),
    (AMBER, '06', 'Build Dual-Source Strategy Across All Categories',
     'Never sole-source inverters, trackers or modules on projects >50MW.\nHuawei + SMA · Nextracker + Soltec · Jinko + LONGi · Cosapi + JJC.\nCompetitive tension in a capacity-constrained market requires early dual-source commitment.',
     'All projects'),
]

positions_recs = [
    [0.02, 0.53, 0.47, 0.41],
    [0.51, 0.53, 0.47, 0.41],
    [0.02, 0.10, 0.47, 0.41],
    [0.51, 0.10, 0.47, 0.41],
]
# Put recs 1-4 in 2x2 grid, recs 5-6 as bottom strip
for i, (col, num, title, body, timing) in enumerate(recs[:4]):
    ax = fig.add_axes(positions_recs[i], facecolor='#162A44')
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0),0.012,1, color=col))
    ax.add_patch(plt.Rectangle((0.015,0.75),0.12,0.22, color=col))
    ax.text(0.075, 0.86, num, ha='center', va='center', fontsize=24, color=NAVY, fontweight='bold')
    ax.text(0.15, 0.89, title, fontsize=12, color=col, fontweight='bold', va='center')
    ax.text(0.15, 0.72, f'⏱  {timing}', fontsize=8, color=AMBER, va='center')
    for j, line in enumerate(body.split('\n')[:3]):
        ax.text(0.025, 0.58-j*0.17, '→  '+line.strip(), fontsize=8.5, color=GREY_L, va='top')

# Bottom two as wide strips
for i, (col, num, title, body, timing) in enumerate(recs[4:]):
    ax = fig.add_axes([0.02 + i*0.49, 0.02, 0.47, 0.07], facecolor='#162A44')
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0),0.006,1, color=col))
    ax.text(0.015, 0.72, f'{num}: {title}', fontsize=9, color=col, fontweight='bold', va='center')
    ax.text(0.015, 0.25, body.split('\n')[0], fontsize=8, color=GREY_L, va='center')

save_slide(fig, 10, 'recommendations')

print('\n✅  All 10 slides rendered.')
print(f'    Output: {OUT}')
