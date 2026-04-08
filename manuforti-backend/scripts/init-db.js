const { query } = require('../models/db');

async function initDatabase() {
  console.log('Initializing database...');

  // Create orders table with new schema
  await query(`
    CREATE TABLE IF NOT EXISTS orders (
      id SERIAL PRIMARY KEY,
      order_reference VARCHAR(20) UNIQUE NOT NULL,
      
      -- Product Type
      product_type VARCHAR(30) DEFAULT 'report' CHECK (product_type IN ('report', 'monitoring', 'category_strategy')),
      
      -- Tier & Pricing
      tier VARCHAR(30) NOT NULL,
      price INTEGER NOT NULL,
      monitoring_plan VARCHAR(20),
      
      -- Payment (simplified - invoice by default)
      payment_status VARCHAR(20) DEFAULT 'invoice_pending' CHECK (payment_status IN ('pending', 'paid', 'invoice_pending', 'failed', 'refunded')),
      
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
      billing_address TEXT,
      
      -- Supplier (for reports)
      supplier_name VARCHAR(255),
      supplier_website VARCHAR(255),
      analysis_context TEXT,
      
      -- Category Strategy fields
      category_name VARCHAR(255),
      annual_spend VARCHAR(50),
      spend_currency VARCHAR(10),
      timeline_constraint VARCHAR(255),
      incumbent_suppliers TEXT,
      key_pain_points TEXT,
      strategic_priorities TEXT,
      
      -- Status
      order_status VARCHAR(20) DEFAULT 'received' CHECK (order_status IN ('received', 'processing', 'completed', 'cancelled')),
      
      -- Timestamps
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW(),
      paid_at TIMESTAMP,
      delivered_at TIMESTAMP
    )
  `);

  // Create indexes
  await query('CREATE INDEX IF NOT EXISTS idx_orders_reference ON orders(order_reference)');
  await query('CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(order_status)');
  await query('CREATE INDEX IF NOT EXISTS idx_orders_created ON orders(created_at)');
  await query('CREATE INDEX IF NOT EXISTS idx_orders_product_type ON orders(product_type)');

  console.log('Database initialized successfully');
  process.exit(0);
}

initDatabase().catch(err => {
  console.error('Database initialization failed:', err);
  process.exit(1);
});
