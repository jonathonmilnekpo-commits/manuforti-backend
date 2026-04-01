"""
Peru BOS Market Analysis — Rev 2
- Trackers removed (along with modules & inverters)
- New: BOS Market Players slide (CJR, Elecnor, Cobra, COMSA, ISA/REP)
- Scorecard: pure BOS components only
BOS scope: Cabling · Transformers & HV · Civil Works · Grid Connection · SCADA
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os

OUT = '/tmp/peru_rev2'
os.makedirs(OUT, exist_ok=True)

NAVY='#0D1B2A'; NAVY_L='#162A44'; TEAL='#00B4D8'
AMBER='#F5A623'; GREEN='#2ECC71'; RED='#E74C3C'
WHITE='#FFFFFF'; GREY_L='#B0BEC5'; GREY_M='#546E7A'
PURPLE='#9B59B6'; ORANGE='#E67E22'; CYAN='#1ABC9C'

def new_fig(): return plt.figure(figsize=(19.2,10.8),facecolor=NAVY,dpi=100)

def save(fig,n,name):
    p=f'{OUT}/slide_{n:02d}_{name}.jpg'
    fig.savefig(p,bbox_inches='tight',pad_inches=0,facecolor=NAVY,dpi=100)
    plt.close(fig); print(f'  {p}'); return p

def hdr(fig,title,sub='',page=1,total=10):
    ax=fig.add_axes([0,0.88,1,0.12],facecolor=NAVY_L)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0),0.015,1,color=TEAL))
    ax.text(0.025,0.62,title,fontsize=22,color=WHITE,fontweight='bold',va='center')
    ax.text(0.025,0.22,sub,fontsize=11,color=GREY_L,fontstyle='italic',va='center')
    ax.text(0.99,0.5,f'STATKRAFT · CONFIDENTIAL  |  {page}/{total}',fontsize=9,color=GREY_M,ha='right',va='center')

def ftr(fig):
    ax=fig.add_axes([0,0,1,0.035],facecolor=NAVY_L)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.text(0.015,0.5,'Peru BOS Market Analysis — Rev 2 · Statkraft Procurement · February 2026',fontsize=8.5,color=GREY_M,va='center')

def card(fig,pos,name,tier,metric,note,col,sub=''):
    ax=fig.add_axes(pos,facecolor=NAVY_L)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0.94),1,0.06,color=col))
    ax.text(0.5,0.97,tier,ha='center',va='center',fontsize=8,color=NAVY,fontweight='bold')
    ax.text(0.5,0.82,name,ha='center',va='center',fontsize=12,color=WHITE,fontweight='bold',multialignment='center')
    ax.text(0.5,0.66,metric,ha='center',va='center',fontsize=17,color=col,fontweight='bold',multialignment='center')
    ax.text(0.5,0.46,note,ha='center',va='center',fontsize=8.5,color=GREY_L,multialignment='center')
    if sub:
        ax.add_patch(plt.Rectangle((0.04,0.04),0.92,0.22,color='#0D1B2A'))
        ax.text(0.5,0.22,'Peru/LatAm ref:',ha='center',fontsize=7.5,color=col,fontweight='bold')
        ax.text(0.5,0.11,sub,ha='center',fontsize=7.5,color=WHITE,multialignment='center')

def hbar(ax,labels,values,colors,max_val=110,title=''):
    ax.set_facecolor(NAVY_L);ax.spines[:].set_visible(False)
    ax.tick_params(colors=GREY_L,labelsize=9);ax.xaxis.set_visible(False)
    y=range(len(labels))
    bars=ax.barh(list(y),values,color=colors,height=0.6,edgecolor='none')
    ax.set_xlim(0,max_val);ax.set_yticks(list(y));ax.set_yticklabels(labels,color=WHITE,fontsize=9)
    for b,v in zip(bars,values):
        ax.text(b.get_width()+1,b.get_y()+b.get_height()/2,f'{v}%',va='center',color=GREY_L,fontsize=9)
    ax.invert_yaxis()
    if title: ax.set_title(title,color=TEAL,fontsize=10,fontweight='bold')

# ═══ SLIDE 1 COVER ════════════════════════════════════════════════════════════
fig=new_fig()
ax=fig.add_axes([0,0,1,1],facecolor=NAVY);ax.axis('off')
ax.add_patch(plt.Rectangle((0,0),0.025,1,color=TEAL))
ax.add_patch(plt.Rectangle((0.025,0.52),0.975,0.004,color=TEAL))
ax.add_patch(plt.Rectangle((0.025,0.38),0.975,0.003,color=AMBER))
ax.text(0.05,0.76,'PERU RENEWABLE ENERGY — BOS MARKET ANALYSIS',fontsize=14,color=TEAL,fontweight='bold')
ax.text(0.05,0.58,'Balance of System\nSupplier Intelligence',fontsize=52,color=WHITE,fontweight='bold',linespacing=1.1)
ax.text(0.05,0.44,'Cabling · Transformers & HV · Civil Works · Grid Connection · SCADA',fontsize=15,color=GREY_L,fontstyle='italic')
ax.text(0.05,0.33,'Rev 2  ·  Statkraft Procurement International  ·  February 2026',fontsize=13,color=AMBER,fontweight='bold')
ax.text(0.05,0.26,'Prepared by: Aiden  ·  For: Jonathon Milne, VP Procurement International',fontsize=12,color=GREY_L)
save(fig,1,'cover')

# ═══ SLIDE 2 MARKET CONTEXT ═══════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'Peru Market Context','Pipeline scale, regional breakdown & development status',2,10)
ftr(fig)
kpis=[('20,000+\nMW','Total development\npipeline (solar+wind)',TEAL),
      ('938 MW','Solar operational\ntoday (2025)',AMBER),
      ('2,362 MW','Solar target\nby end-2026',GREEN),
      ('19 / 114','Projects with\nfinal MINEM concession',RED),
      ('$700–900/kW','All-in solar CAPEX\n(utility-scale Peru)',TEAL)]
for i,(v,l,c) in enumerate(kpis):
    ax=fig.add_axes([0.02+i*0.196,0.62,0.175,0.25],facecolor=NAVY_L)
    ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.93),1,0.07,color=c))
    ax.text(0.5,0.60,v,ha='center',va='center',fontsize=20,color=c,fontweight='bold',multialignment='center')
    ax.text(0.5,0.20,l,ha='center',va='center',fontsize=9,color=GREY_L,multialignment='center')

ax_b=fig.add_axes([0.03,0.09,0.44,0.49],facecolor=NAVY_L)
sc=['2025\n(Now)','Base 2026','Base 2027','Base 2028','Full\nPotential 2030']
sol=[938,2362,3242,3337,15185];win=[1021,1021,1867,1867,9344]
x=np.arange(5);w=0.35
b1=ax_b.bar(x-w/2,sol,w,color=AMBER,label='Solar PV',edgecolor='none')
b2=ax_b.bar(x+w/2,win,w,color=TEAL,label='Wind',edgecolor='none')
ax_b.set_facecolor(NAVY_L);ax_b.spines[:].set_visible(False)
ax_b.set_xticks(x);ax_b.set_xticklabels(sc,color=GREY_L,fontsize=9)
ax_b.tick_params(colors=GREY_M)
ax_b.set_ylabel('Installed Capacity (MW)',color=GREY_L,fontsize=9)
ax_b.set_title('Capacity Trajectory — Base Case vs Full Pipeline',color=TEAL,fontsize=10,fontweight='bold')
ax_b.legend(facecolor=NAVY,edgecolor='none',labelcolor=WHITE,fontsize=9)
for b in list(b1)+list(b2):
    h=b.get_height()
    if h>1500: ax_b.text(b.get_x()+b.get_width()/2,h+150,f'{h:,.0f}',ha='center',color=WHITE,fontsize=7)

ax_r=fig.add_axes([0.50,0.09,0.48,0.49],facecolor=NAVY_L)
ax_r.axis('off');ax_r.set_xlim(0,1);ax_r.set_ylim(0,1)
ax_r.add_patch(plt.Rectangle((0,0.90),1,0.10,color=TEAL))
ax_r.text(0.5,0.95,'KEY DEVELOPMENT REGIONS & RECENT PROJECTS',ha='center',va='center',fontsize=10,color=NAVY,fontweight='bold')
regs=[(AMBER,'ICA','Solar+Wind','Villacuri 470MW · San Pedro 1,800MW pipeline\nWayra 72MW solar · Ica wind (500MW Inkia)'),
      (TEAL,'PIURA','Wind Hub','Bayóvar Wind Farm — $1.056B investment'),
      (GREEN,'AREQUIPA','Solar Prime','La Joya 225MW (ACCIONA 2024) · Clemesí 204MW\nGHI >6.5 kWh/m²/day'),
      (PURPLE,'LAMBAYEQUE','Wind','Mórrope Wind Farm — $353M investment'),
      (GREY_M,'MOQUEGUA','Solar','Sunny Solar 204MW → 309MW (Kallpa, 2026)')]
y=0.83
for col,reg,tech,proj in regs:
    ax_r.add_patch(plt.Rectangle((0.01,y-0.14),0.98,0.155,color='#0D1B2A'))
    ax_r.add_patch(plt.Rectangle((0.01,y-0.14),0.04,0.155,color=col))
    ax_r.text(0.065,y-0.03,reg,fontsize=10,color=col,fontweight='bold',va='center')
    ax_r.text(0.30,y-0.03,f'[{tech}]',fontsize=8.5,color=GREY_L,va='center')
    for i,line in enumerate(proj.split('\n')[:2]):
        ax_r.text(0.065,y-0.075-i*0.038,line,fontsize=8,color=WHITE,va='center')
    y-=0.175
save(fig,2,'market_context')

# ═══ SLIDE 3 CABLING ══════════════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'BOS: Cabling & Electrical Infrastructure','DC collection, AC distribution & HV connection supply landscape',3,10)
ftr(fig)

cc=[('Indeco\n(Nexans Group)','★ LOCAL LEADER','Peru mfg. base','DC, MV/LV & HV cables up to 220kV\nFastest delivery · Competitive pricing\nPreferred for all standard cable scope',TEAL,'Active across all major\nPeru solar & wind projects'),
    ('CEP\n(Conductores Elec. Peruanos)','LOCAL #2','Peru mfg. base','DC & AC power cables\nCompetitive on bulk volumes\nGood for LV/MV BOS scope',AMBER,'Multiple Ica corridor projects\nwind BOP civil scope'),
    ('Phelps Dodge\n/ Belden','IMPORT — USA','Premium/ESG','HV specialist cables · DC tray cable\nMedium voltage · ESG credentials\nPreferred on IFC-financed projects',GREEN,'IFC-financed projects in Peru\nESG-compliant specification'),
    ('NKT / Nexans\n(Direct Import)','HV SPECIALIST','Europe','Extra high voltage (EHV) 220kV+\nTransmission-grade quality\n6–10 month lead time',PURPLE,'HV grid connection scope\non large utility projects')]

pos_c=[[0.02,0.50,0.20,0.45],[0.23,0.50,0.20,0.45],[0.44,0.50,0.20,0.45],[0.65,0.50,0.20,0.45]]
for (name,tier,origin,note,col,sub),pos in zip(cc,pos_c):
    card(fig,pos,name,tier,origin,note,col,sub)

ax_d=fig.add_axes([0.03,0.07,0.27,0.40],facecolor=NAVY)
ax_d.set_facecolor(NAVY)
w,_=ax_d.pie([45,30,15,10],colors=[TEAL,AMBER,GREEN,GREY_M],startangle=90,
             wedgeprops=dict(width=0.52,edgecolor=NAVY,linewidth=2))
ax_d.text(0,0,'Cable\nOrigin\nMix',ha='center',va='center',fontsize=9,color=WHITE,fontweight='bold',multialignment='center')
ax_d.set_title('Cable Supply Origin (Peru)',color=TEAL,fontsize=10,fontweight='bold')
ax_d.legend(w,['Local MV/LV 45%','China import 30%','Europe HV 15%','USA 10%'],
            loc='lower center',bbox_to_anchor=(0.5,-0.22),ncol=2,facecolor=NAVY_L,edgecolor='none',labelcolor=WHITE,fontsize=8.5)

ax_g=fig.add_axes([0.34,0.07,0.46,0.40],facecolor=NAVY_L)
ax_g.axis('off');ax_g.set_xlim(0,1);ax_g.set_ylim(0,1)
ax_g.add_patch(plt.Rectangle((0,0.92),1,0.08,color=TEAL))
ax_g.text(0.5,0.96,'CABLE PROCUREMENT STRATEGY',ha='center',va='center',fontsize=11,color=NAVY,fontweight='bold')
tips=[('DC Collection (string to combiner)','Local (Indeco/CEP) — fast delivery, ~40% cheaper than import'),
      ('AC Distribution (inverter to trafo)','Local or import — Indeco capable for standard cross-sections'),
      ('MV Collection (combiner to substation)','Dual-source: Indeco + Phelps Dodge for IFC-financed scope'),
      ('HV Grid Connection (132kV+)','Import only — NKT or Nexans. 6–10 month lead. Order at FID.'),
      ('Cable Trays & Conduit','100% local — Peruvian fabricators; no reason to import')]
y=0.82
for scope,strat in tips:
    ax_g.add_patch(plt.Rectangle((0.01,y-0.12),0.98,0.13,color='#0D1B2A'))
    ax_g.text(0.03,y-0.03,scope,fontsize=9,color=TEAL,fontweight='bold',va='center')
    ax_g.text(0.03,y-0.09,strat,fontsize=8.5,color=GREY_L,va='center')
    y-=0.158

ax_lt=fig.add_axes([0.82,0.07,0.17,0.40],facecolor=NAVY_L)
ax_lt.axis('off');ax_lt.set_xlim(0,1);ax_lt.set_ylim(0,1)
ax_lt.add_patch(plt.Rectangle((0,0.92),1,0.08,color=AMBER))
ax_lt.text(0.5,0.96,'LEAD TIMES',ha='center',va='center',fontsize=10,color=NAVY,fontweight='bold')
for lt,lv,c,y in [('DC Cable','2–4 wks',GREEN,0.78),('AC/MV Cable','4–8 wks',AMBER,0.61),
                   ('HV 132kV+','6–10 mths',RED,0.44),('EHV 220kV+','10–14 mths',RED,0.27)]:
    ax_lt.text(0.5,y,lt,ha='center',fontsize=9,color=WHITE,fontweight='bold')
    ax_lt.text(0.5,y-0.09,lv,ha='center',fontsize=14,color=c,fontweight='bold')
save(fig,3,'cabling')

# ═══ SLIDE 4 TRANSFORMERS ═════════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'BOS: Transformers, Switchgear & HV Equipment','Critical long-lead items — global shortage & strategic procurement',4,10)
ftr(fig)

hv=[('ABB / Hitachi Energy','★ BENCHMARK','Global #1/2','Preferred by European developers\nFull range MV–EHV · IEC/IEEE certified\nDigital substation capability',TEAL,'Substation scope Kallpa\nprojects — KEY reference'),
    ('Siemens Energy','★ STRONG #2','Global #2/3','SIEMENS GIS/AIS switchgear\nDigital substation integration\nPremium price / excellent reliability',AMBER,'Active Peru energy sector\nMultiple substation references'),
    ('Schneider Electric','LOCAL OFFICE','France/Global','Lima office — fastest local support\nMV switchgear (Premset, SM6)\nGood for MV distribution scope',GREEN,'Distribution switchgear\nacross Peru solar portfolio'),
    ('CHINT / TBEA','COST OPTION','China','30–40% lower capex vs ABB\nGrowing LatAm track record\nESG/FEOC scrutiny applies',RED,'Chinese-financed projects\nin Peru and LatAm')]

pos_hv=[[0.02,0.50,0.22,0.45],[0.25,0.50,0.22,0.45],[0.48,0.50,0.22,0.45],[0.71,0.50,0.22,0.45]]
for (name,tier,origin,note,col,sub),pos in zip(hv,pos_hv):
    card(fig,pos,name,tier,origin,note,col,sub)

ax_dep=fig.add_axes([0.02,0.07,0.31,0.40],facecolor=NAVY_L)
items=['MV/HV Transformers','GIS Switchgear','HV Circuit Breakers','MV Switchgear','Protection Relays','SCADA/Control']
pcts=[70,80,85,65,90,90]
cols=[RED if p>=80 else AMBER if p>=60 else GREEN for p in pcts]
hbar(ax_dep,items,pcts,cols,title='Import Dependency (%)')

ax_w=fig.add_axes([0.36,0.07,0.30,0.40],facecolor=NAVY_L)
ax_w.axis('off');ax_w.set_xlim(0,1);ax_w.set_ylim(0,1)
ax_w.add_patch(plt.Rectangle((0,0.92),1,0.08,color=RED))
ax_w.text(0.5,0.96,'GLOBAL SHORTAGE ALERT',ha='center',va='center',fontsize=11,color=WHITE,fontweight='bold')
for v,l,c,y in [('10–14 months','HV Transformer\nlead time (2025–26)',RED,0.75),
                ('6–10 months','GIS Switchgear\nlead time',AMBER,0.50),
                ('+40%','Global demand\nsince 2022',AMBER,0.28),
                ('Order at FID\nor earlier','Critical path risk',RED,0.10)]:
    ax_w.text(0.5,y,v,ha='center',fontsize=14,color=c,fontweight='bold',multialignment='center')
    ax_w.text(0.5,y-0.10,l,ha='center',fontsize=8,color=GREY_L,multialignment='center')

ax_s=fig.add_axes([0.69,0.07,0.30,0.40],facecolor=NAVY_L)
ax_s.axis('off');ax_s.set_xlim(0,1);ax_s.set_ylim(0,1)
ax_s.add_patch(plt.Rectangle((0,0.92),1,0.08,color=TEAL))
ax_s.text(0.5,0.96,'PROCUREMENT STRATEGY',ha='center',va='center',fontsize=11,color=NAVY,fontweight='bold')
for num,txt,y in [('1.','Frame agreements NOW\nwith ABB & Siemens',0.78),
                   ('2.','Dual-source all\ntransformer packages',0.57),
                   ('3.','CHINT/TBEA only for\nnon-IFC cost-critical scope',0.36),
                   ('4.','Schneider for MV distrib.\n— fastest local support',0.15)]:
    ax_s.add_patch(plt.Rectangle((0.03,y-0.14),0.94,0.155,color='#0D1B2A'))
    ax_s.text(0.08,y-0.055,num,fontsize=12,color=TEAL,fontweight='bold',va='center')
    ax_s.text(0.20,y-0.055,txt,fontsize=8.5,color=WHITE,va='center')
save(fig,4,'transformers')

# ═══ SLIDE 5 BOS MARKET PLAYERS ════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'BOS Market Players — Integrated Specialists','CJR Renewables, Elecnor, Cobra & emerging players in Peru',5,10)
ftr(fig)

players=[
    ('CJR Renewables','Portugal · Est. 2003',TEAL,'★ INTEGRATED BOS/BOP SPECIALIST',
     'Full EPC/BOP/BOS: design, civil construction,\nelectrical installation, turbine erection.\nChile subsidiary (CJR Wind Chile, Santiago).\nStrong LatAm wind track record.',
     'Sarco wind farm (Chile)\nBOS/BOP multiple LatAm projects\n→ Evaluating Peru pipeline entry',
     [0.02,0.52,0.23,0.44]),
    ('Elecnor Group','Spain · Global EPC',AMBER,'★ MAJOR LATAM EPC',
     'Global engineering group with renewables arm.\nEPC leader in Brazil (Atlas RE solar, 100s MW).\nHas Celeo Redes — grid concession arm.\nActive in Chile, Colombia, Brazil.',
     'Brazil: largest solar farms (Atlas RE)\nChile: wind & solar EPC\n→ Active Peru market studies',
     [0.26,0.52,0.23,0.44]),
    ('Cobra (ACS Group)','Spain · Global',GREEN,'EPC + GRID SPECIALIST',
     'ACS Group engineering division.\nHV grid connection & substation EPC.\nStrong on transmission infrastructure.\nActive in Peru grid scope.',
     'Peru HV transmission projects\nGrid connection on Ica corridor\n→ Grid-connected EPC scope',
     [0.50,0.52,0.23,0.44]),
    ('COMSA','Spain',PURPLE,'ELECTRICAL EPC',
     'Spanish EPC, electrical infrastructure focus.\nMV/HV substations, grid connections.\nGrowing LatAm renewable presence.\nGood competitor to Cobra on electrical scope.',
     'Chile & Colombia EPC references\nLatAm electrical infrastructure\n→ Peru pipeline interest',
     [0.74,0.52,0.23,0.44]),
    ('ISA / REP\n(Red de Energía del Perú)','Colombia/Peru · Transmission',TEAL,'GRID OWNER — MUST ENGAGE',
     'Owns & operates Peru\'s main transmission grid.\nKey counterparty for all grid connections.\nOwner-procure approach essential.\nProject timelines directly dependent on REP.',
     'All Peru HV grid connections\ngo through ISA/REP\n→ Engage before EPC award',
     [0.02,0.05,0.23,0.42]),
    ('Inkia Energy','Peru · Developer',ORANGE,'LOCAL DEVELOPER/OPERATOR',
     'Peru\'s largest solar developer.\n1 GW+ solar in operation (2025).\n600 MW wind pipeline 2026.\nPotential reference / joint venture partner.',
     'Sunny Solar 204MW → 338MW\nSan Pedro 1,800MW pipeline\n→ Key market player to engage',
     [0.26,0.05,0.23,0.42]),
    ('ENGIE Peru','France/Global · Developer',CYAN,'IFC-BACKED DEVELOPER',
     'ENGIE secured $600M IFC financing (2025).\nWind, solar & battery storage pipeline.\nSets benchmark for ESG procurement standards.\nPotential EPC competitor / partner.',
     '$600M IFC-backed portfolio\nWind + solar + BESS\n→ ESG standards benchmark',
     [0.50,0.05,0.23,0.42]),
]

for (name,origin,col,tier,desc,refs,pos) in players:
    ax=fig.add_axes(pos,facecolor=NAVY_L)
    ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.95),1,0.05,color=col))
    ax.text(0.5,0.975,tier,ha='center',va='center',fontsize=7.5,color=NAVY,fontweight='bold')
    ax.text(0.5,0.87,name,ha='center',va='center',fontsize=12,color=WHITE,fontweight='bold',multialignment='center')
    ax.text(0.5,0.79,origin,ha='center',fontsize=8,color=GREY_L)
    ax.add_patch(plt.Rectangle((0.03,0.50),0.94,0.27,color='#0D1B2A'))
    for i,line in enumerate(desc.split('\n')[:3]):
        ax.text(0.5,0.72-i*0.09,line,ha='center',fontsize=7.5,color=WHITE,multialignment='center')
    ax.text(0.5,0.38,'References / Status:',ha='center',fontsize=7.5,color=col,fontweight='bold')
    for i,line in enumerate(refs.split('\n')[:3]):
        ax.text(0.5,0.30-i*0.09,line,ha='center',fontsize=7.5,color=GREY_L,multialignment='center')

ax_box=fig.add_axes([0.74,0.05,0.25,0.42],facecolor=NAVY_L)
ax_box.axis('off');ax_box.set_xlim(0,1);ax_box.set_ylim(0,1)
ax_box.add_patch(plt.Rectangle((0,0.96),1,0.04,color=AMBER))
ax_box.text(0.5,0.88,'STRATEGIC\nRECOMMENDATION',ha='center',fontsize=11,color=AMBER,fontweight='bold',multialignment='center')
for txt,y in [('CJR: best for integrated\nBOS/BOP on wind projects',0.74),
              ('Elecnor: best full EPC\nfor large solar (>100MW)',0.55),
              ('Cobra/COMSA: go-to\nfor HV grid connection EPC',0.36),
              ('Always engage ISA/REP\nbefore EPC contract award',0.17)]:
    ax_box.add_patch(plt.Rectangle((0.03,y-0.12),0.94,0.155,color='#0D1B2A'))
    ax_box.text(0.5,y-0.035,txt,ha='center',fontsize=8.5,color=GREY_L,multialignment='center')
save(fig,5,'market_players')

# ═══ SLIDE 6 EPC CONTRACTORS ══════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'EPC & Civil Contractors — Peru Experience','Who has built what — civil BOS track record & strategic fit',6,10)
ftr(fig)

conts=[('ACCIONA','International EPC','Spain',TEAL,'★ MOST RECENT AWARD',
        '225MW La Joya, Arequipa\n(Kallpa Generación, Nov 2024)',
        'Full turnkey EPC. European procurement standards.\nArequipa specialist. Best for >100MW projects.',
        [0.02,0.50,0.23,0.45]),
       ('Grenergy','Developer/EPC','Spain',AMBER,'ACTIVE IN PERU',
        'Matarani 97MW EPC\n(Yinson Renewables, 2024)',
        'Developer with own EPC arm. Deep Peru knowledge.\nGood for sub-200MW. O&M retained post-construction.',
        [0.26,0.50,0.23,0.45]),
       ('Cosapi','Local Civil/BOP','Peru',GREEN,'★ TOP LOCAL CIVIL',
        'Cupisnique wind (civil/BOP, Ica)\nTalara wind + multiple solar scopes',
        "Peru's largest civil contractor. Deep local relationships.\nEssential for BOS civil scope.",
        [0.50,0.50,0.23,0.45]),
       ('JJC Contratistas','Local Civil','Peru',PURPLE,'ESTABLISHED LOCAL',
        'Solar civil works (Ica region)\nRoad & access for wind projects',
        'Earthworks, foundations, access roads. Best option\nfor competitive tension vs Cosapi.',
        [0.74,0.50,0.23,0.45]),
       ('Mota-Engil','Intl Civil','Portugal',ORANGE,'REGIONAL OPTION',
        'Peru infrastructure (roads, civil)\nEnergy sector entry 2024–25',
        'Portuguese group with LatAm footprint. Good #3\nfor civil competition.',
        [0.02,0.05,0.23,0.42]),
       ('Sacyr','Spanish EPC','Spain',CYAN,'REGIONAL EPC',
        'LatAm energy (Chile, Colombia)\nPeru pipeline 2025',
        'Strong civil EPC. Chile model transferable.\nComing up in Peru market.',
        [0.26,0.05,0.23,0.42]),
       ('Graña y Montero','Local Industrial','Peru',RED,'EMERGING ENERGY',
        'Mining civil (transferable skills)\nEnergy sector entry (Ica 2024)',
        "Peru's largest industrial contractor.\nHeavy civil — newer to renewables.",
        [0.50,0.05,0.23,0.42]),]

for (name,ct,origin,col,tier,proj,strength,pos) in conts:
    ax=fig.add_axes(pos,facecolor=NAVY_L)
    ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0.95),1,0.05,color=col))
    ax.text(0.5,0.975,tier,ha='center',va='center',fontsize=7.5,color=NAVY,fontweight='bold')
    ax.text(0.5,0.87,name,ha='center',fontsize=12,color=WHITE,fontweight='bold',multialignment='center')
    ax.text(0.5,0.79,f'{ct} · {origin}',ha='center',fontsize=8,color=GREY_L)
    ax.add_patch(plt.Rectangle((0.03,0.55),0.94,0.22,color='#0D1B2A'))
    ax.text(0.5,0.67,'RECENT PROJECTS',ha='center',fontsize=7.5,color=col,fontweight='bold')
    for i,l in enumerate(proj.split('\n')[:2]):
        ax.text(0.5,0.60-i*0.08,l,ha='center',fontsize=7.5,color=WHITE,multialignment='center')
    for i,l in enumerate(strength.split('\n')[:2]):
        ax.text(0.5,0.40-i*0.11,l,ha='center',fontsize=8,color=GREY_L,multialignment='center')

ax_t=fig.add_axes([0.74,0.05,0.25,0.42],facecolor=NAVY_L)
ax_t.axis('off');ax_t.set_xlim(0,1);ax_t.set_ylim(0,1)
ax_t.add_patch(plt.Rectangle((0,0.96),1,0.04,color=AMBER))
ax_t.text(0.5,0.88,'STRATEGIC\nACTIONS',ha='center',fontsize=11,color=AMBER,fontweight='bold',multialignment='center')
for num,tip,y in [('1.','Pre-qualify Cosapi & JJC NOW\nbefore pipeline unlocks',0.74),
                   ('2.','ACCIONA — full EPC >100MW',0.55),
                   ('3.','Grenergy for 50–200MW\n(deep Peru knowledge)',0.37),
                   ('4.','Always dual-source civil:\nCosapi + one other',0.18)]:
    ax_t.add_patch(plt.Rectangle((0.03,y-0.13),0.94,0.155,color='#0D1B2A'))
    ax_t.text(0.08,y-0.045,num,fontsize=12,color=AMBER,fontweight='bold',va='center')
    ax_t.text(0.20,y-0.045,tip,fontsize=8.5,color=GREY_L,va='center')
save(fig,6,'epc_contractors')

# ═══ SLIDE 7 SUPPLY CHAIN ═════════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'BOS Supply Chain Origin','Import dependency by component & equipment origin mix',7,10)
ftr(fig)

ax_m=fig.add_axes([0.03,0.10,0.56,0.80],facecolor=NAVY_L)
items=['SCADA/Control Systems','HV Circuit Breakers','Protection Relays','GIS Switchgear',
       'MV/HV Transformers','MV Collection Cables','HV Cabling (132kV+)',
       'MV Switchgear','DC/AC Distribution Cables','Civil Works (Foundations)','Concrete & Aggregate']
pcts=[90,85,90,80,70,40,60,65,35,12,5]
cols=[RED if p>=75 else AMBER if p>=45 else GREEN for p in pcts]
hbar(ax_m,items,pcts,cols,title='BOS Component Import Dependency  (% of value imported)')

ax_leg=fig.add_axes([0.03,0.06,0.56,0.04],facecolor=NAVY)
ax_leg.axis('off');ax_leg.set_xlim(0,1);ax_leg.set_ylim(0,1)
for i,(c,l) in enumerate([(RED,'≥75%  Critical import'),(AMBER,'45–74%  Moderate'),(GREEN,'<45%  Local capable')]):
    ax_leg.add_patch(plt.Rectangle((0.02+i*0.33,0.1),0.03,0.8,color=c))
    ax_leg.text(0.06+i*0.33,0.5,l,fontsize=9,color=WHITE,va='center')

ax_d=fig.add_axes([0.63,0.48,0.34,0.42],facecolor=NAVY)
ax_d.set_facecolor(NAVY)
w,_=ax_d.pie([72,14,8,6],colors=[TEAL,AMBER,GREEN,PURPLE],startangle=90,
             wedgeprops=dict(width=0.52,edgecolor=NAVY,linewidth=2))
ax_d.text(0,0,'BOS\nOrigin\nMix',ha='center',va='center',fontsize=9,color=WHITE,fontweight='bold',multialignment='center')
ax_d.set_title('BOS Equipment Origin — Peru',color=TEAL,fontsize=10,fontweight='bold')
ax_d.legend(w,['China 72%','Europe 14%','USA 8%','Local 6%'],loc='lower center',
            bbox_to_anchor=(0.5,-0.20),ncol=2,facecolor=NAVY_L,edgecolor='none',labelcolor=WHITE,fontsize=9)

cb=[(AMBER,'CUSTOMS ADVANTAGE','FTAs with China, US & EU.\nDuties 0–6% on RE equipment.\nClearance variance 30–90 days.\nSpecialist broker recommended.'),
    (RED,'TRANSFORMER SHORTAGE','Global shortage — 10–14 months.\nOrder at FID minimum.\nFrame now with ABB/Siemens.\nDo not wait for EPC contractor.'),
    (GREEN,'LOCAL OPPORTUNITY','Civil works: 85–90% local.\nCables LV/MV: 40–50% local.\nMaximise local for FX hedge\n& community social licence.')]
yc=0.06
for col,title,body in cb:
    ax_c=fig.add_axes([0.63,yc,0.36,0.135],facecolor=NAVY_L)
    ax_c.axis('off');ax_c.set_xlim(0,1);ax_c.set_ylim(0,1)
    ax_c.add_patch(plt.Rectangle((0,0),0.025,1,color=col))
    ax_c.text(0.04,0.80,title,fontsize=10,color=col,fontweight='bold',va='center')
    for i,line in enumerate(body.split('\n')[:3]):
        ax_c.text(0.04,0.52-i*0.22,line,fontsize=8.5,color=GREY_L,va='center')
    yc+=0.147
save(fig,7,'supply_chain')

# ═══ SLIDE 8 RISK MATRIX ══════════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'BOS Procurement Risk Matrix','Likelihood vs Impact — Peru solar projects',8,10)
ftr(fig)

ax=fig.add_axes([0.04,0.09,0.58,0.81],facecolor=NAVY_L)
ax.spines[:].set_visible(False);ax.set_facecolor(NAVY_L)
ax.set_xlim(0,6);ax.set_ylim(0,6)
ax.set_xlabel('LIKELIHOOD →',color=GREY_L,fontsize=10,labelpad=8)
ax.set_ylabel('IMPACT →',color=GREY_L,fontsize=10,labelpad=8)
ax.set_xticks([1,2,3,4,5]);ax.set_xticklabels(['Very Low','Low','Medium','High','Very High'],color=GREY_L,fontsize=8)
ax.set_yticks([1,2,3,4,5]);ax.set_yticklabels(['Negligible','Minor','Moderate','Major','Critical'],color=GREY_L,fontsize=8)
ax.tick_params(colors=GREY_M)
for (x,y,w,h,c,a) in [(0,0,2.5,2.5,'#1A3A1A',0.4),(2.5,0,3.5,2.5,'#3A3A1A',0.4),
                        (0,2.5,2.5,3.5,'#3A3A1A',0.4),(2.5,2.5,3.5,3.5,'#3A1A1A',0.4)]:
    ax.add_patch(plt.Rectangle((x,y),w,h,color=c,alpha=a))
ax.text(1.2,1.2,'LOW\nRISK',ha='center',fontsize=9,color=GREEN,alpha=0.7,fontweight='bold')
ax.text(3.7,1.2,'WATCH',ha='center',fontsize=9,color=AMBER,alpha=0.7,fontweight='bold')
ax.text(1.2,3.7,'WATCH',ha='center',fontsize=9,color=AMBER,alpha=0.7,fontweight='bold')
ax.text(4.0,4.2,'CRITICAL\nRISK ZONE',ha='center',fontsize=9,color=RED,alpha=0.8,fontweight='bold',multialignment='center')

rs=[(4.5,4.8,'Grid connection\ndelay',RED,'G'),(4.2,4.5,'Transformer\nshortage',RED,'T'),
    (4.3,4.0,'MINEM permitting',RED,'P'),(3.8,3.5,'Civil contractor\ncapacity',AMBER,'C'),
    (3.5,3.8,'PPA unavailability',AMBER,'PPA'),(3.0,2.8,'Customs delay',AMBER,'CU'),
    (3.2,2.5,'PEN inflation',AMBER,'FX'),(1.8,3.5,'FEOC/ESG\nscrutiny',GREEN,'F'),
    (1.5,2.0,'Single-source\ncabling',GREEN,'S')]
for rx,ry,lbl,c,code in rs:
    ax.scatter(rx,ry,s=350,color=c,zorder=5,edgecolors=NAVY,linewidth=1.5)
    ax.annotate(f'{code}\n{lbl}',(rx,ry),xytext=(rx+0.3,ry+0.35),fontsize=7,color=WHITE,
                arrowprops=dict(arrowstyle='->',color=GREY_M,lw=0.8),multialignment='center')
ax.set_title('BOS Procurement Risk — Likelihood vs Impact',color=TEAL,fontsize=11,fontweight='bold')

ax_l=fig.add_axes([0.65,0.09,0.34,0.81],facecolor=NAVY_L)
ax_l.axis('off');ax_l.set_xlim(0,1);ax_l.set_ylim(0,1)
ax_l.add_patch(plt.Rectangle((0,0.96),1,0.04,color=RED))
ax_l.text(0.5,0.98,'RISK MITIGATIONS',ha='center',va='center',fontsize=10,color=WHITE,fontweight='bold')
rk=[('G',RED,'Grid connection delay','Owner-procure; 20% contingency'),
    ('T',RED,'Transformer shortage','Frame ABB/Siemens now; order at FID'),
    ('P',RED,'MINEM permitting','Gate spend to final concession'),
    ('C',AMBER,'Civil contractor capacity','Pre-qualify Cosapi/JJC immediately'),
    ('PPA',AMBER,'PPA unavailability','NTP-linked procurement structure'),
    ('CU',AMBER,'Customs delay','Specialist broker; buffer lead times'),
    ('FX',AMBER,'PEN inflation','CPI clauses on civil contracts'),
    ('F',GREEN,'FEOC/ESG scrutiny','Xinjiang attestation in pre-qual'),
    ('S',GREEN,'Single-source cabling','Dual-source Indeco + import OEM')]
y=0.89
for code,c,name,mit in rk:
    ax_l.add_patch(plt.Circle((0.05,y-0.01),0.028,color=c))
    ax_l.text(0.065,y-0.01,code,ha='center',va='center',fontsize=7,color=NAVY,fontweight='bold')
    ax_l.text(0.11,y+0.01,name,fontsize=9,color=WHITE,fontweight='bold')
    ax_l.text(0.11,y-0.04,mit,fontsize=8,color=GREY_L)
    ax_l.plot([0.02,0.98],[y-0.075,y-0.075],color='#1E3A5F',linewidth=0.4)
    y-=0.098
save(fig,8,'risk_matrix')

# ═══ SLIDE 9 SCORECARD — PURE BOS ═════════════════════════════════════════════
fig=new_fig()
hdr(fig,'BOS Component Scorecard','Peru — Procurement readiness rated by BOS component',9,10)
ftr(fig)

scores=[
    ('Cabling — LV/MV (DC/AC)',       4,GREEN, 'Strong local supply (Indeco, CEP); fast delivery; competitive pricing'),
    ('Cabling — HV (132kV+)',          2,RED,   'Import-only; 6–10 month lead; NKT/Nexans from Europe'),
    ('Transformers (MV/HV)',           2,RED,   'Import-dominant (70%); 10–14 month lead; GLOBAL SHORTAGE'),
    ('Switchgear & Protection',        3,AMBER, 'ABB/Schneider/Siemens active in Peru; 65–85% import dependent'),
    ('SCADA & Control Systems',        3,AMBER, 'Import-dominant (90%); OEM-integrated preferred approach'),
    ('Civil Works — Foundations/Roads',4,GREEN, 'Cosapi/JJC strong; 85–90% local; capacity risk as pipeline builds'),
    ('Civil Works — Electrical Install',3,AMBER,'Partially local; quality control critical for MV/HV scope'),
    ('Grid Connection (HV to grid)',   2,RED,   'Highest-risk BOS item; transmission bottleneck in Peru'),
    ('Integrated BOS Contractors',     3,AMBER, 'CJR/Elecnor strong LatAm; Peru-specific experience building'),
    ('EPC Civil Contractors (Peru)',   4,GREEN, 'ACCIONA, Grenergy, Cosapi, JJC — solid track records'),
]

ax_s=fig.add_axes([0.02,0.08,0.62,0.82],facecolor=NAVY_L)
ax_s.axis('off');ax_s.set_xlim(0,1);ax_s.set_ylim(0,1)
ax_s.add_patch(plt.Rectangle((0,0.96),1,0.04,color=TEAL))
ax_s.text(0.02,0.965,'BOS COMPONENT',fontsize=9,color=NAVY,fontweight='bold',va='center')
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
    ax_s.text(0.82,y-0.033,comment,fontsize=7.5,color=GREY_L,va='center')
    y-=0.09

ax_v=fig.add_axes([0.67,0.08,0.32,0.82],facecolor=NAVY_L)
ax_v.axis('off');ax_v.set_xlim(0,1);ax_v.set_ylim(0,1)
ax_v.add_patch(plt.Rectangle((0,0.96),1,0.04,color=TEAL))
ax_v.text(0.5,0.89,'BOS SUMMARY',ha='center',fontsize=14,color=TEAL,fontweight='bold')

summary=[('STRONG',  GREEN,  'Local civil & LV/MV cabling\n— procure locally'),
         ('WATCH',   AMBER,  'Switchgear, SCADA,\nelectrical install quality'),
         ('CRITICAL',RED,    'Transformers, HV cables,\ngrid connection'),]
y=0.74
for label,col,desc in summary:
    ax_v.add_patch(plt.Rectangle((0.05,y-0.13),0.90,0.155,color='#0D1B2A'))
    ax_v.add_patch(plt.Rectangle((0.05,y-0.13),0.06,0.155,color=col))
    ax_v.text(0.15,y-0.04,label,fontsize=11,color=col,fontweight='bold',va='center')
    ax_v.text(0.15,y-0.10,desc,fontsize=8.5,color=GREY_L,va='center')
    y-=0.185

ax_v.add_patch(plt.Rectangle((0.05,0.07),0.90,0.26,color='#0D1B2A'))
ax_v.text(0.5,0.30,'TOP 5 ACTIONS',ha='center',fontsize=9,color=AMBER,fontweight='bold')
for i,(act,col) in enumerate([('Frame ABB/Siemens (transformers)',RED),
                               ('Frame NKT/Nexans (HV cables)',AMBER),
                               ('Pre-qualify Cosapi + JJC (civil)',GREEN),
                               ('Indeco as primary cable supplier',TEAL),
                               ('Owner-procure grid — 20% contingency',RED)]):
    ax_v.add_patch(plt.Rectangle((0.07,0.23-i*0.038),0.025,0.030,color=col))
    ax_v.text(0.12,0.238-i*0.038,act,fontsize=8,color=GREY_L,va='center')
save(fig,9,'scorecard')

# ═══ SLIDE 10 RECOMMENDATIONS ═════════════════════════════════════════════════
fig=new_fig()
hdr(fig,'Strategic Procurement Recommendations','Statkraft Peru BOS — Priority Actions for 2026',10,10)
ftr(fig)

recs=[(TEAL,'01','Frame Agreements: Transformers & HV Cables First',
       'ABB and Siemens Energy for HV transformers — 10–14 month lead time, global shortage.\nNKT or Nexans (Europe) for HV cables 132kV+ — 6–10 month lead. Order at FID minimum.\nTarget signed frame agreements BEFORE MINEM pipeline unlocks (est. mid-2026).','Q1 2026'),
      (AMBER,'02','Pre-Qualify Civil Contractors Immediately',
       'Cosapi and JJC for BOS civil — pre-qual now before pipeline absorbs capacity.\nACCIONA (full EPC >100MW) and Grenergy (50–200MW) for international EPC scope.\nCJR Renewables and Elecnor for integrated BOS/EPC — both evaluating Peru market entry.','Q1–Q2 2026'),
      (GREEN,'03','Establish Local Cable Supply: Indeco Primary',
       'Indeco (Nexans Group) as primary — local manufacturing, fastest delivery, competitive price.\nDual-source with Phelps Dodge for IFC-financed scope (ESG credentials required).\nLock MV cable volume early — pricing leverage before demand surge hits Ica corridor.','Q2 2026'),
      (TEAL,'04','Owner-Procure Grid Connection — Engage ISA/REP Early',
       'Grid connection is highest-risk BOS item in Peru. Never wrap in EPC package.\nISA/REP is the key counterparty — engage before EPC award, not after.\nBudget 15–20% contingency. Variance: $30/kW (near lines) to $150+/kW (remote sites).','Immediate'),
      (RED,'05','Gate Procurement Spend to MINEM Concession',
       '95 of 114 projects still pending final concession — procurement spend at risk if stalled.\nNTP-linked structure: warm supplier relationships but no financial commitments pre-concession.','Standing'),
      (AMBER,'06','Build Dual-Source Across All BOS Categories',
       'Transformers: ABB + Siemens  ·  HV Cables: NKT + Nexans  ·  MV/LV: Indeco + Phelps Dodge\nCivil: Cosapi + JJC  ·  Electrical EPC: ACCIONA + Grenergy or CJR/Elecnor','All projects')]

pr=[[0.02,0.53,0.47,0.41],[0.51,0.53,0.47,0.41],
    [0.02,0.10,0.47,0.41],[0.51,0.10,0.47,0.41]]
for i,(col,num,title,body,timing) in enumerate(recs[:4]):
    ax=fig.add_axes(pr[i],facecolor=NAVY_L)
    ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0),0.012,1,color=col))
    ax.add_patch(plt.Rectangle((0.015,0.76),0.10,0.21,color=col))
    ax.text(0.065,0.865,num,ha='center',va='center',fontsize=22,color=NAVY,fontweight='bold')
    ax.text(0.14,0.89,title,fontsize=11,color=col,fontweight='bold',va='center')
    ax.text(0.14,0.73,f'Timing: {timing}',fontsize=8,color=AMBER,va='center')
    for j,line in enumerate(body.split('\n')[:3]):
        ax.text(0.025,0.58-j*0.17,'→ '+line.strip(),fontsize=8.5,color=GREY_L,va='top')

for i,(col,num,title,body,timing) in enumerate(recs[4:]):
    ax=fig.add_axes([0.02+i*0.49,0.02,0.47,0.07],facecolor=NAVY_L)
    ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.add_patch(plt.Rectangle((0,0),0.005,1,color=col))
    ax.text(0.015,0.72,f'{num}: {title}',fontsize=9,color=col,fontweight='bold',va='center')
    ax.text(0.015,0.25,body.split('\n')[0],fontsize=8,color=GREY_L,va='center')
save(fig,10,'recommendations')

print('\nRev 2 complete. 10 slides. Pure BOS focus.')
