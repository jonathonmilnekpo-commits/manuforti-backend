# Manu Forti Backend — Deployment Guide

## Local Development

```bash
cd manuforti-backend

# Install dependencies
npm install

# Set up PostgreSQL locally
# macOS with Homebrew:
brew install postgresql
brew services start postgresql

# Create database
createdb manuforti

# Copy environment file
cp .env.example .env
# Edit .env with your values

# Initialize database
npm run db:init

# Start development server
npm run dev
```

## Production Deployment Options

### Option 1: Railway (Recommended)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Add PostgreSQL
railway add --database postgres

# Deploy
railway up

# Set environment variables in Railway dashboard
```

### Option 2: Render

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repo
4. Add PostgreSQL database
5. Set environment variables
6. Deploy

### Option 3: Fly.io

```bash
# Install Fly CLI
brew install flyctl

# Launch app
fly launch

# Create database
fly postgres create

# Set secrets
fly secrets set STRIPE_SECRET_KEY=xxx VIPPS_CLIENT_ID=xxx ...

# Deploy
fly deploy
```

## Environment Variables for Production

Required:
- `DATABASE_URL` — PostgreSQL connection string
- `STRIPE_SECRET_KEY` — Stripe live key
- `STRIPE_WEBHOOK_SECRET` — Stripe webhook endpoint secret
- `SENDGRID_API_KEY` — SendGrid API key
- `ADMIN_API_KEY` — Secure random string for admin access

Optional:
- `VIPPS_CLIENT_ID` — For Norwegian mobile payments
- `VIPPS_CLIENT_SECRET`
- `VIPPS_SUBSCRIPTION_KEY`
- `VIPPS_MERCHANT_SERIAL_NUMBER`
- `S3_BUCKET` — For file uploads
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Webhook Configuration

### Stripe
1. Go to Stripe Dashboard → Developers → Webhooks
2. Add endpoint: `https://your-api.com/api/webhooks/stripe`
3. Select events: `payment_intent.succeeded`
4. Copy signing secret to `STRIPE_WEBHOOK_SECRET`

### Vipps
1. Configure callback URL in Vipps portal: `https://your-api.com/api/webhooks/vipps`

## Health Check

```bash
curl https://your-api.com/health
```

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2026-03-08T03:00:00.000Z",
  "version": "1.0.0"
}
```
