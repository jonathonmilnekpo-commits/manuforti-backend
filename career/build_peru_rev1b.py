"""
Peru BOS Market Analysis — Rev 1b
Removes PV Modules & Inverters slides.
Replaces with: Cabling & Electrical + Transformers & HV Equipment.
True BOS focus: Trackers · Cabling · Transformers · Civil · Grid · SCADA
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = '/tmp/peru_rev1b'
os.makedirs(OUT, exist_ok=True)

NAVY='#0D1B2A'; NAVY_L='#162A44'; TEAL='#00B4D8'
AMBER='#F5A623'; GREEN='#2ECC71'; RED='#E74C3C'
WHITE='#FFFFFF'; GREY_L='#B0BEC5'; GREY_M='#546E7A'
PURPLE='#9B59B6'; ORANGE='#E67E22'; CYAN='#1ABC9C'

def new_fig():
    return plt.figure(figsize=(19.2, 10.8), facecolor=NAVY, dpi=100)

def save(fig, n, name):
    path = f'{OUT}/slide_{n:02d}_{name}.jpg'
    fig.savefig(path, bbox_inches='tight', pad_inches=0, facecolor=NAVY, dpi=100)
    plt.close(fig)
    print(f'  {path}')
    return path

def header(fig, title, subtitle='', page=1, total=10):
    ax = fig.add_axes([0,0.88,1,0.12], facecolor=NAVY_L)
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0),0.015,1, color=TEAL))
    ax.text(0.025,0.62, title, fontsize=22, color=WHITE, fontweight='bold', va='center')
    ax.text(0.025,0.22, subtitle, fontsize=11, color=GREY_L, fontstyle='italic', va='center')
    ax.text(0.99,0.5, f'STATKRAFT · CONFIDENTIAL  |  {page}/{total}',
            fontsize=9, color=GREY_M, ha='right', va='center')

def footer(fig):
    ax = fig.add_axes([0,0,1,0.035], facecolor=NAVY_L)
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.text(0.015,0.5,'Peru BOS Market Analysis — Rev 1b · Statkraft Procurement · February 2026',
            fontsize=8.5, color=GREY_M, va='center')

def supplier_card(fig, pos, name, tier, metric, note, col, recent=''):
    ax = fig.add_axes(pos, facecolor=NAVY_L)
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0.94),1,0.06, color=col))
    ax.text(0.5,0.97, tier, ha='center', va='center', fontsize=8, color=NAVY, fontweight='bold')
    ax.text(0.5,0.81, name, ha='center', va='center', fontsize=13, color=WHITE, fontweight='bold', multialignment='center')
    ax.text(0.5,0.65, metric, ha='center', va='center', fontsize=18, color=col, fontweight='bold', multialignment='center')
    ax.text(0.5,0.46, note,  ha='center', va='center', fontsize=8.5, color=GREY_L, multialignment='center')
    if recent:
        ax.add_patch(plt.Rectangle((0.04,0.04),0.92,0.22, color='#0D1B2A'))
        ax.text(0.5,0.22,'Peru reference:', ha='center', fontsize=7.5, color=col, fontweight='bold')
        ax.text(0.5,0.11, recent, ha='center', fontsize=7.5, color=WHITE, multialignment='center')

def hbar_simple(ax, labels, values, colors, max_val=110):
    ax.set_facecolor(NAVY_L)
    ax.spines[:].set_visible(False)
    ax.tick_params(colors=GREY_L, labelsize=9)
    ax.xaxis.set_visible(False)
    y = range(len(labels))
    bars = ax.barh(list(y), values, color=colors, height=0.6, edgecolor='none')
    ax.set_xlim(0, max_val)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, color=WHITE, fontsize=9)
    for bar, val in zip(bars, values):
        ax.text(bar.get_width()+1, bar.get_y()+bar.get_height()/2,
                f'{val}%', va='center', color=GREY_L, fontsize=9)
    ax.invert_yaxis()

# ── SLIDE 1: COVER ────────────────────────────────────────────────────────────
fig = new_fig()
ax = fig.add_axes([0,0,1,1], facecolor=NAVY); ax.axis('off')
ax.add_patch(plt.Rectangle((0,0),0.025,1, color=TEAL))
ax.add_patch(plt.Rectangle((0.025,0.52),0.975,0.004, color=TEAL))
ax.add_patch(plt.Rectangle((0.025,0.38),0.975,0.003, color=AMBER))
ax.text(0.05,0.76,'PERU RENEWABLE ENERGY — BOS MARKET ANALYSIS',
        fontsize=14, color=TEAL, fontweight='bold')
ax.text(0.05,0.58,'Balance of System\nSupplier Intelligence',
        fontsize=52, color=WHITE, fontweight='bold', linespacing=1.1)
ax.text(0.05,0.44,'Trackers · Cabling · Transformers · Civil Works · Grid Connection · SCADA',
        fontsize=15, color=GREY_L, fontstyle='italic')
ax.text(0.05,0.33,'Rev 1b — BOS Focus Edition  ·  Statkraft Procurement International  ·  February 2026',
        fontsize=13, color=AMBER, fontweight='bold')
ax.text(0.05,0.26,'Prepared by: Aiden  ·  For: Jonathon Milne, VP Procurement International',
        fontsize=12, color=GREY_L)
save(fig, 1, 'cover')

# ── SLIDE 2: MARKET CONTEXT ───────────────────────────────────────────────────
fig = new_fig()
header(fig,'Peru Market Context','Pipeline scale, regional breakdown & development status',2,10)
footer(fig)

kpis=[('20,000+\nMW','Total development\npipeline (solar+wind)',TEAL),
      ('938 MW','Solar operational\ntoday (2025)',AMBER),
      ('2,362 MW','Solar target\nby end-2026',GREEN),
      ('19 / 114','Projects with\nfinal MINEM concession',RED),
      ('$700–900/kW','All-in solar CAPEX\n(utility-scale Peru)',TEAL)]
for i,(val,lbl,col) in enumerate(kpis):
    ax=fig.add_axes([0.02+i*0.196,0.62,0.175,0.25],facecolor=NAVY_L)
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.93),1,0.07,color=col))
    ax.text(0.5,0.60,val,ha='center',va='center',fontsize=20,color=col,fontweight='bold',multialignment='center')
    ax.text(0.5,0.20,lbl,ha='center',va='center',fontsize=9,color=GREY_L,multialignment='center')

ax_bar=fig.add_axes([0.03,0.09,0.44,0.49],facecolor=NAVY_L)
scenarios=['2025\n(Now)','Base 2026','Base 2027','Base 2028','Full\nPotential 2030']
solar=[938,2362,3242,3337,15185]; wind=[1021,1021,1867,1867,9344]
x=np.arange(len(scenarios)); w=0.35
b1=ax_bar.bar(x-w/2,solar,w,color=AMBER,label='Solar PV',edgecolor='none')
b2=ax_bar.bar(x+w/2,wind,w,color=TEAL,label='Wind',edgecolor='none')
ax_bar.set_facecolor(NAVY_L); ax_bar.spines[:].set_visible(False)
ax_bar.set_xticks(x); ax_bar.set_xticklabels(scenarios,color=GREY_L,fontsize=9)
ax_bar.tick_params(colors=GREY_M)
ax_bar.set_ylabel('Installed Capacity (MW)',color=GREY_L,fontsize=9)
ax_bar.set_title('Capacity Trajectory — Base Case vs Full Pipeline',color=TEAL,fontsize=10,fontweight='bold')
ax_bar.legend(facecolor=NAVY,edgecolor='none',labelcolor=WHITE,fontsize=9)
for b in list(b1)+list(b2):
    h=b.get_height()
    if h>1500:
        ax_bar.text(b.get_x()+b.get_width()/2,h+150,f'{h:,.0f}',ha='center',color=WHITE,fontsize=7)

ax_r=fig.add_axes([0.50,0.09,0.48,0.49],facecolor=NAVY_L)
ax_r.axis('off'); ax_r.set_xlim(0,1); ax_r.set_ylim(0,1)
ax_r.add_patch(plt.Rectangle((0,0.90),1,0.10,color=TEAL))
ax_r.text(0.5,0.95,'KEY DEVELOPMENT REGIONS & RECENT PROJECTS',ha='center',va='center',fontsize=10,color=NAVY,fontweight='bold')
regions=[(AMBER,'ICA','Solar+Wind','Villacuri 470MW · San Pedro 1,800MW pipeline\nWayra 72MW solar · Ica wind (500MW Inkia)'),
         (TEAL,'PIURA','Wind Hub','Bayóvar Wind Farm — $1.056B investment\nStrongest wind resource in Peru'),
         (GREEN,'AREQUIPA','Solar Prime','La Joya 225MW (ACCIONA 2024) · Clemesí 204MW\nAttacama fringe — GHI >6.5 kWh/m²/day'),
         (PURPLE,'LAMBAYEQUE','Wind','Mórrope Wind Farm — $353M investment'),
         (GREY_M,'MOQUEGUA','Solar','Sunny Solar 204MW → 309MW (Kallpa, 2026)')]
y=0.83
for col,region,tech,projects in regions:
    ax_r.add_patch(plt.Rectangle((0.01,y-0.14),0.98,0.155,color='#0D1B2A'))
    ax_r.add_patch(plt.Rectangle((0.01,y-0.14),0.04,0.155,color=col))
    ax_r.text(0.065,y-0.03,region,fontsize=10,color=col,fontweight='bold',va='center')
    ax_r.text(0.30,y-0.03,f'[{tech}]',fontsize=8.5,color=GREY_L,va='center')
    for i,line in enumerate(projects.split('\n')[:2]):
        ax_r.text(0.065,y-0.075-i*0.038,line,fontsize=8,color=WHITE,va='center')
    y-=0.175
save(fig,2,'market_context')

# ── SLIDE 3: TRACKERS & MOUNTING ─────────────────────────────────────────────
fig = new_fig()
header(fig,'BOS: Trackers & Mounting Structures','Single-axis tracker market — Nextracker leads globally & in LatAm',3,10)
footer(fig)

ax1=fig.add_axes([0.02,0.10,0.34,0.75],facecolor=NAVY)
tr_sizes=[38,18,10,8,8,18]; tr_colors=[TEAL,AMBER,GREEN,PURPLE,ORANGE,GREY_M]
ax1.set_facecolor(NAVY)
w1,_=ax1.pie(tr_sizes,colors=tr_colors,startangle=90,
             wedgeprops=dict(width=0.52,edgecolor=NAVY,linewidth=2))
ax1.text(0,0,'Single-Axis\nTracker\nMarket\n2025',ha='center',va='center',
         fontsize=9,color=WHITE,fontweight='bold',multialignment='center')
ax1.set_title('Global Solar Tracker Market Share',color=TEAL,fontsize=11,fontweight='bold')
labels_tr=['Nextracker ~38%','Array Tech ~18%','Soltec ~10%','Arctech ~8%','PVHardware ~8%','Others ~18%']
ax1.legend(w1,labels_tr,loc='lower center',bbox_to_anchor=(0.5,-0.16),
           ncol=2,facecolor=NAVY_L,edgecolor='none',labelcolor=WHITE,fontsize=9)

tr_cards=[
    ('Nextracker','★ GLOBAL #1','~38%\nglobal share','Strongest LatAm footprint\nAI-enabled TrueCapture yield opt.\nAcquired robotics co. (2025)',
     TEAL,'Active Ica & Arequipa corridors\nPreferred tracker in Peru'),
    ('Array Tech','★ STRONG #2','~18%\nglobal share','US-listed, Mexico mfg base\nOmniTrack dual-row system\nCompetitive on large flat sites',
     AMBER,'Growing Peru presence\nSan Pedro pipeline'),
    ('Soltec','LATAM FOCUS','~10%\nglobal share','Spanish, strong LatAm network\nSF7 bifacial-optimised\nGood local support & references',
     GREEN,'Installed on Ica corridor projects\nSolid Peru track record'),
    ('Fixed-Tilt\n(Local Steel)','COST OPTION','15–20%\ncheaper','Local fabricators Arequipa/Lima\nSuitable flat terrain <50MW\nNo yield optimisation benefit',
     GREY_M,'Used on smaller <50MW\nand high-altitude projects'),
]
pos_tr=[[0.39,0.53,0.145,0.42],[0.545,0.53,0.145,0.42],
        [0.39,0.08,0.145,0.42],[0.545,0.08,0.145,0.42]]
for (name,tier,pct,note,col,recent),pos in zip(tr_cards,pos_tr):
    supplier_card(fig,pos,name,tier,pct,note,col,recent)

ax_r=fig.add_axes([0.71,0.08,0.28,0.87],facecolor=NAVY_L)
ax_r.axis('off'); ax_r.set_xlim(0,1); ax_r.set_ylim(0,1)
ax_r.add_patch(plt.Rectangle((0,0.97),1,0.03,color=GREEN))
ax_r.text(0.5,0.90,'TRACKER vs.\nFIXED TILT\n(Peru)',ha='center',fontsize=11,color=GREEN,fontweight='bold',multialignment='center')
for val,lbl,col,y in [('+8–12%','Yield gain\nwith tracker',TEAL,0.76),
                      ('+$60–80\n/kW','Cost premium\nvs fixed-tilt',AMBER,0.58),
                      ('4–5 yr','Payback on\ntracker premium',GREEN,0.40)]:
    ax_r.text(0.5,y,val,ha='center',fontsize=18,color=col,fontweight='bold',multialignment='center')
    ax_r.text(0.5,y-0.09,lbl,ha='center',fontsize=8,color=GREY_L,multialignment='center')
ax_r.add_patch(plt.Rectangle((0.04,0.04),0.92,0.24,color='#0D1B2A'))
ax_r.text(0.5,0.24,'RECOMMENDATION',ha='center',fontsize=8.5,color=GREEN,fontweight='bold')
ax_r.text(0.5,0.13,'Tracker justified on flat sites\n>50MW (Ica, Arequipa).\nNextracker default;\nSoltec for competition.',
          ha='center',fontsize=7.5,color=GREY_L,multialignment='center')
save(fig,3,'trackers')

# ── SLIDE 4: CABLING & ELECTRICAL ────────────────────────────────────────────
fig = new_fig()
header(fig,'BOS: Cabling & Electrical Infrastructure','DC collection, AC distribution & HV connection supply landscape',4,10)
footer(fig)

cable_cards=[
    ('Indeco\n(Nexans Group)','★ LOCAL LEADER','Peru mfg. base','DC cables, LV/MV distribution\nHV cable up to 220kV\nFastest delivery in Peru',
     TEAL,'Active across all major\nPeru solar projects'),
    ('CEP\n(Conductores Elec. Peruanos)','LOCAL #2','Peru mfg. base','DC & AC power cables\nCompetitive on bulk volumes\nGood for LV/MV scope',
     AMBER,'Multiple Ica corridor\nprojects, BOP civil scope'),
    ('Phelps Dodge\n/ Belden','IMPORT SPECIALIST','USA/Global','HV specialist cables\nDC tray cable, medium voltage\nPremium quality / ESG credentials',
     GREEN,'Used on IFC-financed\nprojects in Peru'),
    ('NKT / Nexans\n(Direct Import)','HV SPECIALIST','Europe','Extra high voltage (EHV)\n220kV+ transmission cables\nLong lead time: 6–10 months',
     PURPLE,'HV grid connection\nscope on large projects'),
]
pos_cables=[[0.02,0.50,0.19,0.45],[0.22,0.50,0.19,0.45],
            [0.42,0.50,0.19,0.45],[0.62,0.50,0.19,0.45]]
for (name,tier,origin,note,col,recent),pos in zip(cable_cards,pos_cables):
    supplier_card(fig,pos,name,tier,origin,note,col,recent)

# Cable split donut
ax_d=fig.add_axes([0.03,0.07,0.28,0.40],facecolor=NAVY)
ax_d.set_facecolor(NAVY)
c_sizes=[45,30,15,10]
c_colors=[TEAL,AMBER,GREEN,GREY_M]
w,_=ax_d.pie(c_sizes,colors=c_colors,startangle=90,wedgeprops=dict(width=0.52,edgecolor=NAVY,linewidth=2))
ax_d.text(0,0,'Cable\nOrigin\nMix',ha='center',va='center',fontsize=9,color=WHITE,fontweight='bold',multialignment='center')
ax_d.set_title('Cable Supply Origin (Peru)',color=TEAL,fontsize=10,fontweight='bold')
ax_d.legend(w,['Local MV/LV 45%','China import 30%','Europe HV 15%','USA 10%'],
            loc='lower center',bbox_to_anchor=(0.5,-0.22),ncol=2,
            facecolor=NAVY_L,edgecolor='none',labelcolor=WHITE,fontsize=8.5)

# Procurement guidance
ax_g=fig.add_axes([0.34,0.07,0.46,0.40],facecolor=NAVY_L)
ax_g.axis('off'); ax_g.set_xlim(0,1); ax_g.set_ylim(0,1)
ax_g.add_patch(plt.Rectangle((0,0.92),1,0.08,color=TEAL))
ax_g.text(0.5,0.96,'CABLE PROCUREMENT STRATEGY',ha='center',va='center',fontsize=11,color=NAVY,fontweight='bold')
tips=[('DC Collection (string to combiner)',   'Local (Indeco/CEP) — good quality, fastest delivery, ~40% cheaper than import'),
      ('AC Distribution (inverter to trafo)',   'Local or import — Indeco capable; use import for larger cross-sections (>300mm²)'),
      ('MV Collection (combiner to substation)','Dual-source: Indeco for standard + Phelps Dodge for IFC-financed scope'),
      ('HV Grid Connection (132kV+)',            'Import only — NKT or Nexans. 6–10 month lead time. Order at FID or earlier.'),
      ('Cable Trays & Conduit',                  '100% local supply — use Peruvian fabricators; no reason to import'),]
y=0.82
for scope,strategy in tips:
    ax_g.add_patch(plt.Rectangle((0.01,y-0.12),0.98,0.13,color='#0D1B2A'))
    ax_g.text(0.03,y-0.03,scope,fontsize=9,color=TEAL,fontweight='bold',va='center')
    ax_g.text(0.03,y-0.09,strategy,fontsize=8.5,color=GREY_L,va='center')
    y-=0.158

# Lead time callout
ax_lt=fig.add_axes([0.82,0.07,0.17,0.40],facecolor=NAVY_L)
ax_lt.axis('off'); ax_lt.set_xlim(0,1); ax_lt.set_ylim(0,1)
ax_lt.add_patch(plt.Rectangle((0,0.92),1,0.08,color=AMBER))
ax_lt.text(0.5,0.96,'LEAD TIMES',ha='center',va='center',fontsize=10,color=NAVY,fontweight='bold')
for lt_label,lt_val,col,y in [('DC Cable','2–4 wks',GREEN,0.78),
                               ('AC/MV Cable','4–8 wks',AMBER,0.61),
                               ('HV 132kV+','6–10 mths',RED,0.44),
                               ('EHV 220kV+','10–14 mths',RED,0.27)]:
    ax_lt.text(0.5,y,lt_label,ha='center',fontsize=9,color=WHITE,fontweight='bold')
    ax_lt.text(0.5,y-0.09,lt_val,ha='center',fontsize=14,color=col,fontweight='bold')
save(fig,4,'cabling')

# ── SLIDE 5: TRANSFORMERS & HV EQUIPMENT ─────────────────────────────────────
fig = new_fig()
header(fig,'BOS: Transformers, Switchgear & HV Equipment','Critical long-lead items — global shortage & strategic procurement',5,10)
footer(fig)

hv_cards=[
    ('ABB / Hitachi Energy','★ BENCHMARK','Global #1/2','Preferred by European developers\nIEC & IEEE certified\nFullest product range MV–EHV',
     TEAL,'Substation scope Kallpa projects\nKEY reference for Statkraft'),
    ('Siemens Energy','★ STRONG #2','Global #2/3','SIEMENS NXAIR/NXPLUS GIS\nStrong on digital substation\nPremium price, excellent reliability',
     AMBER,'Active Peru energy sector\nMultiple substation references'),
    ('Schneider Electric','LOCAL PRESENCE','France/Global','Local Schneider office in Lima\nMV switchgear (Premset, SM6)\nFastest local response time',
     GREEN,'Distribution switchgear\nacross Peru solar portfolio'),
    ('CHINT / TBEA','COST OPTION','China','30–40% lower capex vs ABB\nGrowing LatAm track record\nESG/FEOC scrutiny applies',
     RED,'Used on Chinese-financed\nprojects in LatAm'),
]
pos_hv=[[0.02,0.50,0.21,0.45],[0.24,0.50,0.21,0.45],
        [0.46,0.50,0.21,0.45],[0.68,0.50,0.21,0.45]]
for (name,tier,origin,note,col,recent),pos in zip(hv_cards,pos_hv):
    supplier_card(fig,pos,name,tier,origin,note,col,recent)

# Import dependency for this category
ax_dep=fig.add_axes([0.02,0.07,0.30,0.40],facecolor=NAVY_L)
items=['MV/HV Transformers','GIS Switchgear','HV Circuit Breakers','MV Switchgear','Protection Relays','SCADA/Control Systems']
pcts=[70,80,85,65,90,90]
cols=[RED if p>=80 else AMBER if p>=60 else GREEN for p in pcts]
hbar_simple(ax_dep,items,pcts,cols)
ax_dep.set_title('Import Dependency (% of value)',color=TEAL,fontsize=10,fontweight='bold')

# Critical warning box
ax_w=fig.add_axes([0.35,0.07,0.32,0.40],facecolor=NAVY_L)
ax_w.axis('off'); ax_w.set_xlim(0,1); ax_w.set_ylim(0,1)
ax_w.add_patch(plt.Rectangle((0,0.92),1,0.08,color=RED))
ax_w.text(0.5,0.96,'GLOBAL SHORTAGE\nALERT',ha='center',va='center',fontsize=11,color=WHITE,fontweight='bold',multialignment='center')
shortage_pts=[
    ('10–14 months','HV Transformer lead time',RED),
    ('6–10 months','GIS Switchgear lead time',AMBER),
    ('Global demand up\n40% since 2022','Grid electrification\ndriving shortage',AMBER),
    ('Order at FID\nor earlier','Critical path risk\nif delayed',RED),
]
y=0.82
for val,lbl,col in shortage_pts:
    ax_w.text(0.5,y,val,ha='center',fontsize=13,color=col,fontweight='bold',multialignment='center')
    ax_w.text(0.5,y-0.10,lbl,ha='center',fontsize=8,color=GREY_L,multialignment='center')
    y-=0.21

# Strategy box
ax_s=fig.add_axes([0.69,0.07,0.30,0.40],facecolor=NAVY_L)
ax_s.axis('off'); ax_s.set_xlim(0,1); ax_s.set_ylim(0,1)
ax_s.add_patch(plt.Rectangle((0,0.92),1,0.08,color=TEAL))
ax_s.text(0.5,0.96,'PROCUREMENT\nSTRATEGY',ha='center',va='center',fontsize=11,color=NAVY,fontweight='bold',multialignment='center')
strat=[('1.','Frame agreements NOW\nwith ABB & Siemens\nbefore pipeline unlocks'),
       ('2.','Dual-source all\ntransformer packages\n(never sole-source)'),
       ('3.','CHINT/TBEA only\nfor non-IFC-financed\nand cost-critical scope'),
       ('4.','Schneider for MV\ndistribution — fastest\nlocal support in Peru'),]
y=0.84
for num,txt in strat:
    ax_s.add_patch(plt.Rectangle((0.03,y-0.14),0.94,0.155,color='#0D1B2A'))
    ax_s.text(0.08,y-0.055,num,fontsize=12,color=TEAL,fontweight='bold',va='center')
    ax_s.text(0.20,y-0.055,txt,fontsize=8.5,color=WHITE,va='center')
    y-=0.185
save(fig,5,'transformers_hv')

# ── SLIDE 6: EPC CONTRACTORS ──────────────────────────────────────────────────
fig = new_fig()
header(fig,'EPC & BOS Contractors — Peru Experience','Who has built what — recent project track record & strategic fit',6,10)
footer(fig)

contractors=[
    ('ACCIONA','International EPC','Spain',TEAL,'★ MOST RECENT AWARD',
     '225MW La Joya, Arequipa\n(Kallpa Generación, Nov 2024)',
     'Full turnkey EPC. European procurement standards. Arequipa specialist. Best for >100MW.',
     [0.02,0.50,0.23,0.45]),
    ('Grenergy','Developer/EPC','Spain',AMBER,'ACTIVE IN PERU',
     'Matarani 97MW EPC\n(Yinson Renewables, 2024)',
     'Developer with own EPC arm. Deep Peru market knowledge. Good for sub-200MW.',
     [0.26,0.50,0.23,0.45]),
    ('Cosapi','Local Civil/BOP','Peru',GREEN,'★ TOP LOCAL CIVIL',
     'Cupisnique wind (civil/BOP)\nTalara wind farm + solar civil scopes',
     "Peru's largest civil contractor. Deep local relationships. Essential for BOP civil scope.",
     [0.50,0.50,0.23,0.45]),
    ('JJC Contratistas','Local Civil','Peru',PURPLE,'ESTABLISHED LOCAL',
     'Solar civil works (Ica region)\nRoad & access for wind projects',
     'Earthworks, foundations, access roads. Best for competitive tension vs Cosapi.',
     [0.74,0.50,0.23,0.45]),
    ('Mota-Engil','International Civil','Portugal',ORANGE,'REGIONAL OPTION',
     'Peru infra (roads, civil)\nEnergy sector entry 2024–25',
     'Portuguese group with LatAm footprint. Good #3 option for civil competition.',
     [0.02,0.05,0.23,0.42]),
    ('Sacyr','Spanish EPC','Spain',CYAN,'REGIONAL EPC',
     'LatAm energy projects\n(Chile, Colombia references)',
     'Strong civil EPC capability. Chile model transferable to Peru.',
     [0.26,0.05,0.23,0.42]),
    ('Graña y Montero','Local Industrial','Peru',RED,'EMERGING ENERGY',
     'Mining civil works\nEnergy sector entry (Ica 2024)',
     "Peru's largest industrial contractor. Heavy civil capability. Newer to renewables.",
     [0.50,0.05,0.23,0.42]),
]
for (name,ctype,origin,col,tier,projects,strength,pos) in contractors:
    ax=fig.add_axes(pos,facecolor=NAVY_L)
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.95),1,0.05,color=col))
    ax.text(0.5,0.975,tier,ha='center',va='center',fontsize=7.5,color=NAVY,fontweight='bold')
    ax.text(0.5,0.87,name,ha='center',va='center',fontsize=13,color=WHITE,fontweight='bold',multialignment='center')
    ax.text(0.5,0.79,f'{ctype} · {origin}',ha='center',fontsize=8,color=GREY_L)
    ax.add_patch(plt.Rectangle((0.03,0.55),0.94,0.22,color='#0D1B2A'))
    ax.text(0.5,0.68,'RECENT PROJECTS',ha='center',fontsize=7.5,color=col,fontweight='bold')
    for i,line in enumerate(projects.split('\n')[:2]):
        ax.text(0.5,0.61-i*0.08,line,ha='center',fontsize=7.5,color=WHITE,multialignment='center')
    ax.text(0.5,0.35,strength,ha='center',fontsize=8,color=GREY_L,multialignment='center')

ax_tip=fig.add_axes([0.74,0.05,0.25,0.42],facecolor=NAVY_L)
ax_tip.axis('off'); ax_tip.set_xlim(0,1); ax_tip.set_ylim(0,1)
ax_tip.add_patch(plt.Rectangle((0,0.96),1,0.04,color=AMBER))
ax_tip.text(0.5,0.88,'STRATEGIC\nACTIONS',ha='center',fontsize=11,color=AMBER,fontweight='bold',multialignment='center')
tips_c=[('1.','Pre-qualify Cosapi & JJC NOW\nbefore pipeline unlocks'),
        ('2.','ACCIONA — go-to full EPC >100MW'),
        ('3.','Grenergy for 50–200MW\n(deep Peru knowledge)'),
        ('4.','Always dual-source civil:\nCosapi + one other'),
        ('5.','Mota-Engil as #3 option\nfor competitive tension')]
y=0.76
for num,tip in tips_c:
    ax_tip.text(0.06,y,num,fontsize=10,color=AMBER,fontweight='bold',va='top')
    ax_tip.text(0.18,y,tip,fontsize=8,color=GREY_L,va='top')
    y-=0.155
save(fig,6,'epc_contractors')

# ── SLIDE 7: SUPPLY CHAIN ORIGIN ─────────────────────────────────────────────
fig = new_fig()
header(fig,'BOS Supply Chain Origin','Import dependency by component & equipment origin mix',7,10)
footer(fig)

ax_main=fig.add_axes([0.03,0.10,0.56,0.80],facecolor=NAVY_L)
items=['SCADA/Control Systems','HV Circuit Breakers','Protection Relays',
       'GIS Switchgear','MV/HV Transformers','Tracker Systems',
       'MV Switchgear','HV Cabling (132kV+)',
       'MV Collection Cables','DC/AC Distribution Cables',
       'Civil Works (Foundations)','Concrete & Aggregate']
pcts=[90,85,90,80,70,70,65,60,40,35,12,5]
cols=[RED if p>=75 else AMBER if p>=45 else GREEN for p in pcts]
hbar_simple(ax_main,items,pcts,cols,max_val=110)
ax_main.set_title('BOS Component Import Dependency  (% of value imported)',
                  color=TEAL,fontsize=11,fontweight='bold')
for col,lbl,xp in [(RED,'≥75% — critical import',60),(AMBER,'45–74% — moderate',60),(GREEN,'<45% — local capability',60)]:
    pass

ax_leg=fig.add_axes([0.03,0.06,0.56,0.04],facecolor=NAVY)
ax_leg.axis('off'); ax_leg.set_xlim(0,1); ax_leg.set_ylim(0,1)
for i,(col,lbl) in enumerate([(RED,'≥75%  Critical import risk'),(AMBER,'45–74%  Moderate import'),(GREEN,'<45%  Local capability exists')]):
    ax_leg.add_patch(plt.Rectangle((0.02+i*0.33,0.1),0.03,0.8,color=col))
    ax_leg.text(0.06+i*0.33,0.5,lbl,fontsize=9,color=WHITE,va='center')

# Origin donut
ax_d=fig.add_axes([0.63,0.48,0.34,0.42],facecolor=NAVY)
ax_d.set_facecolor(NAVY)
o_sizes=[72,14,8,6]; o_cols=[TEAL,AMBER,GREEN,PURPLE]
w,_=ax_d.pie(o_sizes,colors=o_cols,startangle=90,wedgeprops=dict(width=0.52,edgecolor=NAVY,linewidth=2))
ax_d.text(0,0,'BOS\nOrigin\nMix',ha='center',va='center',fontsize=9,color=WHITE,fontweight='bold',multialignment='center')
ax_d.set_title('BOS Equipment Origin — Peru',color=TEAL,fontsize=10,fontweight='bold')
ax_d.legend(w,['China 72%','Europe 14%','USA 8%','Local 6%'],
            loc='lower center',bbox_to_anchor=(0.5,-0.20),ncol=2,
            facecolor=NAVY_L,edgecolor='none',labelcolor=WHITE,fontsize=9)

# 3 callout boxes
callouts=[(AMBER,'CUSTOMS ADVANTAGE','Peru FTAs with China, US & EU.\nImport duties 0–6% on RE equipment.\nClearance variance: 30–90 days.\nUse specialist customs broker.'),
          (RED,'TRANSFORMER SHORTAGE','HV transformers: global shortage.\n10–14 month lead time (2025–26).\nOrder at FID minimum.\nFrame now with ABB/Siemens.'),
          (GREEN,'LOCAL OPPORTUNITY','Civil works: 85–90% local.\nCabling: 35–50% local.\nMaximise local content for\ncommunity licence & FX hedge.')]
y_c=0.06
for col,title,body in callouts:
    ax_c=fig.add_axes([0.63,y_c,0.36,0.135],facecolor=NAVY_L)
    ax_c.axis('off'); ax_c.set_xlim(0,1); ax_c.set_ylim(0,1)
    ax_c.add_patch(plt.Rectangle((0,0),0.025,1,color=col))
    ax_c.text(0.04,0.80,title,fontsize=10,color=col,fontweight='bold',va='center')
    for i,line in enumerate(body.split('\n')[:3]):
        ax_c.text(0.04,0.52-i*0.22,line,fontsize=8.5,color=GREY_L,va='center')
    y_c+=0.147
save(fig,7,'supply_chain')

# ── SLIDE 8: RISK MATRIX ─────────────────────────────────────────────────────
fig = new_fig()
header(fig,'BOS Procurement Risk Matrix','Likelihood vs Impact — Peru solar projects',8,10)
footer(fig)

ax=fig.add_axes([0.04,0.09,0.58,0.81],facecolor=NAVY_L)
ax.spines[:].set_visible(False); ax.set_facecolor(NAVY_L)
ax.set_xlim(0,6); ax.set_ylim(0,6)
ax.set_xlabel('LIKELIHOOD →',color=GREY_L,fontsize=10,labelpad=8)
ax.set_ylabel('IMPACT →',color=GREY_L,fontsize=10,labelpad=8)
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(['Very Low','Low','Medium','High','Very High'],color=GREY_L,fontsize=8)
ax.set_yticks([1,2,3,4,5])
ax.set_yticklabels(['Negligible','Minor','Moderate','Major','Critical'],color=GREY_L,fontsize=8)
ax.tick_params(colors=GREY_M)
ax.add_patch(plt.Rectangle((0,0),2.5,2.5,color='#1A3A1A',alpha=0.4))
ax.add_patch(plt.Rectangle((2.5,0),3.5,2.5,color='#3A3A1A',alpha=0.4))
ax.add_patch(plt.Rectangle((0,2.5),2.5,3.5,color='#3A3A1A',alpha=0.4))
ax.add_patch(plt.Rectangle((2.5,2.5),3.5,3.5,color='#3A1A1A',alpha=0.4))
ax.text(1.2,1.2,'LOW\nRISK',ha='center',fontsize=9,color=GREEN,alpha=0.7,fontweight='bold')
ax.text(3.7,1.2,'WATCH',ha='center',fontsize=9,color=AMBER,alpha=0.7,fontweight='bold')
ax.text(1.2,3.7,'WATCH',ha='center',fontsize=9,color=AMBER,alpha=0.7,fontweight='bold')
ax.text(4.0,4.2,'CRITICAL\nRISK ZONE',ha='center',fontsize=9,color=RED,alpha=0.8,fontweight='bold',multialignment='center')

risks_scatter=[(4.5,4.8,'Grid connection\ndelay',RED,'G'),
               (4.2,4.5,'Transformer\nshortage',RED,'T'),
               (4.3,4.0,'MINEM permitting\ndelay',RED,'P'),
               (3.8,3.5,'Civil contractor\ncapacity',AMBER,'C'),
               (3.5,3.8,'PPA unavailability',AMBER,'PPA'),
               (3.0,2.8,'Customs delay',AMBER,'CU'),
               (3.2,2.5,'PEN inflation\n(civil costs)',AMBER,'FX'),
               (1.8,3.5,'FEOC/ESG\nscrutiny',GREEN,'F'),
               (1.5,2.0,'Single-source\ncabling OEM',GREEN,'S')]
for x,y,lbl,col,code in risks_scatter:
    ax.scatter(x,y,s=350,color=col,zorder=5,edgecolors=NAVY,linewidth=1.5)
    ax.text(x,y,'',ha='center',fontsize=7,color=NAVY,fontweight='bold',zorder=6,va='center')
    ax.annotate(f'{code}\n{lbl}',(x,y),xytext=(x+0.3,y+0.35),fontsize=7,color=WHITE,
                arrowprops=dict(arrowstyle='->',color=GREY_M,lw=0.8),multialignment='center')
ax.set_title('BOS Procurement Risk — Likelihood vs Impact',color=TEAL,fontsize=11,fontweight='bold')

ax_leg=fig.add_axes([0.65,0.09,0.34,0.81],facecolor=NAVY_L)
ax_leg.axis('off'); ax_leg.set_xlim(0,1); ax_leg.set_ylim(0,1)
ax_leg.add_patch(plt.Rectangle((0,0.96),1,0.04,color=RED))
ax_leg.text(0.5,0.98,'RISK MITIGATIONS',ha='center',va='center',fontsize=10,color=WHITE,fontweight='bold')
risk_keys=[('G',RED,'Grid connection delay','Owner-procure; 20% contingency'),
           ('T',RED,'Transformer shortage','Frame ABB/Siemens now; order at FID'),
           ('P',RED,'MINEM permitting delay','Gate spend to final concession'),
           ('C',AMBER,'Civil contractor capacity','Pre-qualify Cosapi/JJC immediately'),
           ('PPA',AMBER,'PPA unavailability','NTP-linked procurement structure'),
           ('CU',AMBER,'Customs delay','Specialist broker; buffer lead times'),
           ('FX',AMBER,'PEN inflation','CPI clauses on civil contracts'),
           ('F',GREEN,'FEOC/ESG scrutiny','Xinjiang attestation in pre-qual'),
           ('S',GREEN,'Single-source cabling','Dual-source Indeco + import OEM')]
y=0.89
for code,col,name,mit in risk_keys:
    ax_leg.add_patch(plt.Circle((0.05,y-0.01),0.028,color=col))
    ax_leg.text(0.065,y-0.01,code,ha='center',va='center',fontsize=7,color=NAVY,fontweight='bold')
    ax_leg.text(0.11,y+0.01,name,fontsize=9,color=WHITE,fontweight='bold')
    ax_leg.text(0.11,y-0.04,mit,fontsize=8,color=GREY_L)
    ax_leg.plot([0.02,0.98],[y-0.075,y-0.075],color='#1E3A5F',linewidth=0.4)
    y-=0.098
save(fig,8,'risk_matrix')

# ── SLIDE 9: SCORECARD ────────────────────────────────────────────────────────
fig = new_fig()
header(fig,'BOS Market Scorecard','Peru solar procurement readiness — component by component',9,10)
footer(fig)

scores=[('Tracker/Mounting Supply',    4,TEAL, 'Nextracker & Soltec strong in LatAm; local fixed-tilt option available'),
        ('Cable Supply (LV/MV)',        4,GREEN,'Good local supply (Indeco, CEP); competitive and fast delivery'),
        ('Cable Supply (HV 132kV+)',    2,RED,  'Import-only; 6–10 month lead; global supply constraints'),
        ('Transformer Supply',          2,RED,  'Import-dominant (70%); 10–14 month lead; global shortage 2024–26'),
        ('Switchgear & Protection',     3,AMBER,'ABB/Schneider/Siemens active in Peru; 65–80% import dependent'),
        ('SCADA & Controls',            3,AMBER,'Import-dominant; OEM-integrated preferred; ABB/Siemens most reliable'),
        ('Civil Works Capability',      4,GREEN,'Cosapi/JJC strong; capacity constraint as pipeline accelerates'),
        ('Grid Connection',             2,RED,  'Transmission bottleneck; highest-risk BOS item in Peru'),
        ('Overall Market Growth',       5,GREEN,'20 GW pipeline; 15%+ CAGR; strong government intent'),
        ('Procurement Complexity',      1,RED,  'HIGH: import dependency, global shortages, grid risk, FX, capacity')]

ax_s=fig.add_axes([0.02,0.08,0.62,0.82],facecolor=NAVY_L)
ax_s.axis('off'); ax_s.set_xlim(0,1); ax_s.set_ylim(0,1)
ax_s.add_patch(plt.Rectangle((0,0.96),1,0.04,color=TEAL))
ax_s.text(0.02,0.965,'BOS DIMENSION',fontsize=9,color=NAVY,fontweight='bold',va='center')
ax_s.text(0.65,0.965,'RATING',fontsize=9,color=NAVY,fontweight='bold',va='center',ha='center')
ax_s.text(0.78,0.965,'COMMENTARY',fontsize=9,color=NAVY,fontweight='bold',va='center')
y=0.875
for i,(label,score,col,comment) in enumerate(scores):
    bg='#10223A' if i%2==0 else NAVY_L
    ax_s.add_patch(plt.Rectangle((0,y-0.08),1,0.085,color=bg))
    ax_s.add_patch(plt.Rectangle((0,y-0.08),0.012,0.085,color=col))
    ax_s.text(0.02,y-0.033,label,fontsize=9.5,color=WHITE,fontweight='bold',va='center')
    for d in range(5):
        fc=col if d<score else '#1E3A5F'
        ax_s.add_patch(plt.Rectangle((0.60+d*0.04,y-0.058),0.032,0.048,color=fc))
    ax_s.text(0.82,y-0.033,comment,fontsize=8,color=GREY_L,va='center')
    y-=0.09

ax_v=fig.add_axes([0.67,0.08,0.32,0.82],facecolor=NAVY_L)
ax_v.axis('off'); ax_v.set_xlim(0,1); ax_v.set_ylim(0,1)
ax_v.add_patch(plt.Rectangle((0,0.96),1,0.04,color=TEAL))
ax_v.text(0.5,0.89,'OVERALL\nVERDICT',ha='center',fontsize=16,color=TEAL,fontweight='bold',multialignment='center')
ax_v.text(0.5,0.78,'4/5',ha='center',fontsize=36,color=AMBER,fontweight='bold')
ax_v.text(0.5,0.70,'Strong Opportunity\nHigh Complexity',ha='center',fontsize=12,color=WHITE,fontweight='bold',multialignment='center')
ax_v.add_patch(plt.Rectangle((0.05,0.52),0.90,0.14,color='#0D1B2A'))
ax_v.text(0.5,0.62,'PROCUREMENT WINDOW',ha='center',fontsize=9,color=AMBER,fontweight='bold')
ax_v.text(0.5,0.55,'Act now — before the\n20 GW pipeline unlocks',ha='center',fontsize=9,color=GREY_L,multialignment='center')
actions=[('1','Frame: Nextracker + Soltec',TEAL),
         ('2','Frame: ABB + Siemens (trafo)',AMBER),
         ('3','Pre-qual: Cosapi + JJC',GREEN),
         ('4','Cable: Indeco primary',TEAL),
         ('5','Owner-procure grid; 20% contingency',RED)]
y_a=0.47
for num,txt,col in actions:
    ax_v.add_patch(plt.Rectangle((0.03,y_a-0.02),0.12,0.082,color=col))
    ax_v.text(0.09,y_a+0.022,num,ha='center',va='center',fontsize=13,color=NAVY,fontweight='bold')
    ax_v.text(0.20,y_a+0.025,txt,fontsize=8,color=WHITE,va='center')
    y_a-=0.088
save(fig,9,'scorecard')

# ── SLIDE 10: RECOMMENDATIONS ─────────────────────────────────────────────────
fig = new_fig()
header(fig,'Strategic Procurement Recommendations','Statkraft Peru BOS — Priority Actions for 2026',10,10)
footer(fig)

recs=[(TEAL,'01','Frame Agreements Now: Trackers & Transformers',
       'Nextracker (trackers) and Array Tech for competitive tension — strong LatAm coverage.\nABB and Siemens Energy for HV transformers — 10–14 month lead, global shortage.\nTarget signed frame agreements BEFORE MINEM pipeline unlocks (est. mid-2026).','Q1 2026'),
      (AMBER,'02','Pre-Qualify Civil Contractors Immediately',
       'Cosapi and JJC are Peru\'s go-to BOP civil contractors — capacity will be absorbed fast.\nACCIONA (full EPC >100MW) and Grenergy (50–200MW) for international EPC scope.\nConsider early works contracts / LOIs to secure scheduling priority.','Q1–Q2 2026'),
      (GREEN,'03','Establish Local Cable Supply Chain',
       'Indeco (Nexans) and CEP are strong for DC/MV/LV cables — local manufacturing advantage.\nDual-source for DC collection; use import (Phelps Dodge / NKT) for HV 132kV+ scope.\nLock MV cable volume with Indeco early — pricing leverage before demand surge.','Q2 2026'),
      (TEAL,'04','Owner-Procure Grid Connection',
       'Grid connection is highest-risk BOS item in Peru. Never wrap in EPC package.\nEngage REP/ISA/COES directly. Budget 15–20% contingency on grid cost estimates.\nVaribility: $30/kW (near existing lines) to $150+/kW (remote sites).','Immediate'),
      (RED,'05','Gate Procurement Spend to MINEM Concession',
       'Do not commit procurement spend before final MINEM concession is confirmed.\nStructure NTP-linked procurement — warm supplier relationships without financial commitment.\n95 of 114 projects still pending concession — procurement at risk if project stalls.','Standing policy'),
      (AMBER,'06','Build Dual-Source Across All BOS Categories',
       'Trackers: Nextracker + Soltec  ·  Transformers: ABB + Siemens  ·  Cables: Indeco + import HV\nCivil: Cosapi + JJC  ·  SCADA: OEM-integrated (avoid third-party separation)\nCompetitive tension in a capacity-constrained market requires early dual-source commitment.','All projects')]

pos_recs=[[0.02,0.53,0.47,0.41],[0.51,0.53,0.47,0.41],
          [0.02,0.10,0.47,0.41],[0.51,0.10,0.47,0.41]]
for i,(col,num,title,body,timing) in enumerate(recs[:4]):
    ax=fig.add_axes(pos_recs[i],facecolor=NAVY_L)
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0),0.012,1,color=col))
    ax.add_patch(plt.Rectangle((0.015,0.76),0.10,0.21,color=col))
    ax.text(0.065,0.865,num,ha='center',va='center',fontsize=22,color=NAVY,fontweight='bold')
    ax.text(0.14,0.89,title,fontsize=11,color=col,fontweight='bold',va='center')
    ax.text(0.14,0.73,f'Timing: {timing}',fontsize=8,color=AMBER,va='center')
    for j,line in enumerate(body.split('\n')[:3]):
        ax.text(0.025,0.58-j*0.17,'→ '+line.strip(),fontsize=8.5,color=GREY_L,va='top')

for i,(col,num,title,body,timing) in enumerate(recs[4:]):
    ax=fig.add_axes([0.02+i*0.49,0.02,0.47,0.07],facecolor=NAVY_L)
    ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0),0.005,1,color=col))
    ax.text(0.015,0.72,f'{num}: {title}',fontsize=9,color=col,fontweight='bold',va='center')
    ax.text(0.015,0.25,body.split('\n')[0],fontsize=8,color=GREY_L,va='center')

save(fig,10,'recommendations')

print('\nRev 1b complete — 10 slides. True BOS focus.')
print(f'Output: {OUT}')
