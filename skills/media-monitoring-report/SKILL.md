---
name: media-monitoring-report
description: Generates professional Media Monitoring reports for supplier intelligence. Creates executive-ready Word documents with 30-day media coverage analysis, sentiment categorization, social media monitoring, and trend visualization. Use when delivering media monitoring subscriptions or standalone reports.
---

# ⚠️ MANDATORY — READ THIS FIRST

## Standard Data Input System (April 2026 — ALL companies)

Every media monitoring report uses this file structure:
```
media-monitoring/
  COMPANY_DATA_TEMPLATE.py      ← copy for each new company
  GENERATOR_TEMPLATE.py         ← copy for each new company
  STANDARD_PROTOCOL.md          ← search rules
  statkraft/
    statkraft_data.py            ← versioned data file
    generate_statkraft_report.py ← one-command generator
```

To run any report: `python3 media-monitoring/<company>/generate_<company>_report.py`

To add a new company:
1. Copy COMPANY_DATA_TEMPLATE.py → media-monitoring/<company>/<company>_data.py
2. Copy GENERATOR_TEMPLATE.py → media-monitoring/<company>/generate_<company>_report.py
3. Fill in data (research ALL projects in ALL countries in LOCAL LANGUAGE)
4. Run generator

**ALWAYS USE `generate_report.py` TO GENERATE REPORTS.**

NEVER write a report generator from scratch. The script at:
`/Users/jonathonmilne/.openclaw/workspace/skills/media-monitoring-report/generate_report.py`

...produces the PROPER professional format: navy cover page, colour-coded sentiment tables, structured metrics, Manu Forti branding, and all locked v1.1 styling.

**Usage:**
```python
import sys
sys.path.insert(0, '/Users/jonathonmilne/.openclaw/workspace/skills/media-monitoring-report')
from generate_report import generate_media_monitoring_report

generate_media_monitoring_report(
    company_name=...,
    report_period=...,
    risk_assessment=...,
    risk_score=...,   # 'LOW', 'MEDIUM', or 'HIGH'
    summary_text=...,
    key_metrics=[...],
    themes=[...],
    media_items=[...],
    output_path=...
)
```

Then open the output with `Document(output_path)` and append enterprise sections.

**NEVER skip this.** Writing from scratch = plain text, no cover, no formatting = rejected by Jonathon.

# Media Monitoring Report Format (LOCKED v1.1)

**Version:** 1.1  
**Date:** March 11, 2026  
**Status:** CANONICAL — Do not modify without approval  
**Changes:** Added sentiment trend charts and social media monitoring

---

## Report Structure (LOCKED)

### 1. Cover Page
- Manu Forti crest logo (top center)
- Navy blue background (#002147) — full page
- "MANU FORTI INTELLIGENCE" — bold white, 28pt
- "MEDIA MONITORING / SUPPLIER INTELLIGENCE REPORT" — 20pt/14pt
- Company name in highlighted box (#1a3a5c)
- Report metadata: Period, Date, Reference
- Confidentiality footer

### 2. Executive Summary (Page 2-3)
- Overall Risk Assessment (color-coded)
- Summary paragraph
- Key Metrics table (5 rows)
- **NEW: Sentiment Trend Overview** — 30-day trajectory

### 3. Sentiment Trend Analysis (Page 4) ⭐ NEW
- **Line chart:** Daily sentiment score (0-100)
- **Moving average:** 7-day trend line
- **Key inflection points:** Annotated events
- **Volume overlay:** Article count per day

### 4. Key Themes from Media Coverage (Page 5-6)
- Analysis period stated
- 5 key themes minimum
- Each theme: Heading + 2-3 sentence explanation

### 5. Traditional Media Coverage (Page 7-8)
- Sentiment summary table
- Detailed media table (Date/Source/Headline/Category/Sentiment)

### 6. Social Media Monitoring (Page 9-10) ⭐ NEW
- **Platform breakdown:** X/Twitter, LinkedIn, Facebook, YouTube
- **Engagement metrics:** Shares, likes, comments, reach
- **Top performing posts:** Highest engagement
- **Influencer mentions:** Key accounts mentioning supplier
- **Social sentiment:** Platform-specific analysis

### 7. 30-Day Media Summary (Page 11)
- Combined traditional + social media stats
- Week-over-week comparison
- Emerging topics word cloud

---

## NEW: Sentiment Trend Visualization

### Chart Specifications
- **Type:** Dual-axis line chart
- **X-axis:** Date (last 30 days)
- **Y-axis (left):** Sentiment score (0-100)
- **Y-axis (right):** Article volume (count)
- **Lines:**
  - Daily sentiment (navy line)
  - 7-day moving average (cobalt line)
  - Volume bars (light gray)

### Color Coding
- Score 0-33: Red zone (negative)
- Score 34-66: Amber zone (neutral)
- Score 67-100: Green zone (positive)

### Annotations
- Major events labeled on chart
- Contract wins, earnings, controversies
- CEO statements, analyst ratings

---

## NEW: Social Media Monitoring

### Platforms Monitored
1. **X (Twitter)** — Real-time news, executive statements
2. **LinkedIn** — B2B announcements, hiring, executive posts
3. **Facebook** — Community sentiment, local news
4. **YouTube** — Corporate videos, conference presentations, earnings calls

### Metrics Tracked
| Metric | X | LinkedIn | Facebook | YouTube |
|--------|---|----------|----------|---------|
| Mentions | ✅ | ✅ | ✅ | ✅ |
| Sentiment | ✅ | ✅ | ✅ | ✅ |
| Shares/Reposts | ✅ | ✅ | ✅ | N/A |
| Likes/Reactions | ✅ | ✅ | ✅ | ✅ |
| Comments | ✅ | ✅ | ✅ | ✅ |
| Reach/Views | ✅ | ✅ | ✅ | ✅ |
| Engagement Rate | ✅ | ✅ | ✅ | ✅ |

### Social Media Table Format
| Date | Platform | Author | Content | Engagement | Sentiment |
|------|----------|--------|---------|------------|-----------|
| Mar 5 | LinkedIn | CEO Peter Berdowski | "Proud of our 2025 results..." | 2.4K likes, 156 comments | Positive |
| Mar 3 | X | @Boskalis | "New contract win: Gennaker..." | 89 retweets, 245 likes | Positive |

### Top Influencers
- Track accounts with >10K followers mentioning supplier
- Categorize: Industry analyst, Journalist, Competitor, Customer, NGO
- Flag verified accounts and blue-check marks

---

## Visual Standards (LOCKED)

### Colors
| Element | Hex Code | RGB |
|---------|----------|-----|
| Navy (background) | #002147 | 0, 33, 71 |
| Cobalt (accent) | #2B6CB0 | 43, 108, 176 |
| Green (positive) | #48BB78 | 72, 187, 120 |
| Amber (medium) | #D69E2E | 214, 158, 46 |
| Red (negative/high) | #E53E3E | 229, 62, 62 |
| Positive background | #d4edda | 212, 237, 218 |
| Neutral background | #fff3cd | 255, 243, 205 |
| Negative background | #f8d7da | 248, 215, 218 |
| X (Twitter) blue | #1DA1F2 | 29, 161, 242 |
| LinkedIn blue | #0A66C2 | 10, 102, 194 |
| Facebook blue | #1877F2 | 24, 119, 242 |
| YouTube red | #FF0000 | 255, 0, 0 |

### Typography
- **Headings:** Calibri Bold, 16-20pt, Navy #002147
- **Body:** Calibri Regular, 11pt, Black
- **Tables:** Calibri, 10pt
- **Charts:** Arial, 9pt for labels

### Charts
- **Sentiment Trend:** Matplotlib line chart, saved as PNG
- **Social Breakdown:** Horizontal bar chart by platform
- **Engagement:** Vertical bar chart, top 5 posts

---

## Data Sources (Expanded)

### Traditional Media (Existing)
- Company press releases
- Financial news (Reuters, Bloomberg, FT)
- Industry publications
- Local news
- NGO websites

### Social Media (NEW)
- **X API** — Real-time tweets, mentions, hashtags
- **LinkedIn API** — Company posts, executive activity
- **Facebook Graph API** — Public posts, comments
- **YouTube Data API** — Video uploads, comments, transcripts

### Engagement Data
- Native platform APIs for likes, shares, comments
- Third-party tools (Brandwatch, Sprout Social) as backup
- Manual verification for high-engagement posts

---

## Quality Checklist (Updated)

Before delivery, verify:
- [ ] Cover page has Manu Forti logo
- [ ] Navy background on cover (#002147)
- [ ] Executive Summary is first content section
- [ ] **Sentiment trend chart generated**
- [ ] **Social media section included**
- [ ] All 4 platforms covered (X, LinkedIn, Facebook, YouTube)
- [ ] Engagement metrics populated
- [ ] Risk assessment is color-coded
- [ ] 5 key themes are present
- [ ] 30-day media table has sentiment colors
- [ ] No placeholder text
- [ ] Confidentiality footer on cover
- [ ] File size > 100 KB (indicates charts embedded)

---

## Pricing Integration (Updated)

### Monitor Tier (€35/month)
- Weekly summary (email)
- 10 suppliers max
- Traditional media only
- Basic sentiment (positive/neutral/negative)

### Alert Tier (€105/month)
- **Full report monthly (this format v1.1)**
- **Sentiment trend charts included**
- **Social media monitoring (X + LinkedIn)**
- Real-time alerts for critical news
- 25 suppliers max

### Enterprise (Custom)
- **Weekly reports with full format**
- **All 4 social platforms (X, LinkedIn, Facebook, YouTube)**
- **Custom dashboards**
- Unlimited suppliers
- API access
- WhatsApp alerts for critical issues

---

## Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Mar 11, 2026 | Initial locked format | Jonathon Milne |
| 1.1 | Mar 11, 2026 | Added sentiment trends + social media | Jonathon Milne |
| 1.2 | Apr 1, 2026 | Enhanced methodology: multilingual search, asset-level monitoring, ESG controversy detection | Jonathon Milne |

---

## Enhanced Search Methodology (v2.0)

### 1. Asset/Project-Level Monitoring
Search company name combined with specific operational assets:
- **Format:** "[Company]" + "[Project Name]" + "[Location]"
- **Example:** "Statkraft" + "Santa Eugênia" + "Bahia"
- **Include:** Power plant names, facility locations, development projects

### 2. Multilingual Search Protocol
For each operating country, search in local language:
- **Portuguese (Brazil):** desmatamento, energia solar, quilombola, licença ambiental
- **Spanish (Latin America):** deforestación, comunidad indígena, permiso ambiental
- **Norwegian:** vindkraft, same, reindrift, miljøkonsesjon
- **Local media:** National newspapers, regional outlets, environmental NGOs

### 3. ESG Controversy Detection
Automated flagging of high-risk scenarios:
- **Environmental paradox:** "Green energy" + "environmental destruction" + company name
- **Indigenous rights:** "ILO Convention 169" + "consultation" + company name
- **Legal proceedings:** "lawsuit" + "suspended license" + company name
- **Community opposition:** "protest" + "campaign against" + company name

### 4. Stakeholder-Specific Search Terms

| Stakeholder | Search Terms |
|-------------|--------------|
| NGOs/Activists | "protest" + company, "campaign against" + company, boycott + company |
| Local Communities | Community name + "versus" + company, municipality + opposition |
| Regulators | Agency name + company + "fine" / "suspension" / "license" |
| Competitors | Company name + "vs" / "compared to" / "losing to" |

### 5. Source Weighting by Geography
- **Home market media** (Norway for Statkraft): Potential positive bias — verify claims
- **Operating country media** (Brazil for Brazil projects): Critical local perspective — Tier 1 priority
- **International financial**: Market-moving information — Tier 1 priority
- **Regional/local outlets**: Early warning signals — Tier 2 priority
- **NGO/activist sources**: ESG risk indicators — Tier 1 for controversy detection

### 6. Temporal Context Analysis
- Track controversy lifecycle: emergence → peak → resolution
- Include "ongoing" vs. "resolved" status
- Monitor if company response changed narrative trajectory
- Flag anniversaries of major incidents

### 7. Gap Analysis Section (New Required Element)
Every report must include:
- "What we may have missed" — acknowledge limitations
- Suggested follow-up searches for next report
- Data gaps (e.g., "Limited Portuguese sources scanned")
- Access limitations (e.g., "Court database not accessible")

### 8. Automated Red Flag Keywords
Immediate escalation for mentions of:
- Lawsuit filed / legal action initiated
- License suspended / revoked / denied
- Environmental permit violation
- Community blockade / protest / occupation
- Executive resignation following incident
- Regulatory investigation opened
- ESG rating downgrade

---

## Quality Checklist (Updated v1.2)

Before delivery, verify:
- [ ] Cover page has Manu Forti logo
- [ ] Navy background on cover (#002147)
- [ ] Executive Summary is first content section
- [ ] **Sentiment trend chart generated**
- [ ] **Social media section included**
- [ ] **Critical findings section for high-priority controversies**
- [ ] **Risk assessment with ESG focus**
- [ ] **Gap analysis section included**
- [ ] **Enhanced search methodology notes**
- [ ] All 4 platforms covered (X, LinkedIn, Facebook, YouTube)
- [ ] Engagement metrics populated
- [ ] Risk assessment is color-coded
- [ ] 5 key themes are present
- [ ] 30-day media table has sentiment colors
- [ ] No placeholder text
- [ ] Confidentiality footer on cover
- [ ] File size > 100 KB (indicates charts embedded)

---

**DO NOT MODIFY** this format without written approval from Jonathon Milne.

For questions or suggested improvements, document in CHANGELOG.md and request review.
