# Manu Forti Backend API

Order management and payment processing backend for Manu Forti Intelligence.

## Quick Start

```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Initialize database
npm run db:init

# Start server
npm run dev
```

## Environment Variables

```bash
# Server
PORT=3000
NODE_ENV=development

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/manuforti

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Vipps
VIPPS_CLIENT_ID=...
VIPPS_CLIENT_SECRET=...
VIPPS_SUBSCRIPTION_KEY=...
VIPPS_MERCHANT_SERIAL_NUMBER=...
VIPPS_BASE_URL=https://apitest.vipps.no

# SendGrid
SENDGRID_API_KEY=SG.xxx
EMAIL_FROM=orders@manuforti.com

# Aiden Notification
AIDEN_WEBHOOK_URL=https://...
AIDEN_WEBHOOK_SECRET=...

# File Storage
S3_BUCKET=manuforti-uploads
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

## API Endpoints

### Orders
- `POST /api/orders` — Create new order
- `GET /api/orders/:reference` — Get order status
- `GET /api/orders/:reference/status` — Check order status (public)

### Payments
- `POST /api/payments/stripe/create` — Create Stripe payment intent
- `POST /api/webhooks/stripe` — Stripe webhook
- `POST /api/webhooks/vipps` — Vipps webhook

### Admin
- `GET /api/admin/orders` — List all orders (auth required)
- `POST /api/admin/orders/:reference/activate` — Manually activate order

## Order Status Flow

```
received → pending_payment → paid → processing → completed
                    ↓
                cancelled
```

## Payment Methods

| Method | Flow | Status |
|--------|------|--------|
| Stripe | Payment Intent → Confirm → Webhook | Ready |
| Vipps | ePayment → Redirect → Webhook | Ready |
| Invoice | Create → Email → Manual confirm | Ready |
