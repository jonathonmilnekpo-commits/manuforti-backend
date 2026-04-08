const express = require('express');
const { body, validationResult } = require('express-validator');
const router = express.Router();

const Order = require('../models/order');
const { notifyAiden } = require('../services/notifications');
const emailService = require('../services/email');
const logger = require('../utils/logger');

// Validation rules for new multi-product form
const orderValidation = [
  body('product_type').isIn(['report', 'monitoring', 'category_strategy']).withMessage('Invalid product type'),
  body('customer_name').trim().notEmpty().withMessage('Customer name is required'),
  body('customer_email').isEmail().normalizeEmail().withMessage('Valid email is required'),
  body('company_name').trim().notEmpty().withMessage('Company name is required'),
  body('industry').trim().notEmpty().withMessage('Industry is required'),
  body('country').trim().notEmpty().withMessage('Country is required'),
  body('company_number').trim().notEmpty().withMessage('Company/VAT number is required'),
  body('billing_address').trim().notEmpty().withMessage('Billing address is required')
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
      product_type: order.product_type,
      tier: order.tier,
      customer: order.customer_email
    });

    // 1. Send confirmation email to buyer
    try {
      await emailService.sendConfirmationEmail(order);
      logger.info(`Confirmation email sent to ${order.customer_email}`);
    } catch (emailErr) {
      logger.error('Failed to send confirmation email:', emailErr);
      // Don't fail the request if email fails
    }

    // 2. Send notification to Jonathon
    try {
      await emailService.sendJonathonNotification(order);
    } catch (emailErr) {
      logger.error('Failed to send Jonathon notification:', emailErr);
      // Don't fail the request if notification fails
    }

    // 3. Notify Aiden for fulfillment initiation
    try {
      await notifyAiden('order_received', order);
    } catch (notifyErr) {
      logger.error('Failed to notify Aiden:', notifyErr);
      // Don't fail the request if notification fails
    }

    res.status(201).json({
      success: true,
      message: 'Order received successfully',
      order: {
        reference: order.order_reference,
        product_type: order.product_type,
        status: order.order_status,
        customer_email: order.customer_email
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
        product_type: order.product_type,
        tier: order.tier,
        price: order.price,
        status: order.order_status,
        created_at: order.created_at,
        customer: {
          name: order.customer_name,
          email: order.customer_email,
          company: order.company_name
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
      product_type: order.product_type
    });
  } catch (err) {
    next(err);
  }
});

module.exports = router;
