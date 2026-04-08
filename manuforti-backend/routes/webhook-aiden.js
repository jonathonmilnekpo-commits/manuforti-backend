const express = require('express');
const router = express.Router();
const { notifyTelegram, logToTerminal } = require('../utils/notifications');

/**
 * Order Webhook Endpoint
 * Receives notifications from Manu Forti backend when new orders are placed
 * 
 * POST /webhook/orders
 * Headers: X-Webhook-Secret (optional validation)
 */
router.post('/orders', async (req, res) => {
  try {
    const { event, order } = req.body;
    
    if (!order || !order.reference) {
      return res.status(400).json({ error: 'Invalid payload' });
    }
    
    // Log to terminal immediately
    logToTerminal(`
╔══════════════════════════════════════════════════════════════╗
║  🛎️  NEW ORDER RECEIVED                                        ║
╠══════════════════════════════════════════════════════════════╣
║  Reference: ${order.reference.padEnd(48)} ║
║  Product:  ${(order.product_type || 'report').toUpperCase().padEnd(48)} ║
║  Customer: ${order.customer?.name?.padEnd(48) || 'N/A'.padEnd(48)} ║
║  Company:  ${order.customer?.company?.padEnd(48) || 'N/A'.padEnd(48)} ║
║  Amount:   €${String(order.price || 0).padEnd(47)} ║
╚══════════════════════════════════════════════════════════════╝
    `);
    
    // Build notification message
    const isCategoryStrategy = order.product_type === 'category_strategy';
    const isMonitoring = order.product_type === 'monitoring';
    
    let productLabel = 'Supplier Report';
    if (isCategoryStrategy) productLabel = 'Category Strategy';
    if (isMonitoring) productLabel = 'Media Monitoring';
    
    const telegramMessage = `
🛎️ <b>NEW ORDER — ${order.reference}</b>

<b>${productLabel}</b>
👤 ${order.customer?.name || 'N/A'}
🏢 ${order.customer?.company || 'N/A'}
📧 ${order.customer?.email || 'N/A'}
💶 €${order.price || 0}

${order.supplier?.name ? `🔍 Supplier: ${order.supplier.name}` : ''}
${order.category_name ? `📊 Category: ${order.category_name}` : ''}

⏰ <i>Send invoice within 24h</i>
    `.trim();
    
    // Send Telegram notification
    try {
      await notifyTelegram(telegramMessage);
    } catch (err) {
      console.error('Telegram notification failed:', err.message);
    }
    
    // Log to order tracking system
    const orderRecord = {
      reference: order.reference,
      product_type: order.product_type || 'report',
      tier: order.tier,
      price: order.price,
      customer_name: order.customer?.name,
      customer_email: order.customer?.email,
      company_name: order.customer?.company,
      supplier_name: order.supplier?.name,
      category_name: order.category_name,
      received_at: new Date().toISOString(),
      status: 'received',
      actions: ['Send invoice within 24h', 'Begin fulfillment workflow']
    };
    
    // Append to daily memory log
    const fs = require('fs');
    const path = require('path');
    const today = new Date().toISOString().split('T')[0];
    const memoryFile = path.join(process.cwd(), 'memory', `${today}.md`);
    
    const orderLogEntry = `
## Order Received — ${order.reference} — ${new Date().toLocaleTimeString('en-GB')}

- **Product:** ${productLabel}
- **Customer:** ${order.customer?.name} (${order.customer?.email})
- **Company:** ${order.customer?.company}
- **Amount:** €${order.price}
- **Status:** Invoice pending

**Next Actions:**
- [ ] Send invoice within 24h
- [ ] Confirm payment received
- [ ] Begin fulfillment

---
`;
    
    try {
      fs.appendFileSync(memoryFile, orderLogEntry);
      console.log(`Order logged to memory: ${memoryFile}`);
    } catch (err) {
      console.error('Failed to log order to memory:', err.message);
    }
    
    // Respond to backend
    res.status(200).json({ 
      success: true, 
      message: 'Order notification received',
      reference: order.reference
    });
    
  } catch (err) {
    console.error('Webhook error:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Health check endpoint
 */
router.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

module.exports = router;
