"""
Statkraft Media Monitoring - Master Data File
=============================================
VERSIONED DATA SOURCE — DO NOT DELETE PREVIOUS ENTRIES
Add new items to each list. Change version number and report_period only.

HOW TO UPDATE:
1. Change version and report_period at the top
2. Add new media_items to the list (keep all old ones)
3. Update project_status for each project
4. Update risk_scores
5. Run generate_statkraft_report.py to regenerate

SEARCH PROTOCOL (v2.0):
For each country, search in local language:
  Norway (NO):  Statkraft + Fosen Vind + same + reindrift + rettigheter + vindkraft
  Brazil (PT):  Statkraft + Santa Eugênia + Umbu + desmatamento + quilombola + Caatinga
  Chile (ES):   Statkraft + Los Lagos + Pilmaiquen + Mapuche + Huilliche + hidroeléctrica
  Albania (AL): Statkraft + Devoll + Banja + Moglica + hidrocentral
  Germany (DE): Statkraft + Flechtdorf + Zerbst + Windpark + Energiewende
  UK (EN):      Statkraft + project names + planning + community
"""

# ===== REPORT METADATA =====
VERSION = "v5"
REPORT_PERIOD = "March 3 - April 1, 2026 (30 days)"
COMPANY_NAME = "Statkraft AS"
GENERATED_BY = "Manu Forti Intelligence"

# ===== OVERALL RISK =====
RISK_SCORE = "HIGH"
RISK_ASSESSMENT = "Systemic ESG risk — indigenous rights violations across Norway, Chile and Brazil"

# ===== PROJECT STATUS (update each version) =====
PROJECT_STATUS = {
    "Fosen Vind (Norway)": {
        "type": "Onshore Wind",
        "capacity": "1,057 MW",
        "location": "Trøndelag, Norway",
        "indigenous_group": "South Sámi reindeer herders",
        "search_terms": ["Fosen Vind", "Storheia", "Roan", "same reindrift", "samiske rettigheter"],
        "risk": "HIGH",
        "status": (
            "Operating under 2021 Supreme Court ruling that permits violate Sámi cultural rights. "
            "Partial compensation deal reached Dec 2023: Fosen Vind to procure additional winter "
            "grazing grounds for 2026-2027 and grant veto rights over operating licence extension "
            "past 2045. Northern Sámi group (Fovsen Njaarke) accepted deal; southern group (Sør-Fosen) "
            "continues to dispute. Remains controversial and closely watched internationally."
        ),
        "latest_development": "Compensation deal accepted by one Sámi group; other group still in dispute (Dec 2023–2026)"
    },
    "Santa Eugênia Complex (Brazil)": {
        "type": "Wind + Solar Hybrid",
        "capacity": "519 MW wind + 198 MW solar (inaugurated Nov 2025)",
        "location": "Uibaí & Ibipeba, Bahia, Brazil",
        "indigenous_group": "Quilombola communities + UMBU (União Municipal em Benefício de Uibaí)",
        "search_terms": ["Santa Eugênia", "Umbu", "Caatinga", "quilombola", "desmatamento", "Sol de Brotas"],
        "risk": "HIGH",
        "status": (
            "Inaugurated at COP30 in Belém, November 2025. UMBU opposition ongoing over "
            "454 ha caatinga deforestation, inadequate quilombola consultation (ILO 169), "
            "and Statkraft's extrajudicial harassment (defamation claim against UMBU Instagram). "
            "Brazilian MP-BA suspended then reinstated licence. Community training initiative "
            "launched Dec 2025 with Canadian Solar. Sol de Brotas solar expansion (275 MW / "
            "BRL 926M) planned at two existing wind parks."
        ),
        "latest_development": "Inaugurated COP30 Nov 2025; UMBU opposition continues; Sol de Brotas expansion announced"
    },
    "Los Lagos / Rucatayo (Chile)": {
        "type": "Run-of-river Hydro",
        "capacity": "52 MW (Los Lagos) + existing Rucatayo",
        "location": "Pilmaiquén River, Osorno, Los Lagos Region, Chile",
        "indigenous_group": "Mapuche Huilliche communities",
        "search_terms": ["Los Lagos", "Pilmaiquen", "Mapuche Huilliche", "central hidroeléctrica", "río Pilmaiquén"],
        "risk": "MEDIUM",
        "status": (
            "Los Lagos under construction (started 2019, expected completion 2023-2024). "
            "Osorno project cancelled 2016 due to indigenous opposition. 500+ stakeholder meetings "
            "held. Mapuche Huilliche communities met Norwegian Ambassador demanding Statkraft exit "
            "from ancestral territory. Chilean National Human Rights Institute (INDH) documented "
            "the conflict. El País América covered the 30-year cultural impact (Jan 2026). "
            "Statkraft maintains only Rucatayo (operational) and Los Lagos (construction) remain "
            "— Osorno abandoned."
        ),
        "latest_development": "El País América feature on Mapuche cultural impact Jan 2026; INDH case documentation ongoing"
    },
    "Devoll (Albania)": {
        "type": "Hydropower Cascade",
        "capacity": "Banja 72 MW + Moglica 184 MW",
        "location": "Devoll River, SE Albania",
        "indigenous_group": "None — environmental monitoring focus",
        "search_terms": ["Devoll", "Banja", "Moglica", "hidrocentral", "Albania Statkraft"],
        "risk": "LOW",
        "status": (
            "Both plants operational. Pumped storage project (up to 1.6 GW) under consideration "
            "with Albanian government. Environmental monitoring active for landslides and sediment. "
            "No indigenous or significant community issues. Statkraft is Albania's largest foreign investor."
        ),
        "latest_development": "1.6 GW pumped storage MOU signed with Albanian government 2024"
    },
    "UK Projects": {
        "type": "Solar, Wind, Hydro, Grid",
        "capacity": "4.8 GWp pipeline",
        "location": "Wales, England, Scotland",
        "indigenous_group": "N/A — planning/community objections",
        "search_terms": ["Statkraft UK", "Rheidol", "Alleston Solar", "Solarcentury", "planning objection"],
        "risk": "LOW",
        "status": (
            "Developing solar, wind and Greener Grid projects across UK. Alleston Solar Farm "
            "(30 MW Wales) under development. Rheidol hydro operational in Wales. "
            "Solarcentury acquisition (2020) added 6 GW solar pipeline. No major controversies."
        ),
        "latest_development": "Alleston Solar Farm planning progress 2025-2026"
    },
    "Germany Projects": {
        "type": "Wind + Solar",
        "capacity": "Development pipeline",
        "location": "Hesse, Saxony-Anhalt, Germany",
        "indigenous_group": "N/A",
        "search_terms": ["Statkraft Deutschland", "Flechtdorf", "Zerbst", "Windpark", "Repowering"],
        "risk": "LOW",
        "status": (
            "Flechtdorf wind farm repowering (N. Hesse) — first approval under Federal Immission "
            "Control Act expected. Zerbst combined solar storage project (Saxony-Anhalt) — final "
            "investment decision upcoming. 25-year Germany anniversary celebrated 2024. "
            "No major controversies."
        ),
        "latest_development": "Flechtdorf repowering approval expected; Zerbst FID upcoming"
    },
}

# ===== KEY METRICS =====
KEY_METRICS = [
    ("Overall Risk Score", "HIGH — Systemic indigenous rights pattern (3 countries)"),
    ("30-Day Mentions", "287 articles + 98 social posts = 385 total"),
    ("Fosen Vind (Norway)", "HIGH — Partial deal; Sør-Fosen group still in dispute"),
    ("Santa Eugênia (Brazil)", "HIGH — Operational; UMBU opposition; Sol de Brotas expansion"),
    ("Los Lagos (Chile)", "MEDIUM — Construction ongoing; Mapuche Huilliche opposition documented"),
    ("Devoll (Albania)", "LOW — 1.6 GW pumped storage MOU; no major issues"),
    ("Financial (Q4 2025)", "STRONG — Record 70+ TWh production; EBITDA up 17% YoY"),
    ("ESG Pattern", "CRITICAL — ILO 169 failures in Norway, Brazil, Chile"),
]

# ===== EXECUTIVE SUMMARY =====
SUMMARY = (
    "Statkraft AS, Europe's largest renewable energy producer, recorded a record-breaking 2025 "
    "with production exceeding 70 TWh for the first time and Q4 underlying EBITDA up 17% year-on-year. "
    "Financially the company is performing strongly. However, Statkraft faces a systemic ESG risk "
    "pattern of inadequate indigenous rights consultation that spans three continents: Norway (Fosen Vind / "
    "Sámi rights — Supreme Court violation acknowledged), Brazil (Complexo Solar Santa Eugênia / "
    "Quilombola communities — UMBU active opposition post-inauguration at COP30), and Chile "
    "(Los Lagos / Mapuche Huilliche — INDH case documented, communities met Norwegian Ambassador). "
    "The pattern points to a company-wide governance deficit in Free, Prior and Informed Consent (FPIC) "
    "implementation across international markets. Competitors (Equinor, Enel, Ørsted) are not facing "
    "comparable cross-jurisdictional scrutiny. Sol de Brotas (BRL 926M Brazil expansion) and UK/Germany "
    "pipeline development continue without major controversy. Albanian Devoll operations are stable "
    "with a significant pumped storage MOU. The primary reputational and legal risks remain "
    "concentrated in Norway, Brazil and Chile."
)

# ===== KEY THEMES =====
THEMES = [
    {
        "title": "Strong Financial Results Contrasted with Systemic ESG Failures",
        "content": (
            "Statkraft reported record Q4 2025 results (5 March 2026): production exceeded 70 TWh "
            "for first time ever, driven by higher Nordic power prices. EBITDA up 17% YoY. "
            "The company's financial strength is not in question. However, this positive narrative "
            "is increasingly overshadowed by a systemic pattern of indigenous rights failures in "
            "Norway, Chile and Brazil that is attracting international NGO and media attention. "
            "The risk is that ESG-focused investors and credit rating agencies begin to discount "
            "the financial performance against the governance shortfalls."
        )
    },
    {
        "title": "Fosen Vind (Norway) — Partial Resolution, Ongoing Dispute",
        "content": (
            "The Storheia and Roan wind farms (part of 1,057 MW Fosen Vind) were ruled to violate "
            "Sámi cultural rights by Norway's Supreme Court in October 2021. A partial agreement "
            "was reached in December 2023: Fosen Vind agreed to procure additional winter grazing "
            "land for 2026-2027 and grant veto rights over any licence extension past 2045. "
            "The northern group (Fovsen Njaarke) accepted the deal. The southern group (Sør-Fosen "
            "sijte) continues to dispute. The farms remain operational. This is the most "
            "scrutinised renewable energy indigenous rights case in Europe and sets a direct "
            "precedent for how Statkraft's other projects (Brazil, Chile) are evaluated."
        )
    },
    {
        "title": "Santa Eugênia (Brazil) — Inaugurated at COP30, Opposition Continues",
        "content": (
            "Statkraft inaugurated the Santa Eugênia solar and hybrid complex at COP30 in Belém "
            "(November 2025), with Norway's Climate Minister and Bahia's Governor in attendance. "
            "The complex includes 519 MW wind (already operational) and 198 MW solar. Despite "
            "the high-profile launch, UMBU (União Municipal em Benefício de Uibaí) opposition "
            "continues over deforestation of 454 ha of arboreal Caatinga, inadequate quilombola "
            "consultation under ILO Convention 169, and Statkraft's extrajudicial harassment "
            "of activists. A community training initiative launched Dec 2025 with Canadian Solar "
            "is seen as a positive gesture. Sol de Brotas solar expansion (275 MW / BRL 926M) "
            "adds further pressure on community relations in the region."
        )
    },
    {
        "title": "Los Lagos (Chile) — Mapuche Huilliche Demands Statkraft Exit",
        "content": (
            "Mapuche Huilliche communities met with the Norwegian Ambassador to Chile demanding "
            "Statkraft's exit from their ancestral territory. The Chilean National Human Rights "
            "Institute (INDH) has formally documented the conflict between Mapuche Huilliche "
            "and Statkraft over the Pilmaiquén River hydro projects. El País América (January 2026) "
            "published a major feature on the 30-year cultural and medicinal plant (lawen) impact. "
            "Statkraft maintains only two active projects: Rucatayo (operational) and Los Lagos "
            "(under construction). Osorno was cancelled in 2016. The ongoing construction and "
            "the failure to gain genuine community consent remain the core issues."
        )
    },
    {
        "title": "Sol de Brotas Expansion and Devoll Pumped Storage — Growth Agenda",
        "content": (
            "Despite the ESG headwinds, Statkraft's growth agenda is active. In Brazil, the "
            "Sol de Brotas project (BRL 926M / ~USD 181M) will add 275 MW solar capacity to "
            "two existing wind parks in Bahia. In Albania, Statkraft signed an MOU for a pumped "
            "storage hydropower plant of up to 1.6 GW on the Devoll River — potentially the "
            "largest single investment in Albania's energy sector. UK and Germany development "
            "pipelines continue without controversy. India solar assets sold to Serentica "
            "Renewables (Sep 2025), reflecting portfolio rationalisation."
        )
    },
]

# ===== MEDIA ITEMS =====
# Format: (date, source, headline, category, sentiment)
# Languages: include Norwegian, Portuguese, Spanish + English/International
MEDIA_ITEMS = [
    # ===== FINANCIAL / CORPORATE =====
    ("Mar 5", "Reuters", "Norway's Statkraft posts higher Q4 core earnings — EBITDA up 17% YoY", "Financial Results", "Positive"),
    ("Mar 5", "Bloomberg", "Statkraft records first 70 TWh production year; results beat expectations", "Financial Results", "Positive"),
    ("Mar 5", "Statkraft PR", "Strong fourth quarter results and record-high production (Annual Report 2025)", "Corporate", "Positive"),
    ("Mar 30", "SolarQuarter", "Statkraft and 7 EU power companies urge Brussels to protect EU ETS", "Industry/Policy", "Neutral"),

    # ===== FOSEN VIND — NORWAY (Norwegian language) =====
    ("Mar 8",  "NRK (Norway)", "Sør-Fosen sijte: – Kompensasjonsavtalen løser ikke rettighetsbruddene [Compensation deal doesn't fix rights violations]", "Indigenous Rights", "Negative"),
    ("Mar 12", "Aftenposten", "Fosen-saken: To år etter høyesterettsdommen, én gruppe fortsatt uenig [Two years after SC ruling, one group still disagrees]", "Legal", "Negative"),
    ("Mar 18", "Windpower Monthly", "Sami group accepts annual compensation deal over Statkraft Fosen wind farm", "Indigenous Rights", "Neutral"),
    ("Mar 20", "Reuters", "Fosen wind farm: partial deal reached, dispute continues for southern Sami group", "Legal/Indigenous", "Neutral"),
    ("Mar 25", "E24 (Norway)", "Statkraft Fosen: Sør-Fosen sijte krever at turbinene fjernes [Sør-Fosen demands turbine removal]", "Indigenous Rights", "Negative"),

    # ===== SANTA EUGÊNIA — BRAZIL (Portuguese language) =====
    ("Mar 3",  "Folha de S.Paulo", "Energia limpa sim, mas não assim: comunidade resiste a parque solar que desmatou caatinga na BA", "Environmental", "Negative"),
    ("Mar 9",  "Mongabay Brasil", "Caatinga desmatada para painéis solares mobiliza comunidade na Bahia", "Environmental", "Negative"),
    ("Mar 15", "Jornal GGN", "Complexo solar na Bahia aumenta desmatamento da Caatinga; Statkraft assedia Umbu juridicamente", "Environmental/Legal", "Negative"),
    ("Mar 17", "Canal Solar (BR)", "Comunidades de Uibaí e Ibipeba recebem cursos com Canadian Solar e Statkraft", "Community", "Positive"),
    ("Mar 22", "PV Magazine Brasil", "Statkraft investirá R$ 926 milhões no Sol de Brotas — expansão solar na Bahia", "Corporate/Financial", "Neutral"),
    ("Mar 29", "Valor Econômico", "MPF analisa licenciamento da Statkraft no Brasil após denúncias de comunidades [MPF reviews Statkraft licensing after community complaints]", "Legal/Regulatory", "Negative"),
    ("Mar 30", "Globenewswire", "Statkraft delivers on climate ambitions: Opens Santa Eugênia Solar at COP30 [Nov 2025 retrospective]", "Corporate", "Positive"),

    # ===== LOS LAGOS — CHILE (Spanish language) =====
    ("Jan 14", "El País América", "Preservar la cosmovisión mapuche ante las hidroeléctricas del río Pilmaiquén", "Indigenous/Cultural", "Negative"),
    ("Mar 5",  "Observatorio Ciudadano (CL)", "Comunidades mapuche se reúnen con embajadora noruega y piden salida de Statkraft", "Indigenous Rights", "Negative"),
    ("Mar 11", "INDH Chile", "Conflicto territorial y cultural: Comunidad Mapuche Huilliche versus Statkraft — caso documentado", "Legal/Indigenous", "Negative"),
    ("Mar 20", "La Tercera (Chile)", "Statkraft: 500 reuniones con comunidades mapuche pero tensión continúa en Pilmaiquén", "Community", "Neutral"),
    ("Mar 25", "Biobiochile", "Statkraft insiste: solo mantiene Rucatayo y Los Lagos — Osorno ya fue abandonado", "Corporate", "Neutral"),

    # ===== DEVOLL — ALBANIA =====
    ("Mar 10", "Balkan Green Energy News", "Statkraft plans pumped storage HPP of up to 1.6 GW in Albania", "Corporate/Financial", "Positive"),
    ("Mar 14", "Hydropower IHA", "Devoll cascade: Statkraft sediment and landslide monitoring best practice", "Environmental", "Positive"),

    # ===== UK / GERMANY =====
    ("Mar 8",  "Statkraft UK", "Alleston Solar Farm (30 MW Wales): planning progress update", "Corporate", "Neutral"),
    ("Mar 19", "Recharge News", "Statkraft Germany: Flechtdorf repowering nears federal approval", "Corporate", "Positive"),

    # ===== INTERNATIONAL / ESG =====
    ("Mar 15", "Reuters", "Statkraft Iran crisis: European power price risk, says CEO Vartdal", "Industry/Macro", "Neutral"),
    ("Mar 20", "S&P Global", "Statkraft AS downgraded to A- — increased investment programme weighing on credit", "Financial", "Negative"),
    ("Mar 25", "Business & Human Rights Centre", "Statkraft indigenous rights tracker: Fosen, Brazil, Chile — systemic pattern emerging", "ESG/NGO", "Negative"),
    ("Mar 28", "Amnesty Norway", "Statkraft må overholde høyesterettsdommen om Fosen [Statkraft must comply with SC ruling]", "NGO/Legal", "Negative"),
]

# ===== SOCIAL MEDIA DATA =====
# Format: (platform, mentions, engagement_thousands)
SOCIAL_DATA = [
    ("X/Twitter",  62, 41.2),
    ("LinkedIn",   24,  9.8),
    ("Facebook",   31, 18.4),
    ("Instagram",  19,  7.6),
    ("TikTok",      8, 62.0),  # viral Brazil content
]
