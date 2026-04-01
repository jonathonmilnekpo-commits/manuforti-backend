# Manu Forti Backend — Quick Deploy Guide

## Option 1: Railway Dashboard (Easiest - 5 minutes)

### Step 1: Create Railway Account
1. Go to https://railway.app
2. Sign up with GitHub
3. Verify email

### Step 2: Create Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. If repo not connected, click "Configure GitHub App" and grant access
4. Select your repository (or create one with this backend code)

### Step 3: Add PostgreSQL Database
1. Click "New" → "Database" → "Add PostgreSQL"
2. Railway automatically creates the database and sets `DATABASE_URL`

### Step 4: Deploy
1. Railway auto-detects Node.js and deploys
2. Click "Deploy" if manual deploy needed
3. Wait for build to complete (2-3 minutes)

### Step 5: Set Environment Variables
In Railway Dashboard → Variables tab, add:

```
# Required for basic operation
NODE_ENV=production
ADMIN_API_KEY=your_secure_random_string_here

# Stripe (get from https://dashboard.stripe.com/apikeys)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# SendGrid (get from https://app.sendgrid.com/settings/api_keys)
SENDGRID_API_KEY=SG.xxx
EMAIL_FROM=orders@manuforti.com
EMAIL_FROM_NAME=Manu Forti Intelligence

# Frontend URL (your website)
FRONTEND_URL=https://manuforti.com

# Optional: Aiden webhook for order notifications
AIDEN_WEBHOOK_URL=https://your-openclaw-instance.com/webhooks/orders
AIDEN_WEBHOOK_SECRET=your_webhook_secret

# Optional: Vipps (Norwegian payments)
VIPPS_CLIENT_ID=...
VIPPS_CLIENT_SECRET=...
VIPPS_SUBSCRIPTION_KEY=...
VIPPS_MERCHANT_SERIAL_NUMBER=...
VIPPS_BASE_URL=https://api.vipps.no
```

### Step 6: Initialize Database
1. Go to Railway Dashboard → your service → "Shell" tab
2. Run: `npm run db:init`
3. Check logs for "Database initialized successfully"

### Step 7: Test Health Endpoint
Your API URL will be: `https://your-service.railway.app`

Test: `curl https://your-service.railway.app/health`

Expected:
```json
{"status":"ok","timestamp":"2026-03-10T...","version":"1.0.0"}
```

---

## Option 2: Render (Free Alternative)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial backend commit"
git push origin main
```

### Step 2: Create Render Services
1. Go to https://render.com
2. Click "New" → "Web Service"
3. Connect your GitHub repo
4. Settings:
   - **Name:** manuforti-api
   - **Runtime:** Node
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`
   - **Plan:** Free

### Step 3: Create PostgreSQL Database
1. Click "New" → "PostgreSQL"
2. Name: manuforti-db
3. Plan: Free
4. Copy the "Internal Database URL"

### Step 4: Set Environment Variables
In Render Dashboard → Environment, add all variables from Option 1, using the Internal Database URL for `DATABASE_URL`.

### Step 5: Deploy
Click "Manual Deploy" → "Deploy latest commit"

---

## Option 3: Fly.io (Global Edge Network)

### Prerequisites
```bash
brew install flyctl
fly auth login
```

### Deploy
```bash
cd manuforti-backend

# Launch app
fly launch --name manuforti-api --region arn

# Create database
fly postgres create --name manuforti-db

# Attach database to app
fly postgres attach manuforti-db

# Set secrets
fly secrets set STRIPE_SECRET_KEY=xxx SENDGRID_API_KEY=xxx ...

# Deploy
fly deploy
```

---

## Post-Deployment Checklist

### 1. Configure Stripe Webhooks
1. Go to https://dashboard.stripe.com/webhooks
2. Add endpoint: `https://your-api.com/api/webhooks/stripe`
3. Select events: `payment_intent.succeeded`, `payment_intent.payment_failed`
4. Copy signing secret → set as `STRIPE_WEBHOOK_SECRET`

### 2. Configure SendGrid
1. Go to https://app.sendgrid.com/settings/sender_auth
2. Authenticate your domain (manuforti.com)
3. Create API key with "Mail Send" permissions

### 3. Test Order Flow
```bash
# Create test order
curl -X POST https://your-api.com/api/orders \
  -H "Content-Type: application/json" \
  -d '{
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

### 4. Update Frontend
Edit `manuforti-website/order.html`:
```javascript
const API_BASE_URL = 'https://your-api.com';
```

---

## Troubleshooting

### Database connection errors
- Check `DATABASE_URL` is set correctly
- Ensure database is in same region as app
- Try: `railway connect postgres` to test connection

### Stripe webhooks not working
- Verify webhook URL is publicly accessible
- Check `STRIPE_WEBHOOK_SECRET` matches Stripe dashboard
- Look at Railway logs for webhook errors

### Emails not sending
- Verify SendGrid API key is valid
- Check sender domain is authenticated
- Look at SendGrid activity log

---

## Cost Estimates

| Platform | Database | Compute | Total/Month |
|----------|----------|---------|-------------|
| Railway | $5 (starter) | $5 (starter) | ~$10 |
| Render | Free | Free | $0 |
| Fly.io | $1.94 (shared) | $1.94 (shared) | ~$4 |

**Recommendation:** Start with Render (free), upgrade to Railway when you need more resources.
