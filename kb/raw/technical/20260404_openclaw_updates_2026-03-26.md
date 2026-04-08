---
date: 2026-03-26
topic: technical
tags: ['technical']
---

# OpenClaw Updates Summary (2026-03-26)

## New Releases
- **v2026.3.22** (released 2026-03-23)
- **v2026.3.23** (released 2026-03-??)
- **npm version 2026.3.23-2** published 2026-03-25

## Key Changes
### Breaking
- `openclaw plugins install <package>` now prefers **ClawHub** before npm for npm-safe names, falling back to npm only if ClawHub lacks the package/version.
- **Browser/Chrome MCP**: legacy Chrome extension relay path, bundled extension assets, driver: "extension", and `browser.relayBindHost` removed. Run `openclaw doctor --fix` to migrate host-local browser config.
- **Tools/image generation**: standardized stock image create/edit path on core `image_generate` tool; old nano-banana-pro docs/examples removed.

### Changes & Features
- **ModelStudio/Qwen**: added standard (pay-as-you-go) DashScope endpoints for China/global Qwen API keys; provider group relabeled to Qwen (Alibaba Cloud Model Studio).
- **UI/clarity**: consolidated button primitives, refined Knot theme (black‑red, WCAG 2.1 AA), added config icons, replaced roundness slider with discrete stops, improved aria‑labels.
- **CSP/Control UI**: compute SHA‑256 hashes for inline blocks in served `index.html`; include them in `script-src` CSP directive, keeping inline scripts blocked by default while allowing explicitly hashed bootstrap code.
- **Bundled plugin runtimes**: ship sidecars for WhatsApp, Matrix, and other plug‑ins to improve reliability.
- **ClawHub** becomes default plugin store, with improved install/uninstall handling.

## Security
- Recent blog (blink.new, 2026-03-25) states: **patching to v2026.3.12 closes all currently disclosed 2026 CVEs**. The latest releases (v2026.3.22/23) include these fixes.
- No new critical CVEs reported in the last 24 hours.
- CSP hardening mitigates inline‑script XSS risks.
- Plugin source shift to ClawHub reduces risk of malicious npm packages (ClawHub now includes code‑signing and stricter vetting).

## New Capabilities
- **Jentic Mini** launched 2026-03-25: a free, open‑source permission firewall for OpenClaw agents.
  - Fine‑grained permissions, credential control, single killswitch that instantly shuts down agent data access.
  - Enables safe connection to an AI‑curated catalog of >10,000 APIs/workflows.
- Mentioned in OpenClaw News (Mar 25/26): China’s “Lobster Raising” security guidelines for OpenClaw users.

## Impact on Cron Jobs & Agent Operations
- **Plugin installs** in cron jobs should now target ClawHub first; ensure ClawHub accessibility from cron environment.
- **CSP changes** may affect any custom HTML/JS served via OpenClaw’s Control UI; ensure inline scripts are hashed if needed.
- **Browser automation** updates: legacy Chrome extension relay removed; if your cron jobs rely on the old relay, migrate to `openclaw doctor --fix` and use existing‑session/user or raw CDP flows.
- **Bundled runtimes** improve stability of WhatsApp, Matrix, etc., benefiting cron jobs that use those channels.
- **Image generation tool** path change: update any skills or cron jobs that reference the old `nano-banana-pro` config to use `agents.defaults.imageGenerationModel` or install a dedicated skill.

## Recommendations
1. Update OpenClaw to at least v2026.3.22 (or npm 2026.3.23-2) to receive security patches.
2. Review cron job plugin install commands; adjust to prefer ClawHub or explicitly specify npm if needed.
3. If you use the Control UI with custom inline scripts, compute SHA‑256 hashes and add them to CSP config.
4. Consider evaluating Jentic Mini for additional agent‑level permission controls.
5. Monitor ClawHub for plugin updates and security advisories.