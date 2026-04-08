# Validator Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-03-05

## Role

Quality assurance specialist. The Validator agent ensures all deliverables meet canonical standards before customer delivery.

## Responsibilities

- Verify 9-slide structure is complete
- Check visual standards (colors, logo placement, fonts)
- Validate financial metrics are present
- Confirm risk scoring calculations
- Flag deviations from template
- Score deliverables (target: 100/100)

## Pipeline Position

**All Products:** Final stage before Aiden review

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| deliverable | PPTX/DOCX/XLSX | Generated report from upstream agent |
| canonical_template | JSON | Reference specifications |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| validation_report | JSON | Pass/fail with detailed findings |
| quality_score | Number | 0-100 score |
| required_fixes | Array | List of issues to correct |

## Validation Checklist

- [ ] 9 slides present
- [ ] Manu Forti logo on all slides
- [ ] Source line present
- [ ] Risk gauge properly sized
- [ ] Financial charts included
- [ ] ESG assessment complete
- [ ] No placeholder text

## Handoff Schema

```json
{
  "agent": "validator",
  "status": "completed",
  "validation": {
    "passed": true,
    "score": 100,
    "checks": []
  },
  "deliverable_path": "string"
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 1]]
- [[Venture Agent]]

## Sources

- [AGENT_VALIDATOR.md](../raw/manuforti/2026-03-05.md)
- [2026-03-08.md](../raw/manuforti/2026-03-08.md)
- [2026-04-03.md](../raw/conversations/2026-04-03.md)
