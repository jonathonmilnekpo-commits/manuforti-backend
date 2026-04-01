const { query } = require('../models/db');

async function initDatabase() {
  console.log('Initializing database...');

  // Create orders table
  await query(`
    CREATE TABLE IF NOT EXISTS orders (
      id SERIAL PRIMARY KEY,
      order_reference VARCHAR(20) UNIQUE NOT NULL,
      
      -- Tier & Pricing
      tier VARCHAR(20) NOT NULL CHECK (tier IN ('Standard', 'Premium', 'Enterprise')),
      price INTEGER NOT NULL,
      final_price INTEGER NOT NULL,
      discount_code VARCHAR(50),
      discount_amount INTEGER DEFAULT 0,
      payment_method VARCHAR(20) NOT NULL CHECK (payment_method IN ('Vipps', 'Stripe', 'Invoice')),
      payment_status VARCHAR(20) DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'invoice_pending', 'failed', 'refunded')),
      payment_id VARCHAR(255),
      
      -- Customer
      customer_name VARCHAR(255) NOT NULL,
      customer_email VARCHAR(255) NOT NULL,
      customer_phone VARCHAR(50),
      customer_title VARCHAR(100),
      
      -- Company
      company_name VARCHAR(255) NOT NULL,
      industry VARCHAR(100),
      country VARCHAR(2),
      company_number VARCHAR(50),
      company_website VARCHAR(255),
      
      -- Supplier
      supplier_name VARCHAR(255) NOT NULL,
      supplier_website VARCHAR(255),
      supplier_country VARCHAR(2),
      analysis_context TEXT,
      
      -- Status & SLA
      order_status VARCHAR(20) DEFAULT 'received' CHECK (order_status IN ('received', 'processing', 'completed', 'cancelled')),
      sla_hours INTEGER NOT NULL,
      sla_deadline TIMESTAMP NOT NULL,
      
      -- Timestamps
      created_at TIMESTAMP DEFAULT NOW(),
      paid_at TIMESTAMP,
      delivered_at TIMESTAMP
    )
  `);

  // Create indexes
  await query('CREATE INDEX IF NOT EXISTS idx_orders_reference ON orders(order_reference)');
  await query('CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(order_status)');
  await query('CREATE INDEX IF NOT EXISTS idx_orders_payment ON orders(payment_status)');
  await query('CREATE INDEX IF NOT EXISTS idx_orders_created ON orders(created_at)');

  // Create file uploads table
  await query(`
    CREATE TABLE IF NOT EXISTS order_files (
      id SERIAL PRIMARY KEY,
      order_reference VARCHAR(20) REFERENCES orders(order_reference),
      filename VARCHAR(255) NOT NULL,
      original_name VARCHAR(255) NOT NULL,
      mime_type VARCHAR(100),
      size_bytes INTEGER,
      s3_key VARCHAR(500),
      uploaded_at TIMESTAMP DEFAULT NOW()
    )
  `);

  console.log('Database initialized successfully');
  process.exit(0);
}

initDatabase().catch(err => {
  console.error('Database initialization failed:', err);
  process.exit(1);
});