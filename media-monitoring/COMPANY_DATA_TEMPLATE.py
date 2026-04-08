"""
Manu Forti Intelligence — Media Monitoring Data Template
=========================================================
STANDARD DATA INPUT FOR ALL MEDIA MONITORING REPORTS

HOW TO USE:
1. Copy this file to media-monitoring/<company>/
2. Rename to <company>_data.py
3. Fill in all sections with researched data
4. Run generate_<company>_report.py (copy generator template too)

SEARCH PROTOCOL — MANDATORY:
For every company, map ALL operating countries and ALL named projects.
Search EACH PROJECT NAME in the LOCAL LANGUAGE of each country.
Never search company name only. Never English only.

Search formula: "[Project name in local language]" + "[Company]" + "[local controversy term]"

Examples:
  Norway:    "Fosen Vind" + "Statkraft" + "same reindrift" (Norwegian)
  Brazil:    "Santa Eugênia" + "Statkraft" + "quilombola desmatamento" (Portuguese)
  Chile:     "Los Lagos" + "Statkraft" + "Mapuche río Pilmaiquén" (Spanish)
  Germany:   "Flechtdorf" + "Statkraft" + "Windpark Genehmigung" (German)
  France:    "Projet X" + "Company" + "opposition locale" (French)
  ...and so on for every country in the portfolio

LOCAL MEDIA SOURCES TO CHECK (in addition to international):
  Norway: NRK, Aftenposten, E24, Dagens Næringsliv
  Brazil: Folha de S.Paulo, O Globo, Mongabay Brasil, Jornal GGN
  Chile: La Tercera, El Mercurio, Biobiochile, El País América
  Germany: Handelsblatt, FAZ, Spiegel, local Anzeiger
  UK: The Guardian, FT, local planning authority notices
  Spain: El País, Expansión
  India: Economic Times, Business Standard, Mint
  France: Le Monde, Les Echos
  Netherlands: NRC, Volkskrant
  Sweden: Dagens Nyheter, SvD
"""

# ===== REPORT METADATA =====
VERSION = "v1"
REPORT_PERIOD = "March 1-31, 2026 (30 days)"
COMPANY_NAME = "Company Name AS"
GENERATED_BY = "Manu Forti Intelligence"

# ===== OVERALL RISK =====
RISK_SCORE = "MEDIUM"   # 'LOW', 'MEDIUM', or 'HIGH'
RISK_ASSESSMENT = "One-line summary of overall risk posture"

# ===== PROJECT STATUS =====
# One entry per major project/asset. Include ALL operating countries.
PROJECT_STATUS = {
    "Project Name (Country)": {
        "type": "Technology type (Hydro / Wind / Solar / etc.)",
        "capacity": "MW or GW capacity",
        "location": "City/Region, Country",
        "indigenous_group": "Name of community or 'N/A'",
        "search_terms": [
            "project name in local language",
            "company name in local language",
            "local controversy keyword",
        ],
        "risk": "LOW",   # LOW / MEDIUM / HIGH / CRITICAL
        "status": "Current operational and controversy status in 2-3 sentences.",
        "latest_development": "Most recent newsworthy development in one sentence."
    },
    # Add one entry per project/country...
}

# ===== KEY METRICS =====
# 6-8 rows that summarise the most important indicators
KEY_METRICS = [
    ("Overall Risk Score", "MEDIUM — brief explanation"),
    ("30-Day Mentions", "X articles + Y social posts = Z total"),
    ("Project A (Country)", "RISK LEVEL — one-line status"),
    ("Project B (Country)", "RISK LEVEL — one-line status"),
    ("Financial Snapshot", "Revenue/EBITDA highlight if available"),
    ("ESG Summary", "Key ESG finding in one line"),
]

# ===== EXECUTIVE SUMMARY =====
# 3-5 sentences. Financial performance + key risks + geographic scope.
SUMMARY = (
    "Company overview and financial position. "
    "Key risk themes across the monitoring period. "
    "Geographic scope and most material developments."
)

# ===== KEY THEMES =====
# 5 themes minimum. Each is a heading + 3-5 sentences of analysis.
THEMES = [
    {
        "title": "Theme 1 — Most Material Issue",
        "content": "3-5 sentences of analysis with specific facts, dates, sources."
    },
    {
        "title": "Theme 2",
        "content": "..."
    },
    {
        "title": "Theme 3",
        "content": "..."
    },
    {
        "title": "Theme 4",
        "content": "..."
    },
    {
        "title": "Theme 5",
        "content": "..."
    },
]

# ===== MEDIA ITEMS =====
# Format: (date, source, headline, category, sentiment)
# Sentiment: 'Positive', 'Neutral', or 'Negative'
# Include articles in local languages — do NOT translate headlines, note language in source field
# Categories: Financial Results | ESG/NGO | Legal | Indigenous Rights | Environmental |
#             Community | Corporate | Industry | Regulatory | Government
MEDIA_ITEMS = [
    # ===== FINANCIAL =====
    ("Mar 5", "Reuters", "Company Q4 results beat expectations", "Financial Results", "Positive"),

    # ===== LOCAL LANGUAGE — Country 1 =====
    ("Mar 10", "Local Newspaper (NO)", "Local headline in Norwegian", "Category", "Negative"),

    # ===== LOCAL LANGUAGE — Country 2 =====
    ("Mar 12", "Local Newspaper (PT)", "Manchete em Português", "Category", "Negative"),

    # ===== INTERNATIONAL =====
    ("Mar 20", "Financial Times", "International coverage headline", "Industry", "Neutral"),
]

# ===== SOCIAL MEDIA DATA =====
# Format: (platform, mentions_count, engagement_thousands)
SOCIAL_DATA = [
    ("X/Twitter",  40, 22.0),
    ("LinkedIn",   15,  6.5),
    ("Facebook",   20, 11.0),
    ("Instagram",  12,  4.5),
]
