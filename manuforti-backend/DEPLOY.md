# Railway Deployment Guide

## 1. Push to GitHub

Create repo at https://github.com/new

```bash
cd ~/.openclaw/workspace/manuforti-backend
git remote add origin https://github.com/YOUR_USERNAME/manuforti-backend.git
git push -u origin main
```

## 2. Deploy to Railway

### Option A: Railway CLI
```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

### Option B: GitHub Integration
1. Go to https://railway.app
2. New Project → Deploy from GitHub repo
3. Select your manuforti-backend repo
4. Add PostgreSQL plugin (or use external DB)
5. Add environment variables (see below)

## 3. Required Environment Variables

```bash
# Server
NODE_ENV=production
PORT=3000

# Database (Railway provides this automatically if using their PostgreSQL)
DATABASE_URL=postgresql://...

# Email (SendGrid)
SENDGRID_API_KEY=SG.xxx
EMAIL_FROM=orders@manuforti.no
EMAIL_FROM_NAME="Manu Forti Intelligence"
JONATHON_EMAIL=Jonathon.Milne137@gmail.com

# Notifications (Aiden/OpenClaw)
# This will be your Railway app URL + /webhook/orders
# For testing locally: http://localhost:3000/webhook/orders
AIDEN_WEBHOOK_URL=https://your-railway-app.up.railway.app/webhook/orders

# Frontend (for CORS)
FRONTEND_URL=https://manuforti.no
```

## 4. Get SendGrid API Key

1. Sign up at https://sendgrid.com
2. Create API key with "Mail Send" permissions
3. Verify sender email (orders@manuforti.no)

## 5. Update Frontend

In `manuforti-website/order.html`, update the API_URL:

```javascript
const API_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api/orders' 
    : 'https://your-railway-app.up.railway.app/api/orders';
```

## 6. Test the Flow

1. Submit test order on website
2. Check: Customer receives confirmation email
3. Check: Jonathon receives notification email  
4. Check: Aiden receives webhook (terminal + Telegram)
5. Check: Order logged to memory file

## 7. Database Initialization

First deploy will fail until database is initialized. Run:

```bash
railway run npm run db:init
```

Or connect to Railway PostgreSQL and run the SQL from `scripts/init-db.js`

## Troubleshooting

**Orders not appearing?**
- Check Railway logs: `railway logs`
- Verify DATABASE_URL is set
- Check SendGrid API key is valid

**CORS errors?**
- Ensure FRONTEND_URL matches your actual website URL

**Emails not sending?**
- Verify sender email is verified in SendGrid
- Check SendGrid dashboard for blocked/bounced emails
