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
      tier,
      price,
      final_price,
      discount_code,
      discount_amount,
      payment_method,
      customer_name,
      customer_email,
      customer_phone,
      customer_title,
      company_name,
      industry,
      country,
      company_number,
      company_website,
      supplier_name,
      supplier_website,
      supplier_country,
      analysis_context,
      sla_hours
    } = orderData;

    const orderReference = this.generateReference();
    const slaDeadline = new Date();
    slaDeadline.setHours(slaDeadline.getHours() + sla_hours);

    // If 100% discount, auto-mark as paid
    const initialPaymentStatus = (discount_amount >= price) ? 'paid' : 'pending';
    const initialOrderStatus = (discount_amount >= price) ? 'processing' : 'received';

    const sql = `
      INSERT INTO orders (
        order_reference, tier, price, final_price, discount_code, discount_amount, payment_method,
        customer_name, customer_email, customer_phone, customer_title,
        company_name, industry, country, company_number, company_website,
        supplier_name, supplier_website, supplier_country, analysis_context,
        sla_hours, sla_deadline, order_status, payment_status, paid_at
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, CASE WHEN $23 = 'paid' THEN NOW() ELSE NULL END)
      RETURNING *
    `;

    const values = [
      orderReference, tier, price, final_price || price, discount_code || null, discount_amount || 0, payment_method,
      customer_name, customer_email, customer_phone, customer_title,
      company_name, industry, country, company_number, company_website,
      supplier_name, supplier_website, supplier_country, analysis_context,
      sla_hours, slaDeadline, initialOrderStatus, initialPaymentStatus
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

  static async updatePaymentStatus(reference, status, paymentId = null) {
    const sql = `
      UPDATE orders 
      SET payment_status = $1, 
          payment_id = $2,
          paid_at = CASE WHEN $1 = 'paid' THEN NOW() ELSE paid_at END,
          order_status = CASE WHEN $1 = 'paid' THEN 'processing' ELSE order_status END
      WHERE order_reference = $3
      RETURNING *
    `;
    const result = await query(sql, [status, paymentId, reference]);
    return result.rows[0];
  }

  static async updateOrderStatus(reference, status) {
    const sql = `
      UPDATE orders 
      SET order_status = $1,
          delivered_at = CASE WHEN $1 = 'completed' THEN NOW() ELSE delivered_at END
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
      "SELECT * FROM orders WHERE order_status = 'processing' AND payment_status = 'paid' ORDER BY sla_deadline ASC"
    );
    return result.rows;
  }

  static async getOverdueOrders() {
    const result = await query(
      "SELECT * FROM orders WHERE order_status != 'completed' AND sla_deadline < NOW()"
    );
    return result.rows;
  }
}

module.exports = Order;