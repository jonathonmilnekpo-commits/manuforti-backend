---
date: 2026-03-23
topic: technical
tags: ['52808', 'technical']
---

# OpenClaw Updates Summary - March 23, 2026

**Report Date:** 2026-03-23  
**Current Version:** 2026.3.22 (stable) / 2026.3.22-beta.1 (pre-release)  
**Last Published:** 6 hours ago (npm)

---

## 🚨 CRITICAL SECURITY ALERTS

Multiple CVEs have been disclosed in the past week. **Immediate action recommended:**

### High Priority CVEs (Patch Immediately)

| CVE | Severity | Affected Versions | Impact |
|-----|----------|-------------------|--------|
| **CVE-2026-32051** | High | < 2026.3.1 | Authorization mismatch - operators can invoke owner-only tools (gateway, cron) |
| **CVE-2026-32042** | High | 2026.2.22 - 2026.2.25 | Privilege escalation - unpaired devices bypass operator pairing |
| **CVE-2026-32014** | Critical | Unspecified | Client-provided platform metadata injection |
| **CVE-2026-32015** | High | Unspecified | safeBins PATH hijacking - bypass allowlist checks |
| **CVE-2026-31999** | High | Unspecified | Wrapper resolution bypass in exec |
| **CVE-2026-31996** | High | Unspecified | File/directory traversal in working directory |
| **CVE-2026-31995** | Critical | Unspecified | Command execution via shell fallback |
| **CVE-2026-31992** | High | Unspecified | Shell/script wrapper creation during guard-protected runs |

### Patch Status
- **Fixed in:** 2026.3.22 and later
- **Action:** Upgrade immediately via `openclaw update`
- **Verify:** Run `openclaw doctor` after update

---

## 📦 Latest Releases

### Stable: v2026.3.22 (March 22, 2026)
Major release with security patches and breaking changes.

### Pre-release: v2026.3.22-beta.1 (March 23, 2026)
- No new macOS app build (macOS stays on 2026.3.22)
- Plugin install now prefers ClawHub before npm

---

## ⚠️ BREAKING CHANGES (v2026.3.22)

### 1. Plugin Installation Order
- **Change:** `openclaw plugins install <package>` now prefers **ClawHub** before npm
- **Impact:** Bare package names resolve to ClawHub first
- **Migration:** Use `npm:<package>` to force npm, or publish to ClawHub

### 2. Browser/Chrome MCP
- **Change:** Legacy Chrome extension relay path removed
- **Impact:** `driver: "extension"` and `browser.relayBindHost` no longer work
- **Migration:** Run `openclaw doctor --fix` to migrate to `existing-session` / `user` mode

### 3. Image Generation
- **Change:** Bundled `nano-banana-pro` skill removed
- **Migration:** Use `agents.defaults.imageGenerationModel.primary: "google/gemini-3-pro-image-preview"`

### 4. Plugin SDK
- **Change:** `openclaw/extension-api` removed
- **Migration:** Use `openclaw/plugin-sdk/*` subpaths
- **Docs:** https://docs.openclaw.ai/plugins/sdk-migration

### 5. Environment Variables
- **Change:** Legacy `CLAWDBOT_*` and `MOLTBOT_*` env names removed
- **Migration:** Use `OPENCLAW_*` prefixes

### 6. Gateway Auth (Breaking)
- **Change:** When both `gateway.auth.token` and `gateway.auth.password` are configured, explicit `gateway.auth.mode` is now required
- **Impact:** Gateway may fail to start without explicit auth mode

---

## ✨ New Features & Improvements

### Agent Operations
- **Subagent timeout handling:** Fixed false timeout reports when workers finish quickly
- **Anthropic thinking blocks:** Preserved during transcript image sanitization
- **Skill config resolution:** SecretRefs now resolve correctly during embedded startup

### Cron & Gateway
- **CVE-2026-32051 fix:** Owner-only tool surfaces (gateway, cron) now properly gated
- **Usage tracking:** Reset and deleted archived sessions now included in usage totals

### Browser & MCP
- **Chrome MCP:** Better session handling - waits for tabs to become usable after attach
- **CDP:** Reuses running loopback browser after short reachability miss (fixes Linux headless issues)

### ClawHub Integration
- Native `openclaw skills search|install|update` flows
- `openclaw plugins install clawhub:<package>` with tracked metadata
- macOS auth fixes for saved credentials

### Messaging
- **Telegram:** `asDocument` alias for `forceDocument` on image/GIF sends
- **Discord:** Explicit unauthorized replies for privileged slash commands
- **Feishu:** Fixed file/image attachment routing

### Models
- **Mistral:** Lowered max-token defaults to avoid 422 errors
- **OpenAI Codex OAuth:** Proxy support fixed for token refresh
- **Gemini 3.1 Flash-Lite:** First-class support added

---

## 🔧 Bug Fixes (v2026.3.22+)

- **Control UI:** Fixed 503 error after update (dist/control-ui/ missing from npm package #52808)
- **WhatsApp:** Doctor --fix no longer writes invalid plugin allowlist entries
- **Matrix:** New official matrix-js-sdk plugin (migration required from old plugin)
- **Memory-LanceDB:** Bootstrap on first use for global npm installs
- **Config:** Stale unknown plugins.allow ids now treated as warnings, not fatal errors

---

## 📊 Community Pulse

### Reddit Discussions (r/openclaw)
- Mixed reception to 2026.3.2+ releases - some users report UI/agent loading issues
- Security concerns remain a hot topic; community seeking alternatives with better security posture
- Weekly release cadence criticized by self-hosters for update fatigue
- "Mac Mini gold rush" commentary on hype-driven purchasing

### Notable Community Resources
- Microsoft security bulletin on running OpenClaw safely: https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/
- OpenClaw Security Monitor tool: https://github.com/adibirzu/openclaw-security-monitor

---

## 🎯 Recommendations for Our Deployment

### Immediate Actions
1. **Upgrade to 2026.3.22** - Patches critical CVEs affecting cron and gateway
2. **Run `openclaw doctor --fix`** - Migrates browser config, fixes Mistral settings
3. **Review gateway auth config** - Ensure explicit `gateway.auth.mode` is set
4. **Verify plugin installations** - May need to re-install from ClawHub vs npm

### Monitoring
- Watch for CVE-2026-32051 exploitation attempts (cron/gateway unauthorized access)
- Monitor for safeBins PATH hijacking attempts
- Review logs for "shell fallback" events

### Security Hardening
```bash
# Bind gateway to localhost only
openclaw config set gateway.bind localhost

# Enable authentication
openclaw config set gateway.auth.mode token

# Verify configuration
openclaw config get gateway.bind
openclaw config get gateway.auth.mode
```

---

## 📚 References

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- Changelog: https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md
- SDK Migration: https://docs.openclaw.ai/plugins/sdk-migration
- Security Overview: https://github.com/openclaw/openclaw/security

---

*Report generated by OpenClaw Research Agent - Nightly Cron Job*
