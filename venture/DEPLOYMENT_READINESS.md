# Manu Forti Deployment Readiness Package

**Date:** March 17, 2026  
**Status:** 🟡 READY FOR DEPLOYMENT — Action Required  
**Target:** First paying customer within 48 hours of go decision

---

## Executive Summary

All code is complete and production-ready. This package contains everything needed to deploy the Manu Forti Intelligence platform and begin accepting orders.

**What's Ready:**
- ✅ Frontend website (3 products: Reports, Monitoring, Category Strategy)
- ✅ Backend API (Node.js/Express, PostgreSQL, Stripe/Vipps/Invoice payments)
- ✅ Order management system
- ✅ Email notifications (SendGrid)
- ✅ Aiden webhook integration

**What's Needed:**
- ⏳ Railway account creation (5 minutes)
- ⏳ Stripe account + test mode API keys (10 minutes)
- ⏳ SendGrid account + API key (5 minutes)
- ⏳ Domain configuration (optional for MVP)

**Time to First Order:** ~30 minutes after starting deployment

---

## Quick Start — Deploy in 30 Minutes

### Step 1: Create Accounts (10 minutes)

#### Railway (Hosting)
1. Go to https://railway.app
2. Sign up with GitHub
3. Verify email

#### Stripe (Payments)
1. Go to https://dashboard.stripe.com/register
2. Create account (skip "activate payments" for now — test mode only)
3. Get API keys from https://dashboard.stripe.com/test/apikeys
   - Publishable key: `pk_test_...`
   - Secret key: `sk_test_...`

#### SendGrid (Email)
1. Go to https://signup.sendgrid.com
2. Create free account
3. Create API key at https://app.sendgrid.com/settings/api_keys
   - Permission: "Mail Send"
   - Key: `SG.xxx`

### Step 2: Push Code to GitHub (5 minutes)

```bash
# From workspace root
cd /Users/jonathonmilne/.openclaw/workspace

# Initialize git (if not already)
git init
git add manuforti-backend/ manuforti-website/
git commit -m "Manu Forti v1.0 — Production ready"

# Create GitHub repo and push
git remote add origin https://github.com/YOUR_USERNAME/manuforti.git
git push -u origin main
```

### Step 3: Deploy Backend to Railway (10 minutes)

1. Railway Dashboard → "New Project" → "Deploy from GitHub repo"
2. Select `manuforti-backend` folder (or deploy entire repo and set root directory)
3. Click "New" → "Database" → "Add PostgreSQL"
4. Go to "Variables" tab, add:

```
NODE_ENV=production
ADMIN_API_KEY=mf_admin_$(openssl rand -hex 16)
DATABASE_URL=${{Postgres.DATABASE_URL}}  # Auto-populated

# Stripe (TEST MODE — use test keys for now)
STRIPE_SECRET_KEY=sk_test_your_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_key_here
STRIPE_WEBHOOK_SECRET=whsec_placeholder  # Will update after webhook setup

# SendGrid
SENDGRID_API_KEY=SG.your_key_here
EMAIL_FROM=orders@manuforti.com
EMAIL_FROM_NAME=Manu Forti Intelligence

# Frontend
FRONTEND_URL=https://your-username.github.io/manuforti-website

# Aiden webhook (optional — for order notifications)
AIDEN_WEBHOOK_URL=https://your-openclaw-instance.com/webhooks/orders
AIDEN_WEBHOOK_SECRET=$(openssl rand -hex 32)
```

5. Deploy: Railway auto-deploys on push, or click "Deploy"
6. Get your API URL: `https://manuforti-api.railway.app`

### Step 4: Configure Stripe Webhooks (5 minutes)

1. Stripe Dashboard → Developers → Webhooks → "Add endpoint"
2. Endpoint URL: `https://manuforti-api.railway.app/api/webhooks/stripe`
3. Select events:
   - `payment_intent.succeeded`
   - `payment_intent.payment_failed`
4. Copy "Signing secret" (starts with `whsec_`)
5. Update Railway variable: `STRIPE_WEBHOOK_SECRET=whsec_...`
6. Redeploy

### Step 5: Update Frontend Config (2 minutes)

Edit `manuforti-website/config.js`:

```javascript
const CONFIG = {
    API_BASE_URL: 'https://manuforti-api.railway.app/api',
    STRIPE_PUBLISHABLE_KEY: 'pk_test_your_actual_key_here',
    // ... rest unchanged
};
```

Commit and push — GitHub Pages auto-deploys.

### Step 6: Test the Flow (5 minutes)

```bash
# Health check
curl https://manuforti-api.railway.app/health

# Test order creation
curl -X POST https://manuforti-api.railway.app/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "product_type": "report",
    "tier": "Standard",
    "price": 249,
    "payment_method": "Stripe",
    "customer_name": "Test User",
    "customer_email": "test@example.com",
    "company_name": "Test Corp",
    "supplier_name": "Test Supplier",
    "sla_hours": 24
  }'
```

---

## Production Checklist

### Pre-Launch

- [ ] Railway account created
- [ ] Backend deployed and healthy (`/health` returns 200)
- [ ] PostgreSQL database connected
- [ ] Stripe test mode keys configured
- [ ] Stripe webhooks configured and receiving events
- [ ] SendGrid API key configured
- [ ] Test email sent successfully
- [ ] Frontend config.js updated with production API URL
- [ ] Frontend deployed (GitHub Pages or Railway static)
- [ ] Test order placed end-to-end
- [ ] Test payment processed (Stripe test card: `4242 4242 4242 4242`)
- [ ] Order appears in admin dashboard
- [ ] Email notification received

### Post-Launch (Before First Real Customer)

- [ ] Switch Stripe to live mode (apply for activation)
- [ ] Update Stripe keys to live (`sk_live_`, `pk_live_`)
- [ ] Configure custom domain (optional)
- [ ] Set up Vipps (Norwegian customers) — apply at vipps.no
- [ ] Configure invoice payment method (manual process)
- [ ] Document order fulfillment workflow
- [ ] Train Jonathon on admin dashboard

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         CUSTOMER                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │  GitHub Pages   │    │   Order Form    │    │   Payment   │  │
│  │  (Static Site)  │───▶│   (order.html)  │───▶│   (Stripe)  │  │
│  └─────────────────┘    └─────────────────┘    └──────┬──────┘  │
│           │                                           │          │
│           │    ┌──────────────────────────────────────┘          │
│           │    │                                                  │
│           ▼    ▼                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │              Railway (Node.js + PostgreSQL)               │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐   │    │
│  │  │  API Server │  │   Orders    │  │   Payments      │   │    │
│  │  │  (Express)  │  │   (CRUD)    │  │ (Stripe/Vipps)  │   │    │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────────┘   │    │
│  │         │                │                                 │    │
│  │         ▼                ▼                                 │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐   │    │
│  │  │  Database   │  │   Email     │  │  Aiden Webhook  │   │    │
│  │  │ (PostgreSQL)│  │  (SendGrid) │  │  (Notification) │   │    │
│  │  └─────────────┘  └─────────────┘  └─────────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## File Structure

```
workspace/
├── manuforti-backend/           # Node.js API
│   ├── server.js               # Express entry point
│   ├── routes/
│   │   ├── orders.js          # Order CRUD
│   │   ├── payments.js        # Stripe/Vipps handlers
│   │   ├── webhooks.js        # Payment confirmations
│   │   └── admin.js           # Admin dashboard
│   ├── services/
│   │   ├── stripe.js          # Stripe integration
│   │   ├── vipps.js           # Vipps integration
│   │   ├── email.js           # SendGrid emails
│   │   └── notifications.js   # Aiden webhooks
│   ├── models/
│   │   └── order.js           # Order data model
│   └── scripts/
│       └── init-db.js         # Database setup
├── manuforti-website/          # Frontend
│   ├── index.html             # Homepage
│   ├── order.html             # Order form (all products)
│   ├── payment.html           # Stripe checkout
│   ├── order-success.html     # Confirmation
│   ├── academy.html           # Product 2 landing
│   ├── category-strategy.html # Product 3 landing
│   └── config.js              # API configuration
└── venture/
    ├── DEPLOYMENT_READINESS.md # This file
    └── CUSTOMER_ONBOARDING.md  # Order fulfillment guide
```

---

## Environment Variables Reference

| Variable | Required | Description | Source |
|----------|----------|-------------|--------|
| `NODE_ENV` | Yes | `production` | Set manually |
| `PORT` | No | Server port (default: 3000) | Railway sets this |
| `DATABASE_URL` | Yes | PostgreSQL connection string | Railway auto-generates |
| `ADMIN_API_KEY` | Yes | Secret for admin endpoints | Generate: `openssl rand -hex 16` |
| `STRIPE_SECRET_KEY` | Yes | Stripe secret (test or live) | Stripe Dashboard |
| `STRIPE_PUBLISHABLE_KEY` | Yes | Stripe publishable key | Stripe Dashboard |
| `STRIPE_WEBHOOK_SECRET` | Yes | Webhook signing secret | Stripe Dashboard → Webhooks |
| `SENDGRID_API_KEY` | Yes | SendGrid API key | SendGrid Dashboard |
| `EMAIL_FROM` | Yes | Sender email address | Set manually |
| `EMAIL_FROM_NAME` | Yes | Sender display name | Set manually |
| `FRONTEND_URL` | Yes | Frontend origin for CORS | Your GitHub Pages URL |
| `AIDEN_WEBHOOK_URL` | No | OpenClaw webhook endpoint | Your OpenClaw instance |
| `AIDEN_WEBHOOK_SECRET` | No | Webhook verification secret | Generate manually |
| `VIPPS_*` | No | Vipps API credentials | Vipps Developer Portal |

---

## Testing Procedures

### 1. Health Check
```bash
curl https://your-api.railway.app/health
```
Expected: `{"status":"ok","timestamp":"...","version":"1.0.0"}`

### 2. Create Test Order
```bash
curl -X POST https://your-api.railway.app/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "product_type": "report",
    "tier": "Standard",
    "price": 249,
    "payment_method": "Stripe",
    "customer_name": "Test Customer",
    "customer_email": "test@example.com",
    "company_name": "Test Corp",
    "supplier_name": "Test Supplier AS",
    "sla_hours": 24
  }'
```
Expected: Order object with `id`, `status: "pending_payment"`

### 3. Test Stripe Payment (Test Mode)
Use Stripe test card: `4242 4242 4242 4242`
- Any future expiry date
- Any 3-digit CVC
- Any ZIP code

### 4. Verify Webhook
Check Railway logs: Should show `payment_intent.succeeded` event processed

### 5. Verify Email
Check SendGrid activity log: Should show email sent to customer

### 6. Admin Dashboard
```bash
curl https://your-api.railway.app/api/admin/orders \
  -H "X-API-Key: your_admin_api_key"
```

---

## Troubleshooting

### Database Connection Errors
- Check `DATABASE_URL` is set
- Ensure database is in same region as app
- Test: `railway connect postgres` → `\dt`

### Stripe Webhook Failures
- Verify webhook URL is publicly accessible
- Check `STRIPE_WEBHOOK_SECRET` matches Stripe dashboard
- Look at Railway logs for signature verification errors

### CORS Errors
- Verify `FRONTEND_URL` matches actual frontend origin
- Check for trailing slashes (should not have)

### Email Not Sending
- Verify SendGrid API key is valid (not expired)
- Check SendGrid activity log for bounces/blocks
- Verify sender domain is authenticated (or use generic @sendgrid.net)

---

## Cost Estimates

### Railway (Recommended)
| Component | Plan | Cost/Month |
|-----------|------|------------|
| PostgreSQL | Starter | $5 |
| Compute | Starter (512MB) | $5 |
| **Total** | | **~$10** |

### Render (Free Alternative)
| Component | Plan | Cost/Month |
|-----------|------|------------|
| PostgreSQL | Free | $0 |
| Web Service | Free | $0 |
| **Total** | | **$0** |

### Stripe
- No monthly fee
- 2.9% + 30¢ per transaction
- Example: €249 order = ~€7.50 fee

### SendGrid
- Free tier: 100 emails/day
- Paid: $14.95/month for 50K emails

---

## Next Steps After Deployment

1. **First Customer Protocol** — See `CUSTOMER_ONBOARDING.md`
2. **Monitor Orders** — Check admin dashboard daily
3. **Collect Feedback** — Ask first customers for testimonials
4. **Iterate** — Improve based on real usage
5. **Scale** — Upgrade Railway plan when needed

---

## Emergency Contacts

- **Railway Support:** https://railway.app/help
- **Stripe Support:** https://support.stripe.com
- **SendGrid Support:** https://support.sendgrid.com
- **Aiden (Jonathon's Agent):** Available via OpenClaw

---

**Document Version:** 1.0  
**Last Updated:** March 17, 2026  
**Maintained By:** Venture Agent
