"""Regenerate Slide 2 — Market Context (no BOS cost donut)"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = '/tmp/peru_rev1'
NAVY='#0D1B2A'; NAVY_L='#162A44'; TEAL='#00B4D8'
AMBER='#F5A623'; GREEN='#2ECC71'; RED='#E74C3C'
WHITE='#FFFFFF'; GREY_L='#B0BEC5'; GREY_M='#546E7A'

def add_header(fig, title, subtitle='', page=1, total=10):
    ax = fig.add_axes([0,0.88,1,0.12], facecolor='#162A44')
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0),0.015,1, color=TEAL))
    ax.text(0.025,0.62, title, fontsize=22, color=WHITE, fontweight='bold', va='center')
    ax.text(0.025,0.22, subtitle, fontsize=11, color=GREY_L, fontstyle='italic', va='center')
    ax.text(0.99,0.5, f'STATKRAFT · CONFIDENTIAL  |  {page}/{total}',
            fontsize=9, color=GREY_M, ha='right', va='center')

def add_footer(fig):
    ax = fig.add_axes([0,0,1,0.035], facecolor='#162A44')
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.text(0.015, 0.5, 'Peru BOS/BOP Market Analysis — Rev 1 · Statkraft Procurement · February 2026',
            fontsize=8.5, color=GREY_M, va='center')

fig = plt.figure(figsize=(19.2, 10.8), facecolor=NAVY, dpi=100)
add_header(fig, 'Peru Market Context', 'Pipeline scale, regional breakdown & development status', 2, 10)
add_footer(fig)

# ── Row 1: 5 KPI boxes ──────────────────────────────────────────────────────
kpis = [
    ('20,000+\nMW',   'Total development\npipeline (solar+wind)', TEAL),
    ('938 MW',        'Solar operational\ntoday (2025)',          AMBER),
    ('2,362 MW',      'Solar target\nby end-2026',               GREEN),
    ('19 / 114',      'Projects with\nfinal MINEM concession',   RED),
    ('$700–900/kW',   'All-in solar CAPEX\n(utility-scale Peru)', TEAL),
]
for i, (val, lbl, col) in enumerate(kpis):
    ax = fig.add_axes([0.02+i*0.196, 0.62, 0.175, 0.25], facecolor=NAVY_L)
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.93),1,0.07, color=col))
    ax.text(0.5, 0.60, val, ha='center', va='center', fontsize=20,
            color=col, fontweight='bold', multialignment='center')
    ax.text(0.5, 0.20, lbl, ha='center', va='center', fontsize=9,
            color=GREY_L, multialignment='center')

# ── Row 2 left: Capacity trajectory bar chart ─────────────────────────────
ax_bar = fig.add_axes([0.03, 0.09, 0.44, 0.49], facecolor=NAVY_L)
scenarios = ['2025\n(Now)', 'Base 2026', 'Base 2027', 'Base 2028', 'Full\nPotential 2030']
solar = [938, 2362, 3242, 3337, 15185]
wind  = [1021, 1021, 1867, 1867, 9344]
x = np.arange(len(scenarios))
w = 0.35
b1 = ax_bar.bar(x-w/2, solar, w, color=AMBER, label='Solar PV', edgecolor='none')
b2 = ax_bar.bar(x+w/2, wind,  w, color=TEAL,  label='Wind',     edgecolor='none')
ax_bar.set_facecolor(NAVY_L)
ax_bar.spines[:].set_visible(False)
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(scenarios, color=GREY_L, fontsize=9)
ax_bar.tick_params(colors=GREY_M)
ax_bar.set_ylabel('Installed Capacity (MW)', color=GREY_L, fontsize=9)
ax_bar.set_title('Capacity Trajectory — Base Case vs Full Pipeline', color=TEAL,
                 fontsize=10, fontweight='bold')
ax_bar.legend(facecolor=NAVY, edgecolor='none', labelcolor=WHITE, fontsize=9)
for b in list(b1)+list(b2):
    h = b.get_height()
    if h > 1500:
        ax_bar.text(b.get_x()+b.get_width()/2, h+150, f'{h:,.0f}',
                    ha='center', color=WHITE, fontsize=7)

# ── Row 2 right: Regional development table ───────────────────────────────
ax_r = fig.add_axes([0.50, 0.09, 0.48, 0.49], facecolor=NAVY_L)
ax_r.axis('off'); ax_r.set_xlim(0,1); ax_r.set_ylim(0,1)
ax_r.add_patch(plt.Rectangle((0,0.90),1,0.10, color=TEAL))
ax_r.text(0.5, 0.95, 'KEY DEVELOPMENT REGIONS & RECENT PROJECTS',
          ha='center', va='center', fontsize=10, color=NAVY, fontweight='bold')

regions = [
    (AMBER,'ICA',        'Solar+Wind',  '★ Villacuri 470MW solar  ·  Wayra 72MW solar\nSan Pedro 1,800MW solar pipeline\nIca wind corridor (500MW Inkia)'),
    (TEAL, 'PIURA',      'Wind Hub',    'Bayóvar Wind Farm — $1.056B investment\nStrongest wind resource in Peru\nExisting turbine infrastructure'),
    (GREEN,'AREQUIPA',   'Solar Prime', 'La Joya 225MW (ACCIONA EPC, 2024)\nClemesí 204MW · Matarani 97MW\nAttacama fringe — GHI >6.5 kWh/m²/day'),
    (PURPLE if False else '#9B59B6',
           'LAMBAYEQUE', 'Wind',        'Mórrope Wind Farm — $353M investment\nSecondary wind corridor'),
    (GREY_M,'MOQUEGUA',  'Solar',       'Sunny Solar 204MW (Kallpa)\nExpanding to 309MW in 2026'),
]
PURPLE='#9B59B6'
y = 0.83
for col, region, tech, projects in regions:
    ax_r.add_patch(plt.Rectangle((0.01, y-0.14), 0.98, 0.155, color='#0D1B2A'))
    ax_r.add_patch(plt.Rectangle((0.01, y-0.14), 0.04, 0.155, color=col))
    ax_r.text(0.065, y-0.03,  region, fontsize=10, color=col,   fontweight='bold', va='center')
    ax_r.text(0.30,  y-0.03,  f'[{tech}]', fontsize=8.5, color=GREY_L, va='center')
    for i, line in enumerate(projects.split('\n')[:2]):
        ax_r.text(0.065, y-0.075-i*0.038, line, fontsize=8, color=WHITE, va='center')
    y -= 0.175

path = f'{OUT}/slide_02_market_context_v2.jpg'
fig.savefig(path, bbox_inches='tight', pad_inches=0, facecolor=NAVY, dpi=100)
plt.close(fig)
print(f'Saved: {path}')
