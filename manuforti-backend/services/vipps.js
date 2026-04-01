const axios = require('axios');
const logger = require('../utils/logger');

class VippsService {
  constructor() {
    this.baseURL = process.env.VIPPS_BASE_URL || 'https://apitest.vipps.no';
    this.clientId = process.env.VIPPS_CLIENT_ID;
    this.clientSecret = process.env.VIPPS_CLIENT_SECRET;
    this.subscriptionKey = process.env.VIPPS_SUBSCRIPTION_KEY;
    this.merchantSerial = process.env.VIPPS_MERCHANT_SERIAL_NUMBER;
    this.accessToken = null;
    this.tokenExpiry = null;
  }

  async getAccessToken() {
    // Check if token is still valid (with 5 min buffer)
    if (this.accessToken && this.tokenExpiry && Date.now() < this.tokenExpiry - 300000) {
      return this.accessToken;
    }

    try {
      const response = await axios.post(
        `${this.baseURL}/accesstoken/get`,
        {},
        {
          headers: {
            'client_id': this.clientId,
            'client_secret': this.clientSecret,
            'Ocp-Apim-Subscription-Key': this.subscriptionKey
          }
        }
      );

      this.accessToken = response.data.access_token;
      this.tokenExpiry = Date.now() + (response.data.expires_in * 1000);

      return this.accessToken;
    } catch (err) {
      logger.error('Vipps token error:', err.response?.data || err.message);
      throw new Error('Failed to get Vipps access token');
    }
  }

  async createPayment({ orderReference, amount, phoneNumber, description }) {
    const token = await this.getAccessToken();

    const paymentBody = {
      merchantInfo: {
        merchantSerialNumber: this.merchantSerial,
        callbackPrefix: `${process.env.FRONTEND_URL}/api/webhooks/vipps`,
        returnUrl: `${process.env.FRONTEND_URL}/order-success?ref=${orderReference}`,
        paymentDescription: description
      },
      customerInfo: {
        mobileNumber: phoneNumber?.replace(/\D/g, '') // Remove non-digits
      },
      transaction: {
        orderId: orderReference,
        amount: {
          currency: 'NOK',
          value: amount * 100 // Convert to øre
        },
        transactionText: description
      }
    };

    try {
      const response = await axios.post(
        `${this.baseURL}/epayment/v1/payments`,
        paymentBody,
        {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Ocp-Apim-Subscription-Key': this.subscriptionKey,
            'Idempotency-Key': orderReference,
            'Content-Type': 'application/json'
          }
        }
      );

      return {
        reference: response.data.reference,
        redirectUrl: response.data.redirectUrl
      };
    } catch (err) {
      logger.error('Vipps payment creation error:', err.response?.data || err.message);
      throw new Error('Failed to create Vipps payment');
    }
  }

  async getPaymentStatus(reference) {
    const token = await this.getAccessToken();

    try {
      const response = await axios.get(
        `${this.baseURL}/epayment/v1/payments/${reference}`,
        {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Ocp-Apim-Subscription-Key': this.subscriptionKey
          }
        }
      );

      return response.data;
    } catch (err) {
      logger.error('Vipps status check error:', err.response?.data || err.message);
      throw new Error('Failed to get Vipps payment status');
    }
  }
}

module.exports = new VippsService();