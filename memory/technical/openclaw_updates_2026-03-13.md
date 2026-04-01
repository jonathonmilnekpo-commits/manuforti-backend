---
date: 2026-03-13
topic: technical
tags: ['44699', '43987', 'technical']
---

# OpenClaw Updates — March 13, 2026

## Critical Security Updates

### ⚠️ CVE-2026-XXXXX — Origin Bypass (CRITICAL)
- **Patched in:** 2026.3.11
- **Status:** ✅ You are on 2026.3.12 (patched)
- **Action Required:** None — already secure

### 6 New Vulnerabilities Patched (March 11)
- Server-side request forgery (SSRF)
- Missing authentication bugs  
- Path traversal issues

## Latest Release: 2026.3.12 (March 12)

### New Features
| Feature | Description | Impact |
|---------|-------------|--------|
| **Dashboard v2** | Full redesign with modular views | Better monitoring of Venture cron jobs |
| **Fast Mode** | New model speed option | Faster responses for routine tasks |
| **Better Plugin System** | Improved skill management | Easier to add new capabilities |

### Breaking Changes

**Cron Job Delivery Rules (2026.3.11)**
> "Cron now enforces stricter delivery rules in isolated runs"

- Cron jobs can no longer notify through ad hoc agent sends
- Fallback main-session summaries disabled
- **Impact on Venture:** Eirik reviews may need different notification method
- **Fix:** Use `openclaw doctor --fix` for legacy cron migration

### Known Issues in 2026.3.12

1. **Chat UI Error** — Warning logs showing, no records displayed
   - GitHub Issue #44699
   - Status: Bug reported, workaround pending

2. **Token Usage Display** — Shows 0/200k despite active conversation
   - GitHub Issue #43987
   - Affects: ollama/qwen3.5:35b model

## Industry News

- **Tencent** launched QClaw AI agent with one-click OpenClaw deployment (March 10)
- **China** running massive AI experiment with OpenClaw adoption
- **OpenClawd** released cloud-hosted platform with expanded language support

## Recommendations

1. ✅ **Security:** You're on 2026.3.12 — all known CVEs patched
2. ⚠️ **Monitor:** Chat UI bug may affect Control interface
3. 🔄 **Action:** Update Venture cron delivery settings for new restrictions

---

*Researched by: Researcher Agent 🔍*
*Next update: March 14, 2026 at 02:00 GMT*
