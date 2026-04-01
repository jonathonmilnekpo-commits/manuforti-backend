# OpenClaw Release Notes

## 2026.3.7 — March 7, 2026

**Source:** https://github.com/openclaw/openclaw/releases/tag/2026.3.7  
**Announcement:** https://x.com/openclaw/status/2030522386894946620

### Major Updates

| Feature | Description |
|---------|-------------|
| **GPT-5.4** | Latest OpenAI model support |
| **Gemini 3.1 Flash-Lite** | Google model integration |
| **ACP bindings survive restarts** | Persistent agent connections |
| **Slim Docker multi-stage builds** | Smaller, faster container images |
| **SecretRef for gateway auth** | Enhanced security for gateway authentication |
| **Pluggable context engines** | Modular context management |
| **HEIF image support** | High Efficiency Image Format support |
| **Zalo channel fixes** | Messaging platform improvements |

### Impact on Manu Forti

- **Agent stability:** ACP bindings surviving restarts means more reliable long-running Venture cron jobs
- **Security:** SecretRef improves credential management for payment integrations (Stripe/Vipps)
- **Performance:** Slim Docker builds reduce deployment time for backend API

---

## 2026.3.6 — March 6, 2026

Previous release. Baseline for Manu Forti development.

---

*Last Updated: March 8, 2026*
