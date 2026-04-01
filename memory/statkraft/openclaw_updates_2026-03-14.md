---
date: 2026-03-14
topic: statkraft
tags: ['statkraft']
---

# OpenClaw Updates Summary - March 14, 2026

**Report Date:** 2026-03-14  
**Current Version:** v2026.3.13 (released ~20 hours ago)  
**Previous Version:** v2026.3.12 (released ~24 hours ago)

---

## 🚨 CRITICAL SECURITY ALERTS - IMMEDIATE ACTION REQUIRED

### 1. Authorization Bypass (CRITICAL - GHSA-g353-mgv3-8pcj)
- **Affected Versions:** ≤ 2026.3.11
- **Severity:** CRITICAL
- **Issue:** Missing server-side authorization checks allowed attackers with shared secrets to self-declare `operator.admin` scope via WebSocket handshake, gaining full gateway control.
- **Fix:** Update to 2026.3.12+ immediately
- **Post-Update Action:** Check gateway logs for "Clearing unbound scopes for non-Control-UI connection"

### 2. Workspace Escape (HIGH - CVE-2026-32060)
- **Affected Versions:** ≤ 2026.3.8
- **Severity:** HIGH (CVSS 8.8)
- **Issue:** Path traversal vulnerability allowed `operator.write` users to escape filesystem sandbox via malicious `workspaceDir` RPC parameter
- **Fix:** Update to 2026.3.11+
- **Mitigation:** Run OpenClaw with dedicated non-root user, chmod 700 on workspace

### 3. Credential Exposure in Setup Codes (MODERATE - CVE-2026-XXXX)
- **Affected Versions:** ≤ 2026.3.11
- **Severity:** MODERATE
- **Issue:** Setup codes/QR codes embedded long-lived gateway credentials instead of short-lived bootstrap tokens
- **Fix:** Update to 2026.3.12+
- **Post-Update Action:** Rotate gateway credentials if any setup codes were shared/logged

### 4. Additional Security Fixes (v2026.3.12/v2026.3.13)
- **Exec Approval Bypass:** Multiple hardening measures against command injection (zero-width Unicode, Ruby/Perl module flags, PowerShell wrappers, shell line continuations)
- **Authorization Bypass (Feishu):** Synthetic event processing vulnerability patched
- **Rate Limit Bypass:** Fixed in 2026.3.12
- **Improper Authorization (npm):** GHSA-r7vr-gr74-94p8 patched
- **Browser Profile Auth:** GHSA-vmhq-cqm9-6p7q fixed - proper admin boundary enforcement

**ACTION:** Update immediately with: `npm update -g openclaw && openclaw gateway restart && openclaw doctor --fix`

---

## ✨ New Features & Improvements

### Control UI v2 (Complete Redesign)
- Modular views: overview, chat, config, agents, sessions
- Command palette for quick navigation
- Mobile-responsive layout with bottom tabs
- Slash commands in chat
- Search and export capabilities
- Pinned messages
- **Impact:** Much improved agent management and debugging experience

### Fast Mode (GPT-5.4 & Claude)
- Toggle per session with `/fast`
- Configurable defaults
- Maps to API provider priority tiers
- Works across TUI, Control UI, and ACP
- **Use Case:** Enable for time-sensitive agents (monitoring alerts), disable for background research

### Local Model Provider Plugin Architecture
- Ollama, vLLM, SGLang moved from hardcoded to plugin system
- Independent iteration cycles
- Cleaner Ollama setup
- **Note:** Test existing Ollama configs after update
- **Fix:** Local reasoning models (Qwen, etc.) no longer leak internal thinking into replies

### Browser Automation Enhancements
- Chrome DevTools MCP attach mode for live sessions
- New profiles: `profile="user"` (logged-in host browser) and `profile="chrome-relay"` (extension)
- Batched actions and delayed clicks for reliability
- Combined with Playwright and Camoufox = 3 browser automation paths

### sessions_yield Tool
- Orchestrator agents can end turn immediately and pass payload to next session
- Faster, cleaner multi-agent handoffs
- **Use Case:** Agent team coordination

---

## 🔧 Cron & Agent Operations Fixes

### Cron Reliability (v2026.3.13)
- **Ghost message fix:** Isolated cron sends no longer duplicate after gateway restart
- **Subagent timeout:** Completion announces have 90-second timeout (was infinite retry)
- **Deadlock prevention:** Compaction no longer deadlocks during scheduled jobs
- **Impact:** Removes constant annoyance for monitoring, backups, content schedules

### Gateway Improvements
- `openclaw gateway status --require-rpc` for automation hard-fail on probe misses
- Clearer Linux non-interactive daemon-install failure reporting
- macOS exec approvals respect per-agent settings with allowlist fallback
- WebSocket RPC timeout cleans up stalled connections
- Session reset preserves account/thread routing after `/reset`

---

## 🛠️ Platform-Specific Updates

### Telegram (v3.12/v3.13)
- Model picker persists selections correctly
- Validates fallback models
- IPv4 fallback for broken IPv6 hosts
- Webhook auth validates secrets before parsing

### Discord (v3.13)
- Gateway startup no longer crashes on transient metadata failures
- Allowlists properly handle raw guild IDs

### macOS (v3.13)
- Voice wake crash fix for speech segments from different transcript instances
- Reminders permission prompt works from OpenClaw.app

### Windows (v3.13)
- Gateway install, stop, status, and auth fixes

### Docker (v3.13)
- Timezone override via `OPENCLAW_TZ`

---

## 📊 Community & Ecosystem

- **GitHub:** 310,000+ stars, 47,700 forks, 600+ contributors
- **ClawHub:** 10,000+ skills
- **Notable:** Steinberger joined OpenAI (Feb 14, 2026), project handed to independent open-source foundation
- **China:** "Raise a lobster" craze - OpenClaw gaining massive traction in Chinese AI sector
- **New Integration:** Memori Labs OpenClaw plugin for persistent AI memory in multi-agent gateways

---

## ⚠️ Known Issues / Regressions

1. **Device pairing changes:** Reported regression with `openclaw devices list` on local loopback
   - **Workaround:** Check GitHub issues for updates
   
2. **Reverse proxy/auth layers:** Test Control UI after updating - WebSocket auth handled differently

3. **Ollama configs:** Migration "should be" seamless but verify after update

---

## 📋 Update Checklist

- [ ] Run: `npm update -g openclaw && openclaw gateway restart && openclaw doctor --fix`
- [ ] Verify version: `openclaw --version` (should be 2026.3.13)
- [ ] Test Control UI loads correctly
- [ ] Verify local models respond (Ollama/vLLM if used)
- [ ] Test critical integrations
- [ ] Fire test cron job to verify reliability
- [ ] Review gateway logs for security fix confirmation
- [ ] Rotate credentials if setup codes were previously shared

---

## 📚 References

- **Release Notes:** 
  - v2026.3.12: https://github.com/openclaw/openclaw/releases/tag/v2026.3.12
  - v2026.3.13: https://github.com/openclaw/openclaw/releases/tag/v2026.3.13
- **Security Advisories:**
  - GHSA-g353-mgv3-8pcj (Critical Auth Bypass)
  - GHSA-2rqg-gjgv-84jm (Workspace Escape)
  - GHSA-7h7g-x2px-94hj (Credential Exposure)
  - GHSA-r7vr-gr74-94p8 (Improper Authorization)
  - GHSA-vmhq-cqm9-6p7q (Browser Profile Auth)
  - GHSA-f5mf-3r52-r83w (Authorization Bypass)
  - GHSA-5m9r-p9g7-679c (Rate Limit Bypass)
  - GHSA-wcxr-59v9-rxr8 (Incorrect Authorization)

---

*Report generated by Aiden - OpenClaw Research Nightly Cron Job*
