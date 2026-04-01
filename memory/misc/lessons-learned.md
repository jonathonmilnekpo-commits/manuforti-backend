---
date: 2026-04-01
topic: misc
tags: ['misc']
---

# Lessons Learned

## 2026-03-04: Product 1 Generation Failures

### Lesson 1: Always Check Canonical Template First

**Mistake:** Generated Product 1 for ControlPartner without reviewing the locked v15 canonical template in MEMORY.md.

**Impact:** 
- Wrong format and structure
- Missing required visual elements (risk gauge)
- Incorrect financial metrics presentation
- Poor quality output that didn't meet standards

**Root Cause:** Took shortcuts instead of following established process.

**Correction:**
1. Always read MEMORY.md Product 1 section before starting
2. Review Jarotech or Boskalis reference files
3. Use proper skill input format, not hand-written JSON
4. Validate output against canonical template

**Prevention:**
- Create pre-task checklist for Product 1 work
- Run validation before sending output
- Compare to reference files

---

### Lesson 2: Don't Let Data Limitations Stop Quality

**Mistake:** Focused on ControlPartner's lack of public financials instead of creating best possible report with available data.

**Impact:**
- Delayed delivery
- Poor attitude about the task
- Didn't meet user needs

**Correction:**
- Create "Lite" version acknowledging data gaps
- Focus on what CAN be done, not what can't
- Be transparent about limitations while still delivering value

**Prevention:**
- Ask user preference when data is limited
- Offer alternatives (different target, lite version, etc.)
- Don't let perfect be enemy of good

---

### Lesson 3: Use Skills Properly

**Mistake:** Didn't use the Product 1 generator skill as designed. Hand-wrote JSON and ran generic script.

**Impact:**
- Output didn't match canonical format
- Missing required elements
- Wasted time on manual work

**Correction:**
- Use skills as documented
- Follow skill input/output specifications
- Don't reinvent the wheel

**Prevention:**
- Read SKILL.md before using skill
- Check for example inputs/outputs
- Test with small example first

---

## Pattern: Reluctance to Use Established Tools

**Observation:** Multiple instances of not using available skills properly:
- Product 1 generator (hand-wrote instead of using skill)
- Memory search (didn't check before task)
- Email sender (tried wrong commands first)

**Hypothesis:** Taking shortcuts to save time, but actually creating more work.

**Solution:** 
- Enforce pre-task skill check
- Document proper usage patterns
- Track success/failure by method