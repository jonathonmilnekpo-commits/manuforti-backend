const express = require('express');
const router = express.Router();

const stripeService = require('../services/stripe');
const vippsService = require('../services/vipps');
const Order = require('../models/order');
const logger = require('../utils/logger');

// Create Stripe payment intent
router.post('/stripe/create', async (req, res, next) => {
  try {
    const { order_reference, email } = req.body;

    const order = await Order.findByReference(order_reference);
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    const paymentIntent = await stripeService.createPaymentIntent({
      amount: order.price,
      currency: 'usd',
      orderReference: order_reference,
      email: email || order.customer_email
    });

    res.json({
      client_secret: paymentIntent.client_secret,
      publishable_key: process.env.STRIPE_PUBLISHABLE_KEY
    });
  } catch (err) {
    next(err);
  }
});

// Create Vipps payment
router.post('/vipps/create', async (req, res, next) => {
  try {
    const { order_reference, phone_number } = req.body;

    const order = await Order.findByReference(order_reference);
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    const payment = await vippsService.createPayment({
      orderReference: order_reference,
      amount: order.price,
      phoneNumber: phone_number,
      description: `Manu Forti ${order.tier} Report - ${order.supplier_name}`
    });

    res.json({
      redirect_url: payment.redirectUrl,
      reference: payment.reference
    });
  } catch (err) {
    next(err);
  }
});

// Create invoice payment
router.post('/invoice/create', async (req, res, next) => {
  try {
    const { order_reference } = req.body;

    const order = await Order.findByReference(order_reference);
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    // For invoice, we activate immediately but mark for manual follow-up
    await Order.updatePaymentStatus(order_reference, 'invoice_pending');

    // Send invoice email
    const { sendInvoiceEmail } = require('../services/email');
    await sendInvoiceEmail(order);

    res.json({
      success: true,
      message: 'Invoice will be sent within 24 hours',
      terms: '14 days payment terms'
    });
  } catch (err) {
    next(err);
  }
});

module.exports = router;