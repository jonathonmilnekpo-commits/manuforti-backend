# Manu Forti Website — HTML Structure Overview

## File Structure

| File | Lines | Purpose |
|------|-------|---------|
| `index.html` | 539 | Main landing page |
| `order.html` | 1,032 | Order form with payment selection |
| `payment.html` | 258 | Stripe payment page |
| `order-success.html` | 210 | Order confirmation |
| `ant-design-version.html` | 250 | Alternative Ant Design version |
| `deployment-options-table.html` | 153 | Deployment comparison |

**Total:** 2,442 lines of HTML/CSS/JS

---

## index.html — Main Landing Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manu Forti Intelligence — AI-Powered Supplier Intelligence</title>
    <style>
        /* CSS Variables */
        :root {
            --navy: #002147;
            --cobalt: #2B6CB0;
            --white: #FFFFFF;
            --gray: #718096;
            --light-gray: #F7FAFC;
            --green: #48BB78;
        }
        
        /* Full inline CSS (~400 lines) */
        /* Includes: header, hero, features, pricing, how-it-works, contact, footer */
    </style>
</head>
<body>
    <!-- HEADER -->
    <header>
        <nav class="container">
            <div class="logo">Manu Forti <span>Intelligence</span></div>
            <ul class="nav-links">
                <li><a href="#features">Features</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#how-it-works">How It Works</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- HERO SECTION -->
    <section class="hero">
        <div class="container">
            <h1>Take a grip of procurement with Manu Forti</h1>
            <p>AI-powered supplier intelligence combining cutting-edge analysis with 80+ years of procurement expertise. Professional evaluation reports delivered in 6-24 hours.</p>
            <a href="order.html" class="cta-button">Order Report Now</a>
        </div>
    </section>

    <!-- FEATURES SECTION (6 cards) -->
    <section class="features" id="features">
        <div class="container">
            <h2>Why Manu Forti?</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <h3>🎯 AI-Powered Analysis</h3>
                    <p>Advanced AI models analyze financial health, operational capability, geopolitical risk, and ESG factors.</p>
                </div>
                <!-- 5 more feature cards... -->
            </div>
        </div>
    </section>

    <!-- PRICING SECTION (3 tiers) -->
    <section class="pricing" id="pricing">
        <div class="container">
            <h2>Simple, Transparent Pricing</h2>
            <p class="pricing-subtitle">No subscriptions. No hidden fees. Pay per report. USD pricing.</p>
            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>Standard Report</h3>
                    <div class="price">$249<span>/report</span></div>
                    <ul>
                        <li>9-slide professional report</li>
                        <li>Financial health analysis</li>
                        <li>Operational capability assessment</li>
                        <li>Risk rating & recommendation</li>
                        <li>24-hour delivery</li>
                    </ul>
                    <a href="order.html?tier=standard" class="cta-button">Get Started</a>
                </div>
                <!-- Premium and Enterprise cards... -->
            </div>
        </div>
    </section>

    <!-- HOW IT WORKS (4 steps) -->
    <section class="how-it-works" id="how-it-works">
        <div class="container">
            <h2>How It Works</h2>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Submit Request</h3>
                    <p>Tell us which supplier you need evaluated.</p>
                </div>
                <!-- Steps 2-4... -->
            </div>
        </div>
    </section>

    <!-- CONTACT SECTION -->
    <section class="contact" id="contact">
        <div class="container">
            <h2>Ready to evaluate your suppliers?</h2>
            <p>Request a demo or submit your first supplier evaluation.</p>
            <form class="contact-form" action="mailto:Jonathon.Milne137@gmail.com" method="post" enctype="text/plain">
                <!-- Form fields... -->
                <button type="submit" class="submit-button">Request a Demo</button>
            </form>
        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <p>&copy; 2026 Manu Forti Intelligence. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

---

## order.html — Order Form Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Similar CSS variables + order-specific styles -->
</head>
<body>
    <header><!-- Same navigation --></header>
    
    <main>
        <!-- Progress Steps -->
        <div class="progress-steps">
            <div class="step-indicator active">
                <div class="step-number">1</div>
                <span>Details</span>
            </div>
            <div class="step-indicator">
                <div class="step-number">2</div>
                <span>Payment</span>
            </div>
            <div class="step-indicator">
                <div class="step-number">3</div>
                <span>Confirmation</span>
            </div>
        </div>

        <form id="orderForm" class="form-card">
            <!-- TIER SELECTION -->
            <div class="form-section">
                <h3 class="section-title">📋 Select Your Analysis Tier</h3>
                <div class="tier-options">
                    <div class="tier-option" data-tier="standard" data-price="249">
                        <h4>Standard</h4>
                        <div class="tier-price">$249</div>
                        <p>24-hour delivery</p>
                    </div>
                    <div class="tier-option featured" data-tier="premium" data-price="349">
                        <h4>Premium ⭐</h4>
                        <div class="tier-price">$349</div>
                        <p>12-hour delivery</p>
                    </div>
                    <div class="tier-option" data-tier="enterprise" data-price="499">
                        <h4>Enterprise</h4>
                        <div class="tier-price">$499</div>
                        <p>6-hour delivery</p>
                    </div>
                </div>
            </div>

            <!-- CUSTOMER INFORMATION -->
            <div class="form-section">
                <h3 class="section-title">👤 Your Information</h3>
                <div class="form-row">
                    <div class="form-group">
                        <label>Full Name <span class="required">*</span></label>
                        <input type="text" name="fullName" required>
                    </div>
                    <div class="form-group">
                        <label>Email <span class="required">*</span></label>
                        <input type="email" name="email" required>
                    </div>
                </div>
                <!-- Phone, Job Title... -->
            </div>

            <!-- COMPANY INFORMATION -->
            <div class="form-section">
                <h3 class="section-title">🏢 Company Information</h3>
                <!-- Company name, industry dropdown, country dropdown, VAT, website -->
            </div>

            <!-- SUPPLIER REPORT REQUESTED -->
            <div class="form-section">
                <h3 class="section-title">🔍 Supplier Report Requested</h3>
                <!-- Supplier name, website, country, analysis context textarea -->
            </div>

            <!-- SUPPORTING DOCUMENTS -->
            <div class="form-section">
                <h3 class="section-title">📎 Supporting Documents (Optional)</h3>
                <div class="file-upload">
                    <input type="file" id="documents" name="documents" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.png,.jpg,.jpeg">
                    <span class="file-upload-text">Click to upload files</span>
                </div>
            </div>

            <!-- PAYMENT METHOD -->
            <div class="form-section">
                <h3 class="section-title">💳 Payment Method</h3>
                <div class="payment-options">
                    <div class="payment-option" data-payment="vipps">
                        <span class="payment-radio"></span>
                        <div class="payment-info">
                            <h4>Vipps</h4>
                            <p>Norwegian mobile payment</p>
                        </div>
                    </div>
                    <div class="payment-option" data-payment="stripe">
                        <span class="payment-radio"></span>
                        <div class="payment-info">
                            <h4>Card</h4>
                            <p>Credit or debit card via Stripe</p>
                        </div>
                    </div>
                    <div class="payment-option selected" data-payment="invoice">
                        <span class="payment-radio"></span>
                        <div class="payment-info">
                            <h4>Invoice</h4>
                            <p>14-day payment terms</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ORDER SUMMARY -->
            <div class="order-summary" id="orderSummary">
                <h4>Order Summary</h4>
                <div class="summary-row"><span>Tier:</span><span id="summaryTier">-</span></div>
                <div class="summary-row"><span>Delivery:</span><span id="summarySLA">-</span></div>
                <div class="summary-row"><span>Payment:</span><span id="summaryPayment">-</span></div>
                <div class="summary-row"><span>Total:</span><span id="summaryTotal">$0</span></div>
                <div class="feedback-note">
                    <strong>Quality Assurance:</strong> If the report quality is insufficient, Jonathon will provide feedback for revision at no additional cost.
                </div>
            </div>

            <!-- SUBMIT -->
            <div class="submit-section">
                <button type="submit" class="submit-btn">Complete Order</button>
                <p class="terms-text">By submitting, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>.</p>
            </div>
        </form>
    </main>

    <footer><!-- Same footer --></footer>

    <script>
        // JavaScript for form handling, tier selection, payment selection, file upload
        // ~200 lines of vanilla JS
    </script>
</body>
</html>
```

---

## Key Design Elements

### Color Palette
- **Primary Navy:** `#002147` (headers, buttons)
- **Cobalt Blue:** `#2B6CB0` (accents, links)
- **White:** `#FFFFFF` (backgrounds)
- **Gray:** `#718096` (text, borders)
- **Light Gray:** `#F7FAFC` (section backgrounds)
- **Green:** `#48BB78` (success, checkmarks)

### Typography
- **Font Family:** System font stack (Apple, Segoe, Roboto, Helvetica)
- **Hero H1:** 3.5rem (56px)
- **Section H2:** 2.5rem (40px)
- **Body:** 1rem (16px)

### Layout
- **Container:** max-width 1200px, centered
- **Grid:** CSS Grid and Flexbox
- **Responsive:** Mobile-first with breakpoints at 768px

---

## Full Files Location

All HTML files are in:
```
/Users/jonathonmilne/.openclaw/workspace/manuforti-website/
```

To view full source code:
```bash
cat /Users/jonathonmilne/.openclaw/workspace/manuforti-website/index.html
cat /Users/jonathonmilne/.openclaw/workspace/manuforti-website/order.html
```

Or open in Google Drive where they're shared with you.
