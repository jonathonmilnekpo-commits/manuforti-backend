from PIL import Image, ImageDraw, ImageFont
import os

OUT = '/tmp/slides_preview/rendered'
os.makedirs(OUT, exist_ok=True)

W, H = 1920, 1080

# Colours
NAVY       = (13,  27,  42)
NAVY_L     = (22,  42,  68)
TEAL       = (0,   180, 216)
AMBER      = (245, 166, 35)
GREEN      = (46,  204, 113)
RED        = (231, 76,  60)
WHITE      = (255, 255, 255)
GREY_L     = (176, 190, 197)
GREY_M     = (84,  110, 122)
DIVIDER    = (30,  58,  95)

def get_font(size, bold=False):
    try:
        path = '/System/Library/Fonts/Helvetica.ttc'
        return ImageFont.truetype(path, size, index=1 if bold else 0)
    except:
        return ImageFont.load_default()

def new_slide():
    img = Image.new('RGB', (W, H), NAVY)
    d   = ImageDraw.Draw(img)
    return img, d

def header(d, title, subtitle=''):
    d.rectangle([0, 0, W, 108], fill=NAVY_L)
    d.rectangle([0, 0, 32, 108], fill=TEAL)
    d.text((55, 18), title,    font=get_font(36, True), fill=WHITE)
    if subtitle:
        d.text((55, 68), subtitle, font=get_font(18),      fill=GREY_L)
    d.text((W-20, 42), 'STATKRAFT  ·  CONFIDENTIAL',
           font=get_font(14), fill=GREY_M, anchor='rm')

def footer_bar(d, page):
    d.rectangle([0, H-40, W, H], fill=NAVY_L)
    d.text((30, H-28), 'Peru BOS/BOP Market Analysis  ·  Statkraft Procurement  ·  February 2026',
           font=get_font(13), fill=GREY_M)
    d.text((W-20, H-28), str(page), font=get_font(13), fill=GREY_M, anchor='rm')

def card(d, x, y, w, h, fill=NAVY_L, accent=None, lw=3):
    d.rectangle([x, y, x+w, y+h], fill=fill)
    if accent:
        d.rectangle([x, y, x+lw, y+h], fill=accent)

def row_bg(d, x, y, w, h, shade):
    fill = (16, 34, 56) if shade else NAVY_L
    d.rectangle([x, y, x+w, y+h], fill=fill)

def save(img, n, name):
    path = f'{OUT}/slide_{n:02d}_{name}.jpg'
    img.save(path, 'JPEG', quality=90)
    print(f'Saved: {path}')
    return path

# ── SLIDE 1: COVER ────────────────────────────────────────────────────────────
img, d = new_slide()
d.rectangle([0, 0, 48, H], fill=TEAL)
d.rectangle([48, 400, W, 406], fill=TEAL)
d.rectangle([48, 748, W, 754], fill=AMBER)
d.text((80, 140), 'PERU RENEWABLE ENERGY', font=get_font(22, True), fill=TEAL)
d.text((80, 195), 'BOS & BOP', font=get_font(96, True), fill=WHITE)
d.text((80, 305), 'Market Analysis', font=get_font(72, True), fill=WHITE)
d.text((80, 430), 'Balance of System  ·  Balance of Plant  ·  Wind & Solar',
       font=get_font(24), fill=GREY_L)
d.text((80, 780), 'Statkraft Procurement International  ·  February 2026  ·  CONFIDENTIAL',
       font=get_font(20, True), fill=AMBER)
d.text((80, 830), 'Prepared by: Aiden  ·  For: Jonathon Milne, VP Procurement International',
       font=get_font(18), fill=GREY_L)
save(img, 1, 'cover')

# ── SLIDE 2: EXEC SUMMARY ─────────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Executive Summary', 'Peru BOS/BOP — Key Findings at a Glance')

kpis = [
    (50,  130, '20,000+ MW', 'Renewable pipeline\n(solar+wind)', TEAL),
    (530, 130, '19 / 114',   'Projects with final\nMINEM concession', AMBER),
    (1010,130, '$700–900/kW','Utility-scale solar\nall-in CAPEX (2025)', GREEN),
    (1480,130, '$1,100–1,400/kW','Onshore wind\nall-in CAPEX (2025)', TEAL),
]
for x, y, val, lbl, col in kpis:
    d.rectangle([x, y, x+400, y+160], fill=NAVY_L)
    d.rectangle([x, y, x+400, y+8], fill=col)
    d.text((x+16, y+18), val, font=get_font(30, True), fill=col)
    for i, line in enumerate(lbl.split('\n')):
        d.text((x+16, y+68+i*26), line, font=get_font(16), fill=GREY_L)

d.rectangle([50, 308, W-50, 310], fill=DIVIDER)

findings = [
    (TEAL,  '🌞  Solar BOS', '~40–55% of project CAPEX. Inverters, trackers and transformers are 70–95% imported (China-dominant). Local value concentrated in civil works and DC cabling.'),
    (AMBER, '💨  Wind BOP',  '~30–45% of project CAPEX. Turbines 100% imported. Foundations, roads and crane pads 85–90% local — strong domestic civil contractor base.'),
    (RED,   '⚡  Grid Risk',  'Transmission bottleneck is #1 procurement risk. $430M national investment underway but insufficient for 20 GW pipeline. Build 15–20% cost contingency.'),
    (GREEN, '📋  Bankability','No PPA = no financing. Law 32249 (Jan 2026) improves the framework. Procurement timelines gate-kept by offtake availability.'),
    (TEAL,  '🏗  Strategy',   'If Statkraft develops 1–2 GW in Peru: $400M–$900M in BOS/BOP contracts. Window to lock contractor capacity and frame agreements is NOW.'),
]
y = 325
for col, title, body in findings:
    d.rectangle([50, y, W-50, y+90], fill=NAVY_L)
    d.rectangle([50, y, 62, y+90], fill=col)
    d.text((80, y+12), title, font=get_font(18, True), fill=col)
    d.text((480, y+12), body, font=get_font(16), fill=GREY_L)
    y += 100

footer_bar(d, 2)
save(img, 2, 'exec_summary')

# ── SLIDE 3: MARKET OVERVIEW ──────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Peru Renewable Energy Market', 'Installed Capacity & Pipeline — 2025 to 2030')

cols = ['Scenario', 'Solar PV', 'Wind', 'Total RE', 'Commentary']
col_x = [50, 420, 620, 820, 1060]
col_w = [360, 190, 190, 230, 800]
y = 130
d.rectangle([50, y, W-50, y+44], fill=TEAL)
for i, (cx, cw, col) in enumerate(zip(col_x, col_w, cols)):
    d.text((cx+10, y+10), col, font=get_font(16, True), fill=WHITE)

rows = [
    ['Current (2025)',       '938 MW',   '1,021 MW', '~1,960 MW', 'Operational today'],
    ['Base case 2026',       '2,362 MW', '1,021 MW', '3,383 MW',  'Final concessions only — flat wind'],
    ['Base case 2027',       '3,242 MW', '1,867 MW', '5,109 MW',  'Wind growth accelerates'],
    ['Base case 2028',       '3,337 MW', '1,867 MW', '5,203 MW',  'Marginal solar increase'],
    ['Full pipeline 2026',   '9,838 MW', '7,281 MW', '17,120 MW', 'All COES pre-approved projects'],
    ['Full potential 2030',  '15,185 MW','9,344 MW', '24,529 MW', '56% solar / 44% wind split'],
]
y = 174
for ri, row in enumerate(rows):
    row_bg(d, 50, y, W-100, 46, ri%2==0)
    for i, (cx, cw, cell) in enumerate(zip(col_x, col_w, row)):
        col = TEAL if i==0 else GREY_L
        d.text((cx+10, y+12), cell, font=get_font(15), fill=col)
    y += 46

d.rectangle([50, y+10, W-50, y+12], fill=DIVIDER)
y += 22

# Regions
d.text((50, y+10), 'KEY DEVELOPMENT REGIONS', font=get_font(16, True), fill=TEAL)
d.text((1000, y+10), 'CRITICAL MARKET DYNAMIC', font=get_font(16, True), fill=AMBER)

regions = [
    ('SOLAR', 'Ica — Prime irradiance, flat terrain, grid access\nArequipa/Moquegua — GHI >6.5 kWh/m²/day\nLima Periphery — Smaller, near demand'),
    ('WIND',  'Piura — Strongest resource, existing hub\nIca/Lambayeque — Secondary corridors\nAncash/La Libertad — Emerging sites'),
]
rx = 50
for tech, desc in regions:
    card(d, rx, y+35, 440, 145, NAVY_L, TEAL)
    d.text((rx+16, y+50), tech, font=get_font(18, True), fill=TEAL)
    for i, line in enumerate(desc.split('\n')):
        d.text((rx+16, y+82+i*28), line, font=get_font(14), fill=GREY_L)
    rx += 460

card(d, 1000, y+35, W-1050, 145, NAVY_L, AMBER)
d.text((1016, y+50), '114 COES-approved projects  ·  Only 19 have MINEM final concession', font=get_font(14, True), fill=AMBER)
d.text((1016, y+82), '95 projects = 21,142 MW still awaiting authorisation to build', font=get_font(14), fill=GREY_L)
d.text((1016, y+108), 'Permitting backlog is the primary constraint on procurement volume', font=get_font(14), fill=GREY_L)

footer_bar(d, 3)
save(img, 3, 'market_overview')

# ── SLIDE 4: BOS SOLAR ────────────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Balance of System — Solar PV', 'Component Breakdown, Cost Structure & Supply Origin')

cols = ['BOS Component', '% CAPEX', 'Local/Import', 'Key Suppliers']
col_x = [50, 500, 660, 880]
col_w = [440, 150, 210, 860]
y = 130
d.rectangle([50, y, W-50, y+40], fill=TEAL)
for cx, col in zip(col_x, cols):
    d.text((cx+8, y+10), col, font=get_font(15, True), fill=WHITE)

bos_rows = [
    ['PV Modules (reference)',     '30–35%', '100% Import', 'LONGi, JA Solar, Trina, JinkoSolar'],
    ['Inverters (string/central)', '7–10%',  '95% Import',  'Huawei, SMA, Sungrow, ABB'],
    ['Mounting / Trackers',        '10–14%', '70% Import',  'Nextracker, Array Tech, Soltec'],
    ['DC & AC Cabling',            '5–7%',   '40–50% Local','Indeco (Nexans), CEP, Phelps Dodge'],
    ['MV/HV Transformers',         '6–8%',   '65% Import',  'ABB/Hitachi Energy, Siemens'],
    ['Switchgear & Protection',    '4–6%',   '70% Import',  'Schneider Electric, ABB, Eaton'],
    ['SCADA & Monitoring',         '1–2%',   '90% Import',  'Siemens, GE, vendor-specific'],
    ['Civil Works (foundations)',  '8–12%',  '85–90% Local','Cosapi, JJC Contratistas, Mota-Engil'],
    ['Grid Connection (to POI)',   '5–15%',  'Mixed',       'REP, ISA Peru, Cobra (ACS Group)'],
]
y = 170
for ri, row in enumerate(bos_rows):
    row_bg(d, 50, y, 1700, 43, ri%2==0)
    for i, (cx, cw, cell) in enumerate(zip(col_x, col_w, row)):
        col = TEAL if i==0 else GREY_L
        d.text((cx+8, y+11), cell, font=get_font(14), fill=col)
    y += 43

# Cost bar chart (right)
d.text((1780, 130), 'COST SPLIT (%)', font=get_font(14, True), fill=TEAL)
bar_data = [
    ('PV Modules',    32, TEAL),
    ('Inverters',      9, AMBER),
    ('Trackers',      12, GREEN),
    ('Cabling',        6, TEAL),
    ('Transformers',   7, AMBER),
    ('Civil Works',   10, GREEN),
    ('Grid/Other',    10, GREY_M),
    ('Switchgear+',    6, (155,89,182)),
]
by = 155
for lbl, pct, col in bar_data:
    bw = int(120 * pct / 35)
    d.rectangle([1780, by, 1780+bw, by+28], fill=col)
    d.text((1786+bw, by+6), f'{lbl} {pct}%', font=get_font(13), fill=GREY_L)
    by += 38

d.rectangle([50, y+8, W-50, y+10], fill=DIVIDER)
d.text((50, y+18), '⚠  FEOC/ESG NOTE: Huawei ~40% inverter share in Peru. European lenders increasingly scrutinise Xinjiang-linked supply chains. Document due diligence.',
       font=get_font(14), fill=AMBER)
d.text((50, y+48), 'All-in solar CAPEX: $700–900/kW  ·  BOS = 40–55% of CAPEX  ·  Grid connection highly variable ($30–150+/kW)',
       font=get_font(14, True), fill=TEAL)

footer_bar(d, 4)
save(img, 4, 'bos_solar')

# ── SLIDE 5: BOP WIND ─────────────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Balance of Plant — Wind', 'Component Breakdown, OEM Landscape & Cost Structure')

cols = ['BOP Component', '% CAPEX', 'Local/Import', 'Key Suppliers']
col_x = [50, 480, 640, 860]
y = 130
d.rectangle([50, y, 1700, y+40], fill=TEAL)
for cx, col in zip(col_x, cols):
    d.text((cx+8, y+10), col, font=get_font(15, True), fill=WHITE)

bop_rows = [
    ['Wind Turbines (reference)',   '40–50%', '100% Import',   'Vestas, SGRE, GE Vernova, Goldwind'],
    ['Civil (roads, pads, founds)', '10–15%', '85–90% Local',  'Cosapi, Graña y Montero, JJC'],
    ['Internal Collection Grid',    '5–8%',   '50% Local',     'Indeco, Phelps Dodge'],
    ['Onsite Substation',           '4–6%',   '65% Import',    'ABB/Hitachi, Siemens, Schneider'],
    ['Grid Connection (to POI)',    '5–20%',  'Mixed',         'REP, ISA Peru, Cobra (ACS)'],
    ['SCADA & Communications',      '1–2%',   '90% Import',    'OEM-integrated (Vestas/SGRE)'],
    ['O&M Facility & Access Roads', '1–3%',   '100% Local',    'Local civil contractors'],
]
y = 170
for ri, row in enumerate(bop_rows):
    row_bg(d, 50, y, 1640, 46, ri%2==0)
    for i, cx in enumerate(col_x):
        col = TEAL if i==0 else GREY_L
        d.text((cx+8, y+12), row[i], font=get_font(14), fill=col)
    y += 46

# OEM table (right)
d.text((1720, 130), 'TURBINE OEM LANDSCAPE', font=get_font(14, True), fill=TEAL)
d.rectangle([1720, 155, W-20, 195], fill=TEAL)
for i, col in enumerate(['OEM', 'Origin', 'FEOC']):
    d.text((1720+i*145+8, 163), col, font=get_font(13, True), fill=WHITE)

oems = [
    ('Vestas',        'Denmark', 'Low',  GREEN),
    ('Siemens Gamesa','Spain/DE','Low',  GREEN),
    ('GE Vernova',    'US',      'Low',  GREEN),
    ('Goldwind',      'China',   'HIGH', RED),
    ('Envision',      'China',   'HIGH', RED),
]
oy = 195
for i, (name, origin, feoc, col) in enumerate(oems):
    row_bg(d, 1720, oy, W-1740, 42, i%2==0)
    d.text((1728, oy+10), name,   font=get_font(13), fill=TEAL)
    d.text((1873, oy+10), origin, font=get_font(13), fill=GREY_L)
    d.rectangle([2018, oy+6, 2118, oy+36], fill=col)
    d.text((2022, oy+10), feoc, font=get_font(12, True), fill=WHITE)
    oy += 42

d.rectangle([50, y+10, W-50, y+12], fill=DIVIDER)
principles = [
    '→  Split turbine supply from BOP civil — reduces FX exposure and supports social licence',
    '→  SCADA: keep OEM-integrated — separation creates interface risk and voids turbine warranties',
    '→  Grid connection: owner-procure directly with REP/ISA — EPC wrapping adds premium with no value',
    '→  Secure Cosapi/JJC early — capacity constraints as pipeline accelerates from 2026',
]
py = y+22
for p in principles:
    d.text((60, py), p, font=get_font(15), fill=GREY_L)
    py += 34

d.text((50, py+8), 'All-in wind CAPEX: $1,100–1,400/kW  ·  BOP = 30–45% of CAPEX  ·  Coastal/flat sites at lower end',
       font=get_font(14, True), fill=TEAL)

footer_bar(d, 5)
save(img, 5, 'bop_wind')

# ── SLIDE 6: SUPPLY CHAIN ─────────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Supply Chain Analysis', 'Import Dependency, Logistics & Lead Times')

d.text((50, 120), 'EQUIPMENT IMPORT DEPENDENCY', font=get_font(16, True), fill=TEAL)
import_items = [
    ('PV Modules',         100, RED),
    ('Wind Turbines',      100, RED),
    ('Inverters',           95, RED),
    ('MV/HV Transformers',  70, AMBER),
    ('Tracker Systems',     70, AMBER),
    ('Switchgear',          70, AMBER),
    ('HV Cabling',          60, AMBER),
    ('DC/AC Cabling',       55, (243,213,0)),
    ('Civil Works',         12, GREEN),
    ('Concrete/Aggregate',   5, GREEN),
]
BAR_MAX = 580; bx = 330; by = 148
for item, pct, col in import_items:
    bw = int(BAR_MAX * pct / 100)
    d.text((bx-280, by+6), item, font=get_font(15), fill=GREY_L)
    d.rectangle([bx, by, bx+bw, by+28], fill=col)
    d.text((bx+bw+10, by+6), f'{pct}%', font=get_font(14, True), fill=col)
    by += 40

# Legend
for i, (col, label) in enumerate([(RED,'Critical import'), (AMBER,'Moderate import'), (GREEN,'Primarily local')]):
    d.rectangle([50+i*320, 558, 80+i*320, 578], fill=col)
    d.text((90+i*320, 558), label, font=get_font(14), fill=GREY_L)

d.rectangle([50, 595, W-50, 597], fill=DIVIDER)

# Logistics table
d.text((1060, 120), 'LOGISTICS & LEAD TIMES', font=get_font(16, True), fill=TEAL)
d.rectangle([1060, 148, W-50, 188], fill=TEAL)
for i, col in enumerate(['Item', 'Lead Time', 'Key Risk']):
    d.text((1068+i*320, 158), col, font=get_font(14, True), fill=WHITE)

log_rows = [
    ('Turbines (blades/towers)', '12–18 months', 'Port handling, convoy'),
    ('HV Transformers',          '10–14 months', '⚠ Global shortage 2024–26'),
    ('MV Switchgear',            '6–10 months',  'Tariff disruption risk'),
    ('Tracker Systems',          '4–6 months',   'Low risk'),
    ('Inverters',                '3–5 months',   'Low — high supply'),
    ('PV Modules',               '2–4 months',   'Low risk'),
    ('HV Cabling',               '4–8 months',   'Capacity constraints'),
    ('Civil Equipment',          '1–3 months',   'Generally available'),
]
ly = 188
for i, (item, lt, risk) in enumerate(log_rows):
    row_bg(d, 1060, ly, W-1110, 46, i%2==0)
    d.text((1068, ly+12), item, font=get_font(13), fill=TEAL)
    d.text((1388, ly+12), lt,   font=get_font(13), fill=GREY_L)
    col = RED if '⚠' in risk else GREY_L
    d.text((1708, ly+12), risk, font=get_font(13), fill=col)
    ly += 46

# Callout boxes
boxes = [
    (50,  612, 570, 110, AMBER, 'CUSTOMS', 'FTAs with China, US & EU. Duties 0–6% on RE equipment. Clearance variance 30–90 days. Use specialist customs broker.'),
    (640, 612, 570, 110, TEAL,  'CURRENCY','Equipment: USD. Civil/labour: PEN. Natural hedge available — structure BOP civil in PEN with CPI adjustment.'),
    (1230,612, 640, 110, RED,   'GRID/PORT','HV transformer shortage is GLOBAL. Callao handles oversized cargo. Grid POI congestion adds 6–12 month risk.'),
]
for bx, by, bw, bh, col, title, body in boxes:
    d.rectangle([bx, by, bx+bw, by+bh], fill=NAVY_L)
    d.rectangle([bx, by, bx+bw, by+6], fill=col)
    d.text((bx+12, by+14), title, font=get_font(14, True), fill=col)
    lines = body.split('. ')
    for i, line in enumerate(lines[:2]):
        d.text((bx+12, by+40+i*26), line.strip(), font=get_font(13), fill=GREY_L)

footer_bar(d, 6)
save(img, 6, 'supply_chain')

# ── SLIDE 7: RISK REGISTER ────────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Procurement Risk Register', 'BOS & BOP — Wind & Solar Projects, Peru')

cols = ['Risk', 'Severity', 'Likelihood', 'Impact', 'Mitigation']
col_x = [50, 540, 720, 900, 1240]
d.rectangle([50, 130, W-50, 170], fill=TEAL)
for cx, col in zip(col_x, cols):
    d.text((cx+8, 140), col, font=get_font(15, True), fill=WHITE)

risks = [
    ('Grid connection delay',       'HIGH',   'HIGH',   'Cost overrun 15–25%; schedule slip 6–12m',  'Owner-procure; early COES/REP engagement; 20% contingency'),
    ('HV transformer shortage',     'HIGH',   'HIGH',   'Critical path; 10–14 month lead time',       'Order at FID; frame agreements ABB/Hitachi/Siemens'),
    ('Civil contractor capacity',   'MED',    'HIGH',   'Price escalation; schedule risk',            'Pre-qualify Cosapi/JJC; early works contract'),
    ('PPA non-availability',        'HIGH',   'MED',    'Project non-bankable; spend at risk',        'Gate procurement to PPA milestone; NTP structure'),
    ('PEN currency inflation',      'MED',    'MED',    'Civil BOP cost overrun',                     'CPI adjustment clauses; FX hedging for equipment'),
    ('Customs clearance delay',     'MED',    'MED',    '30–90 day variance impacts schedule',        'Specialist broker; buffer lead times'),
    ('MINEM permitting delay',      'HIGH',   'HIGH',   'Procurement wasted if concession withheld',  'Do not commit spend until final concession confirmed'),
    ('Single-source turbine OEM',   'MED',    'LOW',    'No competitive tension; warranty risk',      'Dual-source short-list at FID'),
]
sev_col = {'HIGH': RED, 'MED': AMBER, 'LOW': GREEN}
ry = 170
for ri, (risk, sev, lik, impact, mit) in enumerate(risks):
    row_bg(d, 50, ry, W-100, 52, ri%2==0)
    d.text((58, ry+14), risk, font=get_font(14), fill=TEAL)
    for ci, (val, cx) in enumerate([(sev, 540), (lik, 720)]):
        col = sev_col.get(val, GREY_L)
        d.rectangle([cx+8, ry+10, cx+168, ry+42], fill=col)
        d.text((cx+20, ry+16), val, font=get_font(13, True), fill=WHITE)
    d.text((908, ry+8),  impact, font=get_font(12), fill=GREY_L)
    d.text((1248, ry+8), mit,   font=get_font(12), fill=GREY_L)
    ry += 52

footer_bar(d, 7)
save(img, 7, 'risk_register')

# ── SLIDE 8: RECOMMENDATIONS ─────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Strategic Procurement Recommendations', 'Statkraft Peru — BOS/BOP Positioning')

recs = [
    (TEAL,  '01', 'Establish Market Intelligence Now',       'Map active EPC contractors and suppliers across Peru\'s 20 GW pipeline. Information advantage = commercial leverage before the market tightens.'),
    (AMBER, '02', 'Pre-Qualify & Reserve Civil Capacity',    'Issue pre-qualification RFQs to Cosapi, JJC and Mota-Engil now. Consider early works contracts to secure scheduling priority.'),
    (GREEN, '03', 'Frame Agreements: Transformers & Trackers','HV transformers = 10–14 month critical path with global shortage. Nextracker/Array Tech engagement yields better pricing and delivery priority.'),
    (TEAL,  '04', 'Owner-Procure Grid Connection',           'Do not wrap grid in EPC package. Peru\'s transmission bottleneck means EPC adds risk premium. Engage REP/ISA/COES directly. Budget 15–20% contingency.'),
    (AMBER, '05', 'Gate Procurement to Concession Milestones','95 of 114 projects lack final MINEM concession. Committed procurement spend before concession = capital at risk. NTP-linked structure required.'),
    (RED,   '06', 'Address FEOC/ESG Supply Chain Risk',      'Chinese OEMs dominate modules and inverters. European lenders require due diligence. Document Xinjiang attestations in supplier pre-qualification.'),
]
rx, ry = 50, 130
for i, (col, num, title, body) in enumerate(recs):
    if i > 0 and i % 2 == 0:
        ry += 210
        rx = 50
    card(d, rx, ry, 880, 195, NAVY_L, col)
    d.rectangle([rx+12, ry+12, rx+78, ry+78], fill=col)
    d.text((rx+20, ry+22), num, font=get_font(32, True), fill=WHITE)
    d.text((rx+96, ry+16), title, font=get_font(17, True), fill=col)
    lines = body.split('. ')
    ty = ry+56
    for line in lines[:3]:
        d.text((rx+96, ty), line.strip(), font=get_font(14), fill=GREY_L)
        ty += 34
    rx += 940

footer_bar(d, 8)
save(img, 8, 'recommendations')

# ── SLIDE 9: SCORECARD ────────────────────────────────────────────────────────
img, d = new_slide()
header(d, 'Peru BOS/BOP — Market Scorecard', 'Summary Assessment for Statkraft Procurement Strategy')

scores = [
    ('Market Growth Potential',     5, GREEN,  '20 GW pipeline; government commitment; 15%+ CAGR'),
    ('BOS Supply Chain Maturity',   3, AMBER,  'Import-dependent but established; strong local civil base'),
    ('BOP Contractor Capability',   4, TEAL,   'Strong civil (Cosapi, JJC); electrical contractors thinner'),
    ('Grid Infrastructure',         2, RED,    'Transmission bottleneck; $430M plan insufficient for pipeline'),
    ('Offtake / PPA Maturity',      2, RED,    'Underdeveloped; Law 32249 improving but regulation pending'),
    ('Regulatory Environment',      3, AMBER,  'Improving direction; MINEM concession queue a constraint'),
    ('Logistics Accessibility',     3, AMBER,  'Callao functional; remote site access variable'),
    ('Procurement Complexity',      1, RED,    'HIGH — import dependency, grid risk, contractor capacity, FX'),
]
sy = 130
for label, score, col, comment in scores:
    d.rectangle([50, sy, W-50, sy+88], fill=NAVY_L)
    d.rectangle([50, sy, 62, sy+88], fill=col)
    d.text((75, sy+10), label, font=get_font(18, True), fill=WHITE)
    for dot in range(5):
        fill = col if dot < score else DIVIDER
        d.rectangle([75+dot*52, sy+48, 75+dot*52+40, sy+75], fill=fill)
    d.text((360, sy+48), f'{score}/5', font=get_font(20, True), fill=col)
    d.text((460, sy+10), comment, font=get_font(15), fill=GREY_L)
    d.text((460, sy+52), '—', font=get_font(14), fill=DIVIDER)
    sy += 96

d.rectangle([50, sy+4, W-50, sy+6], fill=DIVIDER)
card(d, 50, sy+12, W-100, 75, NAVY_L, TEAL, 12)
d.text((80, sy+22), 'OVERALL VERDICT', font=get_font(16, True), fill=TEAL)
d.text((80, sy+52), 'Strong market opportunity with HIGH procurement complexity. Early movers who pre-qualify contractors, lock frame agreements and secure grid connections will win. The window is now.',
       font=get_font(15), fill=GREY_L)

footer_bar(d, 9)
save(img, 9, 'scorecard')

print('\nAll slides rendered successfully.')
print(f'Output: {OUT}')
