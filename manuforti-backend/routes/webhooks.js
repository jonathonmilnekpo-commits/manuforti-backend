const express = require('express');
const router = express.Router();

const stripeService = require('../services/stripe');
const vippsService = require('../services/vipps');
const Order = require('../models/order');
const { notifyAiden } = require('../services/notifications');
const logger = require('../utils/logger');

// Stripe webhook
router.post('/stripe', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];

  try {
    const event = stripeService.constructEvent(req.body, sig);

    logger.info(`Stripe webhook received: ${event.type}`);

    if (event.type === 'payment_intent.succeeded') {
      const paymentIntent = event.data.object;
      const orderReference = paymentIntent.metadata.order_reference;

      if (orderReference) {
        const order = await Order.updatePaymentStatus(orderReference, 'paid', paymentIntent.id);
        
        logger.info(`Payment confirmed for order: ${orderReference}`);

        // Notify Aiden of payment
        await notifyAiden('payment_received', order);
      }
    }

    res.json({ received: true });
  } catch (err) {
    logger.error('Stripe webhook error:', err);
    res.status(400).send(`Webhook Error: ${err.message}`);
  }
});

// Vipps webhook
router.post('/vipps', async (req, res) => {
  try {
    const { reference, status } = req.body;

    logger.info(`Vipps webhook received: ${reference} - ${status}`);

    if (status === 'AUTHORIZED' || status === 'CAPTURED') {
      // Find order by Vipps reference
      const order = await Order.findByReference(reference);
      
      if (order) {
        await Order.updatePaymentStatus(order.order_reference, 'paid', reference);
        
        logger.info(`Vipps payment confirmed for order: ${order.order_reference}`);

        // Notify Aiden
        await notifyAiden('payment_received', order);
      }
    }

    res.json({ received: true });
  } catch (err) {
    logger.error('Vipps webhook error:', err);
    res.status(400).json({ error: err.message });
  }
});

module.exports = router;