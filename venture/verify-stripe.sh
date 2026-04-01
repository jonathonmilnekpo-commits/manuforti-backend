#!/bin/bash
# Stripe Test Mode Verification Script
# Run this after deployment to verify Stripe integration

echo "🔍 Manu Forti Stripe Test Mode Verification"
echo "=========================================="
echo ""

# Configuration
API_URL="${API_URL:-https://manuforti-api.railway.app}"
FRONTEND_URL="${FRONTEND_URL:-https://jonathonmilne.github.io/manuforti-website}"

echo "Testing against:"
echo "  API: $API_URL"
echo "  Frontend: $FRONTEND_URL"
echo ""

# Test 1: Health Check
echo "1️⃣  Testing API Health..."
HEALTH=$(curl -s "$API_URL/health")
if echo "$HEALTH" | grep -q '"status":"ok"'; then
    echo "   ✅ API is healthy"
else
    echo "   ❌ API health check failed"
    echo "   Response: $HEALTH"
    exit 1
fi
echo ""

# Test 2: Create Test Order
echo "2️⃣  Creating test order..."
ORDER_RESPONSE=$(curl -s -X POST "$API_URL/api/orders" \
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
  }')

ORDER_ID=$(echo "$ORDER_RESPONSE" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

if [ -n "$ORDER_ID" ]; then
    echo "   ✅ Order created: $ORDER_ID"
else
    echo "   ❌ Failed to create order"
    echo "   Response: $ORDER_RESPONSE"
    exit 1
fi
echo ""

# Test 3: Create Stripe Payment Intent
echo "3️⃣  Creating Stripe Payment Intent..."
PAYMENT_RESPONSE=$(curl -s -X POST "$API_URL/api/payments/stripe/create-intent" \
  -H "Content-Type: application/json" \
  -d "{
    \"order_id\": \"$ORDER_ID\",
    \"amount\": 24900,
    \"currency\": \"eur\"
  }")

CLIENT_SECRET=$(echo "$PAYMENT_RESPONSE" | grep -o '"client_secret":"[^"]*"' | cut -d'"' -f4)

if [ -n "$CLIENT_SECRET" ]; then
    echo "   ✅ Payment Intent created"
    echo "   Client Secret: ${CLIENT_SECRET:0:20}..."
else
    echo "   ❌ Failed to create Payment Intent"
    echo "   Response: $PAYMENT_RESPONSE"
    exit 1
fi
echo ""

# Test 4: Verify Webhook Endpoint
echo "4️⃣  Checking webhook endpoint..."
WEBHOOK_CHECK=$(curl -s -o /dev/null -w "%{http_code}" "$API_URL/api/webhooks/stripe" -X POST)
if [ "$WEBHOOK_CHECK" = "400" ] || [ "$WEBHOOK_CHECK" = "401" ]; then
    echo "   ✅ Webhook endpoint accessible (returns $WEBHOOK_CHECK as expected without signature)"
else
    echo "   ⚠️  Webhook endpoint returned $WEBHOOK_CHECK (may need configuration)"
fi
echo ""

# Test 5: Check Admin Endpoint
echo "5️⃣  Checking admin endpoint (requires API key)..."
ADMIN_CHECK=$(curl -s -o /dev/null -w "%{http_code}" "$API_URL/api/admin/orders")
if [ "$ADMIN_CHECK" = "401" ]; then
    echo "   ✅ Admin endpoint protected (returns 401 without key)"
else
    echo "   ⚠️  Admin endpoint returned $ADMIN_CHECK"
fi
echo ""

echo "=========================================="
echo "✅ Stripe Test Mode Verification Complete!"
echo ""
echo "Next steps:"
echo "1. Configure Stripe webhook in dashboard:"
echo "   URL: $API_URL/api/webhooks/stripe"
echo "   Events: payment_intent.succeeded, payment_intent.payment_failed"
echo ""
echo "2. Test payment flow manually:"
echo "   - Visit: $FRONTEND_URL/order.html"
echo "   - Select 'Standard Report' + 'Card' payment"
echo "   - Use test card: 4242 4242 4242 4242"
echo "   - Any future expiry, any CVC"
echo ""
echo "3. Verify order appears in admin dashboard"
echo ""
