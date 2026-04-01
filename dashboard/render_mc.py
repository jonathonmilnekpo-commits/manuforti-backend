import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import textwrap

# ─── Colours ───────────────────────────────────────────────────────────────
BG       = '#0f1117'
SURFACE  = '#1a1d27'
SURFACE2 = '#22263a'
BORDER   = '#2e334d'
TEXT     = '#e8eaf0'
MUTED    = '#6b7280'
ACCENT   = '#6366f1'
GREEN    = '#10b981'
YELLOW   = '#f59e0b'
RED      = '#ef4444'
BLUE     = '#3b82f6'
PINK     = '#ec4899'
PURPLE   = '#8b5cf6'

PILLAR_COLS = {
    'Father':  BLUE,
    'Husband': PINK,
    'Career':  YELLOW,
    'Venture': ACCENT,
    'Self':    GREEN,
}
TAG_BG = {
    'Father':  '#1e2f4d',
    'Husband': '#3d1f2f',
    'Career':  '#3d2e10',
    'Venture': '#25204d',
    'Self':    '#0d3020',
}

# ─── Data ──────────────────────────────────────────────────────────────────
COLUMNS = {
    '⚡ NOW': {
        'color': BLUE,
        'tasks': [
            ('Father',  'Buy slippers for Ingrid (size 21)'),
            ('Father',  'Prepare for baby #2 (due 1 June)'),
            ('Husband', 'Check in on Ragnhild this week'),
            ('Career',  '"Why you over others" answer'),
            ('Career',  'Statkraft board priorities 2025–30'),
            ('Career',  'Sharpen Latam complexity narrative'),
            ('Venture', 'Identify 1–3 people for first report'),
            ('Venture', 'Define report template + price'),
            ('Self',    'Maintain weight: 77.1kg target'),
        ]
    },
    '📌 NEXT': {
        'color': YELLOW,
        'tasks': [
            ('Father',  'Set up paternity leave routine'),
            ('Father',  'Baby-proof remaining areas'),
            ('Husband', 'Plan something for Ragnhild before baby'),
            ('Career',  'Mock interview with Aiden'),
            ('Career',  'Prepare reference list'),
            ('Career',  'Define 90-day SVP plan'),
            ('Venture', 'Deliver first manual report'),
            ('Self',    'Weekly review habit (Sunday?)'),
        ]
    },
    '⏳ WAITING': {
        'color': RED,
        'tasks': [
            ('Father',  'Baby #2 name decision'),
            ('Career',  'Interview date (pending HR)'),
            ('Venture', 'SVP outcome → venture pace'),
        ]
    },
    '✅ DONE': {
        'color': GREEN,
        'tasks': [
            ('Self',    'OpenClaw fully operational'),
            ('Self',    'Aiden (AI co-founder) live'),
            ('Career',  'Procurement Vision PPTX'),
            ('Career',  'Peru BOS/BOP Analysis delivered'),
            ('Venture', 'Evaluated two AI biz plans'),
            ('Venture', 'Decided: sell one report first'),
            ('Father',  'AI assistant for family logistics'),
        ]
    },
    '💭 SOMEDAY': {
        'color': MUTED,
        'tasks': [
            ('Father',  'Digital journal for Ingrid'),
            ('Husband', 'Date night system (post-baby)'),
            ('Career',  'LinkedIn thought leader build'),
            ('Venture', 'Supplier Intelligence SaaS'),
            ('Venture', 'Fractional CPO offering'),
            ('Venture', 'Nordic compliance tool'),
            ('Self',    'Reading list + learning plan'),
        ]
    },
}

PILLAR_SUMMARY = [
    ('👨‍👧', 'FATHER',  'Present & intentional with\nIngrid and baby #2',  BLUE),
    ('💑',   'HUSBAND', 'Strong, present partner\nto Ragnhild',           PINK),
    ('💼',   'CAREER',  'Secure SVP Procurement\nat Statkraft',           YELLOW),
    ('🚀',   'VENTURE', 'First paid AI\nprocurement revenue',             ACCENT),
    ('🧠',   'SELF',    'Sharp, healthy\nand growing',                    GREEN),
]

# ─── Figure setup ──────────────────────────────────────────────────────────
FIG_W, FIG_H = 22, 14
fig = plt.figure(figsize=(FIG_W, FIG_H), facecolor=BG)

# Title bar
ax_title = fig.add_axes([0, 0.935, 1, 0.065])
ax_title.set_facecolor(SURFACE)
ax_title.set_xlim(0, 1); ax_title.set_ylim(0, 1)
ax_title.axis('off')
ax_title.add_patch(FancyBboxPatch((0,0), 1, 1, color=SURFACE, zorder=0))
ax_title.text(0.018, 0.55, '🤝', fontsize=22, va='center')
ax_title.text(0.055, 0.65, 'Aiden · Mission Control', color=TEXT,
              fontsize=15, fontweight='bold', va='center')
ax_title.text(0.055, 0.28, 'Jonathon Milne · Oslo, Norway', color=MUTED,
              fontsize=10, va='center')
ax_title.text(0.98, 0.5, '● Aiden Online  |  📱 WhatsApp  |  claude-sonnet-4-6  |  📍Oslo',
              color=MUTED, fontsize=9, va='center', ha='right')

# Pillar row
PIL_Y0 = 0.76; PIL_H = 0.155
n_pil = len(PILLAR_SUMMARY)
pil_w = 0.96 / n_pil
for i, (icon, name, goal, col) in enumerate(PILLAR_SUMMARY):
    x0 = 0.02 + i * (pil_w + 0.005)
    ax_p = fig.add_axes([x0, PIL_Y0, pil_w - 0.005, PIL_H])
    ax_p.set_facecolor(SURFACE)
    ax_p.set_xlim(0,1); ax_p.set_ylim(0,1)
    ax_p.axis('off')
    # top colour bar
    ax_p.add_patch(mpatches.Rectangle((0, 0.93), 1, 0.07, color=col, transform=ax_p.transAxes, clip_on=False))
    ax_p.text(0.5, 0.72, icon, fontsize=20, ha='center', va='center')
    ax_p.text(0.5, 0.50, name, color=TEXT, fontsize=10, fontweight='bold', ha='center', va='center')
    ax_p.text(0.5, 0.20, goal, color=MUTED, fontsize=7.5, ha='center', va='center',
              multialignment='center')

# Kanban
N_COLS = len(COLUMNS)
COL_X0  = 0.02
COL_Y0  = 0.02
COL_W   = (0.96 / N_COLS) - 0.007
COL_H   = 0.715
COL_GAP = 0.007

for ci, (col_name, col_data) in enumerate(COLUMNS.items()):
    x0 = COL_X0 + ci * (COL_W + COL_GAP)
    ax_c = fig.add_axes([x0, COL_Y0, COL_W, COL_H])
    ax_c.set_facecolor(SURFACE)
    ax_c.set_xlim(0, 1)
    ax_c.set_ylim(0, 1)
    ax_c.axis('off')

    tasks = col_data['tasks']
    col_color = col_data['color']
    is_done = col_name.startswith('✅')

    # Column header
    ax_c.add_patch(mpatches.Rectangle((0, 0.94), 1, 0.06, color=SURFACE2))
    ax_c.text(0.06, 0.971, col_name, color=col_color,
              fontsize=9.5, fontweight='bold', va='center')
    ax_c.text(0.94, 0.971, str(len(tasks)), color=MUTED,
              fontsize=8, va='center', ha='right')

    # Tasks
    n = len(tasks)
    slot_h = 0.93 / max(n, 1)
    card_h = min(slot_h * 0.85, 0.115)
    pad = 0.012

    for ti, (pillar, text) in enumerate(tasks):
        tag_col  = PILLAR_COLS[pillar]
        tag_bg   = TAG_BG[pillar]
        y_top    = 0.93 - ti * slot_h
        y_center = y_top - slot_h / 2

        # Card background
        card_y = y_center - card_h / 2
        ax_c.add_patch(FancyBboxPatch(
            (pad, card_y), 1 - 2*pad, card_h,
            boxstyle='round,pad=0.01', linewidth=0.6,
            edgecolor=BORDER, facecolor=SURFACE2
        ))

        # Pillar tag
        tag_w = 0.38; tag_h_frac = 0.032
        ax_c.add_patch(FancyBboxPatch(
            (pad + 0.015, card_y + card_h - tag_h_frac - 0.008),
            tag_w, tag_h_frac,
            boxstyle='round,pad=0.005', linewidth=0,
            facecolor=tag_bg
        ))
        ax_c.text(pad + 0.015 + tag_w/2,
                  card_y + card_h - tag_h_frac/2 - 0.008,
                  pillar, color=tag_col, fontsize=6.2,
                  fontweight='bold', va='center', ha='center')

        # Task text
        wrapped = textwrap.fill(text, width=28)
        alpha = 0.45 if is_done else 1.0
        ax_c.text(pad + 0.02, card_y + card_h * 0.38,
                  wrapped, color=TEXT, fontsize=6.8,
                  va='center', alpha=alpha,
                  linespacing=1.3)

        # Strikethrough for done
        if is_done:
            mid_y = card_y + card_h * 0.38
            ax_c.plot([pad + 0.02, 1 - pad - 0.02],
                      [mid_y, mid_y],
                      color=GREEN, linewidth=0.6, alpha=0.5)

# Save
out = '/Users/jonathonmilne/.openclaw/workspace/dashboard/mission_control.png'
plt.savefig(out, dpi=150, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print(f'Saved: {out}')
