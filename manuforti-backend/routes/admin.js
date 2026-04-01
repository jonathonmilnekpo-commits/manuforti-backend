const express = require('express');
const router = express.Router();

const Order = require('../models/order');
const logger = require('../utils/logger');

// Admin authentication middleware
const adminAuth = (req, res, next) => {
  const apiKey = req.headers['x-api-key'];
  
  if (!apiKey || apiKey !== process.env.ADMIN_API_KEY) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  
  next();
};

// List all orders
router.get('/orders', adminAuth, async (req, res, next) => {
  try {
    const limit = parseInt(req.query.limit) || 50;
    const offset = parseInt(req.query.offset) || 0;

    const orders = await Order.listAll(limit, offset);

    res.json({
      count: orders.length,
      orders: orders.map(o => ({
        reference: o.order_reference,
        tier: o.tier,
        price: o.price,
        status: o.order_status,
        payment_status: o.payment_status,
        customer: o.customer_name,
        company: o.company_name,
        supplier: o.supplier_name,
        created_at: o.created_at,
        sla_deadline: o.sla_deadline
      }))
    });
  } catch (err) {
    next(err);
  }
});

// Get pending orders (for Aiden dashboard)
router.get('/orders/pending', adminAuth, async (req, res, next) => {
  try {
    const orders = await Order.getPendingOrders();

    res.json({
      count: orders.length,
      orders: orders.map(o => ({
        reference: o.order_reference,
        tier: o.tier,
        supplier: o.supplier_name,
        customer: o.customer_email,
        sla_deadline: o.sla_deadline,
        time_remaining: Math.round((new Date(o.sla_deadline) - new Date()) / (1000 * 60 * 60)) + ' hours'
      }))
    });
  } catch (err) {
    next(err);
  }
});

// Manually activate order (for invoice payments)
router.post('/orders/:reference/activate', adminAuth, async (req, res, next) => {
  try {
    const order = await Order.updatePaymentStatus(req.params.reference, 'paid');

    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    // Notify Aiden
    const { notifyAiden } = require('../services/notifications');
    await notifyAiden('payment_received', order);

    res.json({
      success: true,
      order: {
        reference: order.order_reference,
        status: order.order_status,
        payment_status: order.payment_status
      }
    });
  } catch (err) {
    next(err);
  }
});

// Update order status
router.post('/orders/:reference/status', adminAuth, async (req, res, next) => {
  try {
    const { status } = req.body;
    const validStatuses = ['received', 'processing', 'completed', 'cancelled'];

    if (!validStatuses.includes(status)) {
      return res.status(400).json({ error: 'Invalid status' });
    }

    const order = await Order.updateOrderStatus(req.params.reference, status);

    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    res.json({
      success: true,
      order: {
        reference: order.order_reference,
        status: order.order_status
      }
    });
  } catch (err) {
    next(err);
  }
});

module.exports = router;