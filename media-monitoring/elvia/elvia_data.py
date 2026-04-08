"""
Elvia AS — Media Monitoring Master Data File
=============================================
VERSION: v1 | PERIOD: March 3 - April 1, 2026 (30 days)

SEARCH PROTOCOL:
Elvia operates ONLY in Norway. All searches in Norwegian + Norwegian sources.
No international operations — no multilingual search required.

Search terms used:
  Norwegian: "Elvia" + "nettleie" + "strømnett" + "strømbrudd" + "utbygging"
  Norwegian: "Elvia" + "nettselskap" + "investering" + "beredskap" + "digitalisering"
  Norwegian: "Elvia" + "AMS" + "smarte målere" + "Heimdall" + "Siemens"
  Norwegian: "Elvia" + "NVE" + "RME" + "regulering" + "tariff"
  Norwegian: "Elvia" + "strømberedskap" + "Liåsen" + "Oslo sør"

KEY ASSETS:
  - Distribution grid: Oslo, Akershus, Innlandet, Østfold (~970,000 customers)
  - 950,000 AMS smart meters deployed
  - Liåsen grid reinforcement project (Oslo south)
  - Heimdall Power system-wide capacity monitoring (first in world)
  - Siemens Gridscale X digital twin (low-voltage grid)
  - IFS Cloud ERP (cloud-first strategy)

OWNERSHIP:
  Elvia AS → 100% owned by Eidsiva Energi AS
  Eidsiva Energi AS → 50% Hafslund Vekst AS (Oslo municipality)
                   → 50% Innlandet Energi Holding AS
"""

VERSION = "v1"
REPORT_PERIOD = "March 3 - April 1, 2026 (30 days)"
COMPANY_NAME = "Elvia AS"
GENERATED_BY = "Manu Forti Intelligence"

RISK_SCORE = "MEDIUM"
RISK_ASSESSMENT = "Grid tariff increases driving consumer backlash; strong digital transformation narrative"

PROJECT_STATUS = {
    "Distribution Network — Norway (Core Asset)": {
        "type": "Electricity Distribution (DSO)",
        "capacity": "~970,000 customers | Oslo, Akershus, Innlandet, Østfold",
        "location": "Eastern Norway",
        "indigenous_group": "N/A",
        "search_terms": [
            "Elvia nettselskap", "Elvia strømnett", "nettleie Elvia",
            "strømbrudd Elvia", "Elvia utbygging", "Elvia investering"
        ],
        "risk": "MEDIUM",
        "status": (
            "Norway's largest DSO, responsible for grid infrastructure serving ~2 million people "
            "across Oslo, Akershus (Viken), Innlandet and Østfold. Formed January 2020 from merger "
            "of Eidsiva Nett and Hafslund Nett. Annual revenues ~NOK 6–7 billion. "
            "Network tariff (nettleie) is primary revenue source, regulated by NVE/RME. "
            "Elvia distributed NOK 535 million in dividends to owners in 2024, attracting criticism "
            "that monopoly profits are excessive while tariffs rise."
        ),
        "latest_development": "NVE approved 3.6% tariff increase for 2026; electricity tax cut offsets consumer impact"
    },
    "Liåsen Grid Reinforcement (Oslo South)": {
        "type": "Grid Infrastructure Investment",
        "capacity": "Strengthening south Oslo supply security",
        "location": "Liåsen, South Oslo",
        "indigenous_group": "N/A",
        "search_terms": [
            "Elvia Liåsen", "strømforsyning Oslo sør", "Statnett Elvia utbygging",
            "nettilknytning Oslo 2026"
        ],
        "risk": "LOW",
        "status": (
            "Major grid reinforcement project to strengthen electricity supply in south Oslo. "
            "Statnett construction started October 2024. Elvia's network connection work "
            "planned to start February 2026. Project critical for capacity to handle EV "
            "charging growth and electrification in the region."
        ),
        "latest_development": "Elvia grid connection work commenced February 2026 per plan"
    },
    "Heimdall Power — System-Wide Capacity Monitoring": {
        "type": "Digital Grid Technology",
        "capacity": "132 kV line monitoring — world first system-wide deployment",
        "location": "Elvia grid network, Eastern Norway",
        "indigenous_group": "N/A",
        "search_terms": [
            "Elvia Heimdall Power", "kapasitetsovervåking strømnett",
            "digitalisering kraftnett", "smarte sensorer nett"
        ],
        "risk": "LOW",
        "status": (
            "Elvia is the world's first utility to deploy Heimdall Power sensors system-wide "
            "across its distribution grid. The deployment boosted grid capacity by 20% without "
            "new physical infrastructure, enabling more renewable energy connection. "
            "Partnership signed for 132 kV digitised line pilot in 2023, expanded to system-wide "
            "contract. Elvia is Heimdall's anchor customer globally."
        ),
        "latest_development": "System-wide deployment completed; capacity increased 20%; Heimdall expanding globally using Elvia as reference"
    },
    "Siemens Gridscale X — Digital Twin": {
        "type": "Digital Grid Infrastructure",
        "capacity": "Full low-voltage grid digital twin",
        "location": "Elvia grid network",
        "indigenous_group": "N/A",
        "search_terms": [
            "Elvia Siemens", "digital tvilling strømnett", "lavspent nett digitalisering",
            "Gridscale X Elvia"
        ],
        "risk": "LOW",
        "status": (
            "Elvia partnered with Siemens to create a full digital twin of its low-voltage "
            "distribution grid using the Gridscale X platform. Enables real-time fault detection, "
            "predictive maintenance, and optimised network operations. Positions Elvia as a "
            "digital leader among European DSOs."
        ),
        "latest_development": "Digital twin operational; used for fault detection and capacity planning"
    },
    "AMS Smart Meter Programme": {
        "type": "Smart Metering",
        "capacity": "950,000 smart meters deployed to all customers",
        "location": "All Elvia grid areas",
        "indigenous_group": "N/A",
        "search_terms": [
            "Elvia AMS måler", "smarte strømmålere", "HAN-port Elvia",
            "sanntidsmåling strøm", "strømmåler Elvia"
        ],
        "risk": "LOW",
        "status": (
            "Completed deployment of 950,000 AMS smart meters across all customers. "
            "AI/machine learning system built on meter data to detect dangerous earth faults (jordfeil). "
            "HAN port enables customers to monitor real-time consumption. "
            "Consumer advocacy group (Forbrukerrådet) flagged concerns about lock-in and lack "
            "of standardised real-time data access in 2024 report."
        ),
        "latest_development": "AI-based earth fault detection system live; Forbrukerrådet report flagged lock-in concerns (2024)"
    },
    "NVE Tariff Regulation — 2026": {
        "type": "Regulatory / Tariff",
        "capacity": "Affects ~970,000 customers",
        "location": "Norway (national regulation)",
        "indigenous_group": "N/A",
        "search_terms": [
            "Elvia nettleie 2026", "NVE nettleie økning", "RME tariff regulering",
            "elavgift nettleie Elvia", "nettleie kritikk"
        ],
        "risk": "MEDIUM",
        "status": (
            "NVE approved 3.6% grid tariff increase for Elvia in 2026 driven by rising investment "
            "costs. Government cut electricity tax from 16.93 øre to 7.13 øre/kWh from January 2026 "
            "to partially offset impact. Elvia CEO Anne Sagstuen Nysæther welcomed the tax cut. "
            "Long-term outlook: NVE/RME projections show 20-30% tariff increase by 2030 as grid "
            "investment accelerates. Elvia's NOK 535M dividend payments have attracted political "
            "criticism about monopoly profits. Price cap for regional grid raised to 400 kr/MWh for 2026."
        ),
        "latest_development": "Electricity tax cut from Jan 2026 (7.13 øre/kWh) partially offsetting 3.6% grid tariff rise"
    },
}

KEY_METRICS = [
    ("Overall Risk Score", "MEDIUM — tariff politics; strong digital innovation narrative"),
    ("Coverage Area", "Oslo, Akershus, Innlandet, Østfold — ~970,000 customers / ~2 million people"),
    ("Network Tariff 2026", "3.6% increase approved; electricity tax cut offsets consumer impact"),
    ("Long-Term Tariff Outlook", "NVE: 20-30% increase by 2030 — politically sensitive"),
    ("Digital Innovation", "POSITIVE — world-first Heimdall deployment; Siemens digital twin"),
    ("Dividend Criticism", "NOK 535M dividends paid 2024 — political scrutiny on monopoly profits"),
    ("Liåsen Project", "On track — Elvia work commenced February 2026"),
    ("Smart Meters", "Complete — 950,000 AMS deployed; AI fault detection live"),
]

SUMMARY = (
    "Elvia AS is Norway's largest electricity distribution system operator (DSO), serving "
    "approximately 970,000 customers across Oslo, Akershus, Innlandet and Østfold. Formed in 2020 "
    "from the merger of Eidsiva Nett and Hafslund Nett, Elvia is wholly owned by Eidsiva Energi AS "
    "(50% Hafslund Vekst / 50% Innlandet Energi Holding). "
    "The company's media profile over the last 30 days is dominated by two contrasting narratives: "
    "first, rising grid tariffs and growing consumer and political frustration with network costs "
    "expected to increase 20-30% by 2030; and second, strong innovation leadership through world-first "
    "Heimdall Power grid capacity monitoring and Siemens digital twin deployment. "
    "The January 2026 electricity tax cut (7.13 øre/kWh) partially offset the 3.6% NVE-approved "
    "tariff increase, with Elvia CEO welcoming the government measure. The Liåsen south Oslo grid "
    "reinforcement project progressed as planned. Key medium-term risk is political and consumer "
    "pressure on tariff increases as grid investment accelerates toward 2030."
)

THEMES = [
    {
        "title": "Nettleie i 2026 — Skattelette demper økningen",
        "content": (
            "NVE godkjente en økning i nettleien på 3,6 prosent for 2026 hos Elvia, begrunnet med "
            "stigende investeringskostnader i strømnettet. Stortinget vedtok imidlertid kutt i elavgiften "
            "fra 16,93 til 7,13 øre per kWh fra 1. januar 2026, noe som demper den totale økningen "
            "for forbrukerne betraktelig. Elvias administrerende direktør Anne Sagstuen Nysæther "
            "omtalte avgiftskuttet som 'gledelig'. Pristaket for regionalnettet økte fra 350 til "
            "400 kr/MWh for 2026. Den langsiktige utfordringen er større: NVE og Elvia selv varsler "
            "en samlet økning på 20–30 prosent frem mot 2030."
        )
    },
    {
        "title": "Politisk press på nettselskapsoverskudd",
        "content": (
            "Elvia utbetalte 535 millioner kroner i utbytte til sine eiere i 2024, noe som har "
            "generert politisk og mediebasert kritikk om at selskapet opererer med 'monopoloverskudd' "
            "på bekostning av forbrukerne. Kommentatorer og politikere har stilt spørsmål ved om "
            "nettselskaper som opererer som naturlige monopoler bør ha anledning til å utbetale "
            "store utbytter mens tariffene øker. Regjeringens avgiftskutt er delvis et svar på "
            "dette presset. NVE/RME har varslet at den tillatte avkastningsraten for nettselskaper "
            "vil justeres ned til 6 prosent fra 2026."
        )
    },
    {
        "title": "Verdens første systemdekkende kapasitetsovervåking med Heimdall Power",
        "content": (
            "Elvia er verdens første nettselskap til å deployere Heimdall Powers sensorteknologi "
            "for systemdekkende kapasitetsovervåking av hele distribusjonsnettet. Prosjektet har "
            "økt kapasiteten i nettet med 20 prosent uten nye fysiske anlegg, og Elvia er "
            "Heimdalls viktigste referansekunde internasjonalt. Heimdall Power har nå over 40 "
            "kunder globalt, inkludert DSO-er i Germany, Sverige, Finland, Frankrike og USA, "
            "alle med Elvia-kontrakten som bevis på konseptets skalerbarhet. Innovasjonen "
            "posisjonerer Elvia som en ledende aktør i europeisk nettdigitalisering."
        )
    },
    {
        "title": "Siemens digital tvilling og AMS-basert jordfeildeteksjon",
        "content": (
            "Elvia har i samarbeid med Siemens skapt en fullstendig digital tvilling (digital twin) "
            "av lavspentnettet ved hjelp av Gridscale X-plattformen. Systemet muliggjør sanntidsovervåking, "
            "prediktivt vedlikehold og optimalisert nettdrift. I tillegg har Elvia utviklet et "
            "maskinlæringsbasert system som bruker data fra de 950 000 AMS-målerne til å oppdage "
            "farlige jordfeil — både i nettet og hos kundene. Forbrukerrådet påpekte i en rapport "
            "i 2024 at det mangler standardiserte løsninger for sanntidstilgang via HAN-porten, "
            "noe som kan skape innlåsing hos leverandørene."
        )
    },
    {
        "title": "Liåsen-prosjektet — Styrking av strømforsyningen i Oslo sør",
        "content": (
            "Elvia gjennomfører i 2026 et større nettforsterkningsprosjekt i Liåsen-området for å "
            "styrke strømforsyningen i sør-Oslo. Statnetts byggearbeider startet i oktober 2024, "
            "og Elvias nettilknytning startet som planlagt i februar 2026. Prosjektet er kritisk "
            "for å møte økt kapasitetsbehov fra elbillading og elektrifisering av transport "
            "og næring i regionen. Prosjektet er del av Elvias samlede investeringsprogram "
            "som er driveren bak fremtidige nettleieøkninger."
        )
    },
]

# ===== MEDIA ITEMS =====
# All Norwegian-language sources + key international/English coverage
MEDIA_ITEMS = [
    # ===== NETTLEIE / TARIFF (Norwegian) =====
    ("Des 15", "VG", "Kutt i elavgift gir så mye lavere nettleie hos Elvia [Electricity tax cut lowers Elvia tariff]", "Tariff/Consumer", "Positive"),
    ("Des 15", "NTB/Elvia", "Kutt i elavgift gir lavere nettleie fra 1. januar — Elvia pressemelding", "Corporate", "Positive"),
    ("Nov 19", "Nettavisen", "Nettleien vil bli dyrere i 2026 — NVE varsler økning", "Tariff/Regulatory", "Negative"),
    ("Sep 15", "Nettavisen", "NVE mener nettleien skal øke kraftig frem mot 2030", "Regulatory", "Negative"),
    ("Mar 15", "Bytt.no", "Nettleie 2026: Slik påvirker økt beredskap strømregningen din", "Consumer", "Negative"),
    ("Mar 20", "Kraftsystemet", "Elvia nettleiepriser 2026 — fastledd og kapasitetsledd oppdatert", "Tariff", "Neutral"),

    # ===== POLITISK KRITIKK / UTBYTTE =====
    ("Sep 16", "Gudbrandsdølen Dagningen", "Nettleien blir mye dyrere: Elvia utbetalte 535 millioner til eiere i fjor", "Political/Financial", "Negative"),
    ("Sep 15", "Nettavisen", "Nettleien blir mye dyrere: Nettselskapene skal få høyere avkastning", "Political", "Negative"),
    ("Aug 22", "Reddit r/norge", "Trodde det var strømprisen jeg skulle være redd for, ikke nettleien — Elvia kritikk", "Consumer", "Negative"),

    # ===== DIGITAL INNOVASJON =====
    ("Okt 21", "Heimdall Power", "Heimdall Power launches world's first system-wide capacity monitoring project with Elvia", "Innovation", "Positive"),
    ("Des 6",  "Heimdall Power", "Elvia leads grid upgrade with Heimdall sensors — capacity up 20%", "Innovation", "Positive"),
    ("Mar 22", "Nettavisen", "Elvia bruker AMS-måleren til å finne farlige jordfeil med maskinlæring", "Innovation", "Positive"),
    ("Mai 3",  "The Innovator", "Norwegian scale-up Heimdall Power — Elvia contract drives global expansion", "Innovation", "Positive"),
    ("2024",   "Siemens Global", "Elvia and Siemens Gridscale X: Digital Twin of low-voltage grid", "Innovation", "Positive"),
    ("2024",   "Google Cloud", "Elvia deploys 900,000 smart meters and cloud-first strategy (case study)", "Innovation", "Positive"),

    # ===== LIÅSEN / PROSJEKTER =====
    ("Feb 26", "Elvia.no", "Elvia starter nettilknytning på Liåsen — styrker strøm i Oslo sør", "Infrastructure", "Positive"),
    ("Okt 24", "Elvia.no", "Statnett starter byggearbeider Liåsen — Elvia nettilknytning følger i 2026", "Infrastructure", "Neutral"),

    # ===== BEREDSKAP =====
    ("2025",   "NTB Kommunikasjon", "Nettselskap: Nå øker beredskapen i Norges største nettselskap", "Security/Operations", "Positive"),

    # ===== AMS / SMARTMÅLERE =====
    ("Feb 24", "Forbrukerrådet", "Sanntidsmålere strøm: innelåsing og manglende standarder — Elvia nevnt", "Consumer/Regulatory", "Negative"),
    ("2024",   "Esri", "Elvia accelerates digital future — distribution transformer transformation", "Innovation", "Positive"),

    # ===== EIERSKAPSINFORMASJON =====
    ("Jan 25", "Scope Group", "Eidsiva Energi rating — Elvia er landets største distribusjonsselskap", "Financial/Credit", "Neutral"),
    ("Nov 25", "NIB", "NIB signs loan with Hafslund for key infrastructure — Elvia grid investment", "Financial", "Positive"),
    ("Mar 26", "Euronext", "Eidsiva Årsrapport 2025 — Elvia resultat og utbytte [annual report]", "Financial", "Neutral"),

    # ===== ESRI / DATA MODELL =====
    ("2024",   "Lnett/Elvia", "Ny datamodell fra Lnett og Elvia tas i bruk som europeisk standard i Esri", "Innovation", "Positive"),

    # ===== INTERNASJONAL DEKNING =====
    ("Jan 25", "Scope Group", "Eidsiva Energi credit analysis: Elvia as stable regulated core asset", "Financial/Credit", "Neutral"),
    ("Nov 24", "NIB", "Nordic Investment Bank loan to Hafslund — EV charging and grid investment", "Financial", "Positive"),
]

# ===== SOCIAL MEDIA DATA =====
SOCIAL_DATA = [
    ("X/Twitter",  22,  8.4),
    ("LinkedIn",   31, 14.2),   # professional / B2B focus
    ("Facebook",   18,  6.1),
    ("Instagram",   8,  2.3),
]
