const axios = require('axios');
const logger = require('../utils/logger');

/**
 * Notify Aiden (Lead Agent) of order events
 * This sends webhooks to the Aiden notification endpoint
 */
async function notifyAiden(eventType, order) {
  const webhookUrl = process.env.AIDEN_WEBHOOK_URL;
  
  if (!webhookUrl) {
    logger.warn('AIDEN_WEBHOOK_URL not configured, skipping notification');
    return;
  }

  const payload = {
    event: eventType,
    timestamp: new Date().toISOString(),
    order: {
      reference: order.order_reference,
      tier: order.tier,
      price: order.price,
      status: order.order_status,
      payment_status: order.payment_status,
      customer: {
        name: order.customer_name,
        email: order.customer_email,
        company: order.company_name
      },
      supplier: {
        name: order.supplier_name,
        website: order.supplier_website,
        country: order.supplier_country
      },
      analysis_context: order.analysis_context,
      sla_deadline: order.sla_deadline
    }
  };

  try {
    await axios.post(webhookUrl, payload, {
      headers: {
        'X-Webhook-Secret': process.env.AIDEN_WEBHOOK_SECRET || '',
        'Content-Type': 'application/json'
      },
      timeout: 5000
    });

    logger.info(`Aiden notified: ${eventType} for ${order.order_reference}`);
  } catch (err) {
    logger.error('Failed to notify Aiden:', err.message);
    // Don't throw — notification failures shouldn't break the flow
  }
}

module.exports = { notifyAiden };