# Media Monitoring Standard Research Protocol

## Rule: ALWAYS search project names + company + local language

For every company, the research process is:

1. Map ALL operating countries and ALL named projects
2. Search each project in the LOCAL LANGUAGE of that country
3. Search company name in each local language
4. Use regional media sources, not just international English press

## Search Template

For each country:
  - "[Company name in local language]" + "[project name]" + "[local term for controversy/opposition]"

## Statkraft Search Map

| Country | Language | Search Terms |
|---------|----------|-------------|
| Norway | Norwegian | "Statkraft" + "Fosen Vind" + "same" / "reindrift" / "rettigheter" |
| Brazil | Portuguese | "Statkraft" + "Santa Eugênia" + "Umbu" + "desmatamento" + "quilombola" |
| Chile | Spanish | "Statkraft" + "Los Lagos" + "Pilmaiquen" + "Mapuche" + "Huilliche" |
| Albania | Albanian | "Statkraft" + "Devoll" + "Banja" + "Moglica" |
| Germany | German | "Statkraft" + "Flechtdorf" + "Zerbst" + "Windpark" |
| UK | English | "Statkraft" + project names + "planning objection" |
| India | English | "Statkraft" + "Serentica" + "solar" + "India" |
| Turkey | Turkish | "Statkraft" + "hidroelektrik" + "çevre" |

## Report Generation Rule

ALWAYS use the generator. Never write from scratch:
```python
import sys
sys.path.insert(0, '/Users/jonathonmilne/.openclaw/workspace/skills/media-monitoring-report')
from generate_report import generate_media_monitoring_report
```

## Version Rule

Each version BUILDS on previous. Never replace. Append new data to existing data file.
