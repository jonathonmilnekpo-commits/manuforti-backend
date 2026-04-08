const { query } = require('./db');
const { v4: uuidv4 } = require('uuid');

class Order {
  static generateReference() {
    const date = new Date();
    const year = date.getFullYear();
    const random = Math.floor(10000 + Math.random() * 90000);
    return `MF-${year}-${random}`;
  }

  static async create(orderData) {
    const {
      product_type = 'report',  // report, monitoring, category_strategy
      tier,
      price,
      monitoring_plan,
      customer_name,
      customer_email,
      customer_phone,
      customer_title,
      company_name,
      industry,
      country,
      company_number,
      billing_address,
      supplier_name,
      supplier_website,
      analysis_context,
      // Category strategy fields
      category_name,
      annual_spend,
      spend_currency,
      timeline_constraint,
      incumbent_suppliers,
      key_pain_points,
      strategic_priorities
    } = orderData;

    const orderReference = this.generateReference();
    
    // Determine price based on product type
    let finalPrice = price;
    let finalTier = tier;
    
    if (product_type === 'category_strategy') {
      finalPrice = 3999;
      finalTier = 'Category Strategy';
    } else if (product_type === 'monitoring') {
      finalPrice = monitoring_plan === 'alert' ? 105 : 35;
      finalTier = monitoring_plan === 'alert' ? 'Alert' : 'Monitor';
    } else {
      // report
      finalPrice = tier === 'premium' || tier === 'express' ? 349 : 249;
      finalTier = tier === 'premium' || tier === 'express' ? 'Express' : 'Standard';
    }

    const sql = `
      INSERT INTO orders (
        order_reference, 
        product_type,
        tier, 
        price,
        monitoring_plan,
        customer_name, 
        customer_email, 
        customer_phone, 
        customer_title,
        company_name, 
        industry, 
        country, 
        company_number,
        billing_address,
        supplier_name, 
        supplier_website,
        analysis_context,
        category_name,
        annual_spend,
        spend_currency,
        timeline_constraint,
        incumbent_suppliers,
        key_pain_points,
        strategic_priorities,
        order_status
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, 'received')
      RETURNING *
    `;

    const values = [
      orderReference,
      product_type,
      finalTier,
      finalPrice,
      monitoring_plan || null,
      customer_name,
      customer_email,
      customer_phone || null,
      customer_title || null,
      company_name,
      industry,
      country,
      company_number,
      billing_address,
      supplier_name || null,
      supplier_website || null,
      analysis_context || null,
      category_name || null,
      annual_spend || null,
      spend_currency || null,
      timeline_constraint || null,
      incumbent_suppliers || null,
      key_pain_points || null,
      strategic_priorities || null
    ];

    const result = await query(sql, values);
    return result.rows[0];
  }

  static async findByReference(reference) {
    const result = await query(
      'SELECT * FROM orders WHERE order_reference = $1',
      [reference]
    );
    return result.rows[0];
  }

  static async updateOrderStatus(reference, status) {
    const sql = `
      UPDATE orders 
      SET order_status = $1,
          updated_at = NOW()
      WHERE order_reference = $2
      RETURNING *
    `;
    const result = await query(sql, [status, reference]);
    return result.rows[0];
  }

  static async listAll(limit = 50, offset = 0) {
    const result = await query(
      'SELECT * FROM orders ORDER BY created_at DESC LIMIT $1 OFFSET $2',
      [limit, offset]
    );
    return result.rows;
  }

  static async getPendingOrders() {
    const result = await query(
      "SELECT * FROM orders WHERE order_status = 'processing' ORDER BY created_at ASC"
    );
    return result.rows;
  }
}

module.exports = Order;
