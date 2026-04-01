const express = require('express');
const { body, validationResult } = require('express-validator');
const router = express.Router();

const Order = require('../models/order');
const { notifyAiden } = require('../services/notifications');
const { sendConfirmationEmail } = require('../services/email');
const logger = require('../utils/logger');

// Validation rules
const orderValidation = [
  body('tier').isIn(['Standard', 'Premium', 'Enterprise']).withMessage('Invalid tier'),
  body('price').isInt({ min: 1 }).withMessage('Invalid price'),
  body('payment_method').isIn(['Vipps', 'Stripe', 'Invoice']).withMessage('Invalid payment method'),
  body('customer_name').trim().notEmpty().withMessage('Customer name is required'),
  body('customer_email').isEmail().normalizeEmail().withMessage('Valid email is required'),
  body('company_name').trim().notEmpty().withMessage('Company name is required'),
  body('supplier_name').trim().notEmpty().withMessage('Supplier name is required'),
  body('sla_hours').isInt({ min: 1 }).withMessage('Invalid SLA hours')
];

// Create new order
router.post('/', orderValidation, async (req, res, next) => {
  try {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({
        error: 'Validation failed',
        details: errors.array()
      });
    }

    const order = await Order.create(req.body);
    
    logger.info(`Order created: ${order.order_reference}`, {
      tier: order.tier,
      payment_method: order.payment_method,
      supplier: order.supplier_name
    });

    // Send confirmation email
    try {
      await sendConfirmationEmail(order);
    } catch (emailErr) {
      logger.error('Failed to send confirmation email:', emailErr);
      // Don't fail the request if email fails
    }

    // Notify Aiden
    try {
      await notifyAiden('order_received', order);
    } catch (notifyErr) {
      logger.error('Failed to notify Aiden:', notifyErr);
      // Don't fail the request if notification fails
    }

    res.status(201).json({
      success: true,
      order: {
        reference: order.order_reference,
        status: order.order_status,
        payment_status: order.payment_status,
        sla_deadline: order.sla_deadline
      }
    });
  } catch (err) {
    next(err);
  }
});

// Get order by reference
router.get('/:reference', async (req, res, next) => {
  try {
    const order = await Order.findByReference(req.params.reference);
    
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    res.json({
      order: {
        reference: order.order_reference,
        tier: order.tier,
        price: order.price,
        status: order.order_status,
        payment_status: order.payment_status,
        created_at: order.created_at,
        sla_deadline: order.sla_deadline,
        supplier: {
          name: order.supplier_name,
          country: order.supplier_country
        }
      }
    });
  } catch (err) {
    next(err);
  }
});

// Public status check (minimal info)
router.get('/:reference/status', async (req, res, next) => {
  try {
    const order = await Order.findByReference(req.params.reference);
    
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    res.json({
      reference: order.order_reference,
      status: order.order_status,
      payment_status: order.payment_status,
      sla_deadline: order.sla_deadline,
      delivered_at: order.delivered_at
    });
  } catch (err) {
    next(err);
  }
});

module.exports = router;