const sgMail = require('@sendgrid/mail');
const logger = require('../utils/logger');

sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const FROM_EMAIL = process.env.EMAIL_FROM || 'orders@manuforti.com';
const FROM_NAME = process.env.EMAIL_FROM_NAME || 'Manu Forti Intelligence';

class EmailService {
  async sendConfirmationEmail(order) {
    const msg = {
      to: order.customer_email,
      from: { email: FROM_EMAIL, name: FROM_NAME },
      subject: `Order Confirmation — ${order.order_reference}`,
      html: this.getConfirmationTemplate(order),
      text: this.getConfirmationText(order)
    };

    try {
      await sgMail.send(msg);
      logger.info(`Confirmation email sent to ${order.customer_email}`);
    } catch (err) {
      logger.error('SendGrid error:', err);
      throw err;
    }
  }

  async sendInvoiceEmail(order) {
    const msg = {
      to: order.customer_email,
      from: { email: FROM_EMAIL, name: FROM_NAME },
      subject: `Invoice — ${order.order_reference}`,
      html: this.getInvoiceTemplate(order),
      text: this.getInvoiceText(order)
    };

    try {
      await sgMail.send(msg);
      logger.info(`Invoice email sent to ${order.customer_email}`);
    } catch (err) {
      logger.error('SendGrid error:', err);
      throw err;
    }
  }

  async sendJonathonNotification(order) {
    const jonathonEmail = process.env.JONATHON_EMAIL || 'Jonathon.Milne137@gmail.com';
    
    const msg = {
      to: jonathonEmail,
      from: { email: FROM_EMAIL, name: FROM_NAME },
      subject: `🛎️ NEW ORDER — ${order.order_reference} — ${order.product_type || 'Report'}`,
      html: this.getJonathonTemplate(order),
      text: this.getJonathonText(order)
    };

    try {
      await sgMail.send(msg);
      logger.info(`Notification email sent to Jonathon: ${jonathonEmail}`);
    } catch (err) {
      logger.error('SendGrid error (Jonathon notification):', err);
      throw err;
    }
  }

  async sendReportDeliveryEmail(order, downloadUrl) {
    const msg = {
      to: order.customer_email,
      from: { email: FROM_EMAIL, name: FROM_NAME },
      subject: `Your Report is Ready — ${order.supplier_name}`,
      html: this.getDeliveryTemplate(order, downloadUrl),
      text: this.getDeliveryText(order, downloadUrl)
    };

    try {
      await sgMail.send(msg);
      logger.info(`Delivery email sent to ${order.customer_email}`);
    } catch (err) {
      logger.error('SendGrid error:', err);
      throw err;
    }
  }

  getConfirmationTemplate(order) {
    return `
      <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
        <div style="text-align: center; margin-bottom: 30px;">
          <h1 style="color: #002147; margin: 0;">Manu Forti Intelligence</h1>
          <p style="color: #718096; margin-top: 10px;">Take a grip of procurement</p>
        </div>
        
        <div style="background: #F7FAFC; border-radius: 8px; padding: 30px; margin-bottom: 30px;">
          <h2 style="color: #002147; margin-top: 0;">Order Confirmation</h2>
          <p style="font-size: 18px; color: #2B6CB0; font-weight: 600;">${order.order_reference}</p>
          
          <table style="width: 100%; margin-top: 20px;">
            <tr>
              <td style="padding: 10px 0; color: #718096;">Tier:</td>
              <td style="padding: 10px 0; text-align: right; font-weight: 600;">${order.tier}</td>
            </tr>
            <tr>
              <td style="padding: 10px 0; color: #718096;">Supplier:</td>
              <td style="padding: 10px 0; text-align: right; font-weight: 600;">${order.supplier_name}</td>
            </tr>
            <tr>
              <td style="padding: 10px 0; color: #718096;">Price:</td>
              <td style="padding: 10px 0; text-align: right; font-weight: 600;">$${order.price}</td>
            </tr>
            <tr>
              <td style="padding: 10px 0; color: #718096;">Delivery:</td>
              <td style="padding: 10px 0; text-align: right; font-weight: 600;">${order.sla_hours} hours</td>
            </tr>
          </table>
        </div>
        
        <p style="color: #4A5568; line-height: 1.6;">
          Thank you for your order. We'll begin the analysis as soon as payment is confirmed.
          You'll receive another email when your report is ready for download.
        </p>
        
        <p style="color: #718096; font-size: 14px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #E2E8F0;">
          Questions? Reply to this email or contact us at support@manuforti.com
        </p>
      </div>
    `;
  }

  getConfirmationText(order) {
    return `
Manu Forti Intelligence — Order Confirmation

Order Reference: ${order.order_reference}
Tier: ${order.tier}
Supplier: ${order.supplier_name}
Price: $${order.price}
Delivery: ${order.sla_hours} hours

Thank you for your order. We'll begin the analysis as soon as payment is confirmed.
You'll receive another email when your report is ready for download.

Questions? Contact support@manuforti.com
    `.trim();
  }

  getInvoiceTemplate(order) {
    return `
      <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
        <h1 style="color: #002147;">Invoice Request Received</h1>
        <p>We'll send your invoice within 24 hours.</p>
        <p><strong>Order:</strong> ${order.order_reference}</p>
        <p><strong>Amount:</strong> $${order.price}</p>
        <p><strong>Terms:</strong> 14 days</p>
      </div>
    `;
  }

  getInvoiceText(order) {
    return `Invoice Request Received\n\nOrder: ${order.order_reference}\nAmount: $${order.price}\nTerms: 14 days`;
  }

  getDeliveryTemplate(order, downloadUrl) {
    return `
      <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
        <h1 style="color: #002147;">Your Report is Ready</h1>
        <p>Your ${order.tier} analysis of ${order.supplier_name} is now available.</p>
        <a href="${downloadUrl}" style="display: inline-block; background: #002147; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 20px 0;">Download Report</a>
      </div>
    `;
  }

  getDeliveryText(order, downloadUrl) {
    return `Your Report is Ready\n\nDownload: ${downloadUrl}`;
  }

  getJonathonTemplate(order) {
    const isCategoryStrategy = order.product_type === 'category_strategy';
    const isMonitoring = order.product_type === 'monitoring';
    
    return `
      <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
        <div style="background: #002147; color: white; padding: 20px; border-radius: 8px 8px 0 0;">
          <h1 style="margin: 0; font-size: 24px;">🛎️ New Order Received</h1>
          <p style="margin: 5px 0 0 0; opacity: 0.8;">${order.order_reference}</p>
        </div>
        
        <div style="background: #F7FAFC; padding: 30px; border-radius: 0 0 8px 8px;">
          <h2 style="color: #002147; margin-top: 0;">${isCategoryStrategy ? 'Category Strategy' : isMonitoring ? 'Media Monitoring' : 'Supplier Report'}</h2>
          
          <table style="width: 100%; margin: 20px 0;">
            <tr>
              <td style="padding: 8px 0; color: #718096; width: 40%;">Customer:</td>
              <td style="padding: 8px 0; font-weight: 600;">${order.customer_name}</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #718096;">Email:</td>
              <td style="padding: 8px 0;">${order.customer_email}</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #718096;">Company:</td>
              <td style="padding: 8px 0; font-weight: 600;">${order.company_name}</td>
            </tr>
            ${isCategoryStrategy ? `
            <tr>
              <td style="padding: 8px 0; color: #718096;">Category:</td>
              <td style="padding: 8px 0;">${order.category_name || 'N/A'}</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #718096;">Annual Spend:</td>
              <td style="padding: 8px 0;">${order.annual_spend || 'N/A'} ${order.spend_currency || ''}</td>
            </tr>
            ` : isMonitoring ? `
            <tr>
              <td style="padding: 8px 0; color: #718096;">Plan:</td>
              <td style="padding: 8px 0;">${order.monitoring_plan || 'N/A'}</td>
            </tr>
            ` : `
            <tr>
              <td style="padding: 8px 0; color: #718096;">Supplier:</td>
              <td style="padding: 8px 0; font-weight: 600;">${order.supplier_name}</td>
            </tr>
            `}
            <tr>
              <td style="padding: 8px 0; color: #718096;">Amount:</td>
              <td style="padding: 8px 0; font-weight: 600; color: #2B6CB0;">€${order.price}</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #718096;">Ordered:</td>
              <td style="padding: 8px 0;">${new Date(order.created_at).toLocaleString('en-GB')}</td>
            </tr>
          </table>
          
          <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid #E2E8F0;">
            <p style="color: #718096; font-size: 14px;">
              <strong>Next Steps:</strong> Send invoice within 24h. Aiden has been notified and will initiate fulfillment workflow.
            </p>
          </div>
        </div>
      </div>
    `;
  }

  getJonathonText(order) {
    return `
🛎️ NEW ORDER — ${order.order_reference}

Product: ${order.product_type || 'Report'}
Customer: ${order.customer_name} (${order.customer_email})
Company: ${order.company_name}
Amount: €${order.price}

${order.supplier_name ? `Supplier: ${order.supplier_name}` : ''}
${order.category_name ? `Category: ${order.category_name}` : ''}

Ordered: ${new Date(order.created_at).toLocaleString('en-GB')}

Next Steps: Send invoice within 24h. Aiden notified.
    `.trim();
  }
}

module.exports = new EmailService();