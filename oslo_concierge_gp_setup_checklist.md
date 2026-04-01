# Fully Private Practice Setup Guide
## Oslo Concierge GP — Step-by-Step Implementation

**For:** Parallel private practice alongside fastlege role  
**Model:** Helfrivat (100% private, no trygderefusjon)  
**Timeline:** 60-90 days to first paying member  

---

## Pre-Launch Checklist

### Phase 1: Legal Foundation (Week 1)

| Step | Action | Details | Cost | Status |
|------|--------|---------|------|--------|
| 1.1 | **Review fastlegeavtale** | Check for clauses restricting competing commercial activity | Free | ☐ |
| 1.2 | **Register business entity** | ENK (simplest) or AS via Altinn | NOK 5,570 (AS) | ☐ |
| 1.3 | **Open business bank account** | DNB, Nordea, or Sparebank 1 | Free | ☐ |
| 1.4 | **Notify municipality** | Send practice details: name, address, size, financing model | Free | ☐ |
| 1.5 | **Notify employer** | Inform municipality of secondary activity per contract | Free | ☐ |
| 1.6 | **Engage lawyer** | Draft membership agreement, privacy notice, consent forms | NOK 15,000-25,000 | ☐ |
| 1.7 | **Apply for ansvarsforsikring** | Professional liability insurance | NOK 20,000-40,000/year | ☐ |

**Critical Decision:** Review fastlegeavtale BEFORE proceeding — this is your primary regulatory risk.

---

### Phase 2: Clinical Infrastructure (Weeks 2-4)

| Step | Action | Details | Cost | Status |
|------|--------|---------|------|--------|
| 2.1 | **Secure consultation space** | Shared privatklinikk or lease | NOK 10,000-20,000/mo | ☐ |
| 2.2 | **Select EPJ system** | EG Pasientsky recommended | NOK 6,700-9,000/year | ☐ |
| 2.3 | **Register with NPE** | Notify within 1 week of first patient | NOK 1,000-2,500/year | ☐ |
| 2.5 | **Set up OpenClaw** | Mac Mini M4, member dossier structure | Existing hardware | ☐ |
| 2.6 | **Configure agents** | Nightly monitor, pre-consult briefer, lab processor | Free | ☐ |
| 2.7 | **Establish lab partnerships** | Unilabs and/or Fürst accounts | Variable | ☐ |
| 2.8 | **Procure equipment** | ECG, BP monitor, body composition scale | NOK 15,000-30,000 | ☐ |

**EPJ Recommendation:** EG Pasientsky is the leading Norwegian EPJ with native AI features for documentation.

---

### Phase 3: Systems & Operations (Weeks 3-6)

| Step | Action | Details | Cost | Status |
|------|--------|---------|------|--------|
| 3.1 | **Payment infrastructure** | Stripe or Vipps recurring billing | Transaction fees | ☐ |
| 3.2 | **Secure communication** | Signal or WhatsApp Business | Free | ☐ |
| 3.3 | **Cloudflare Tunnel** | Encrypted remote access | NOK 500-1,000/year | ☐ |
| 3.4 | **Build intake questionnaire** | Typeform or equivalent (GDPR-compliant) | NOK 0-3,000/year | ☐ |
| 3.5 | **Scheduling tool** | Calendly linked to your calendar | NOK 0-1,200/year | ☐ |
| 3.6 | **Create member handbook** | What to expect, how to contact, what's included | Your time | ☐ |
| 3.7 | **Design supplement protocols** | Evidence-based templates | Your time | ☐ |
| 3.8 | **Build consultation templates** | SOAP format, structured notes | Your time | ☐ |

---

### Phase 4: Marketing & Launch (Weeks 6-10)

| Step | Action | Details | Cost | Status |
|------|--------|---------|------|--------|
| 4.1 | **Create simple website** | One-pager with tier comparison | NOK 0-10,000 | ☐ |
| 4.2 | **Design referral programme** | One free month per successful referral | Cost of month | ☐ |
| 4.3 | **Prepare outreach message** | Personal message for 30-50 network contacts | Your time | ☐ |
| 4.4 | **Create Executive Health Audit** | NOK 15,000 entry offer | Your time | ☐ |
| 4.5 | **Secure 2-year exclusivity** | Clinic and gym partnership agreements | Negotiated | ☐ |
| 4.6 | **Draft thought leadership** | Finansavisen/DN op-ed | Your time | ☐ |

---

### Phase 5: Founder Launch (Weeks 10-14)

| Step | Action | Target | Status |
|------|--------|--------|--------|
| 5.1 | **Send personal outreach** | 30-50 people in professional network | ☐ |
| 5.2 | **Host informal conversations** | 2-3 lunches/coffees explaining concept | ☐ |
| 5.3 | **Offer founding member pricing** | NOK 1,500-2,500/month (discounted) | ☐ |
| 5.4 | **Onboard first members** | Intake, foundation consultation, baseline labs | ☐ |
| 5.5 | **Build first dossiers** | Run first agent briefing cycle | ☐ |

**Target:** 10-15 founding members at discounted rate

---

### Phase 6: Iterate & Validate (Weeks 14-20)

| Step | Action | Target | Status |
|------|--------|--------|--------|
| 6.1 | **Gather feedback** | From founding members on experience | ☐ |
| 6.2 | **Refine systems** | Consultation structure, agent outputs, health briefs | ☐ |
| 6.3 | **Begin corporate outreach** | 3-5 target companies | ☐ |
| 6.4 | **Submit first article** | Finansavisen/DN op-ed | ☐ |
| 6.5 | **Review pricing** | Are members happy to pay full rate? | ☐ |

**Target:** 15+ members and NOK 75,000+/month by Day 90

---

## Key Regulatory Points

### What You DON'T Need
- ❌ Helfo registration (no trygderefusjon)
- ❌ Driftstilskudd agreement
- ❌ Normaltariff compliance (you set prices)

### What You DO Need
- ✅ Business entity (ENK or AS)
- ✅ Municipality notification
- ✅ Employer notification (per contract)
- ✅ NPE registration (within 1 week)
- ✅ Compliant EPJ system
- ✅ Professional liability insurance

### Critical Compliance Rule
**Data Sovereignty:** When using cloud LLMs (Claude, etc.), never include patient names, IDs, or identifying information. Use anonymised descriptions: *"A 52-year-old male with elevated ApoB..."*

**Your local OpenClaw stack (Qwen 35B) can process identifiable data. Cloud APIs cannot.**

---

## Cost Summary

### Setup Costs (One-Time)
| Item | Cost |
|------|------|
| AS registration | NOK 5,570 |
| Lawyer (membership agreement, privacy docs) | NOK 15,000-25,000 |
| Accountant setup | NOK 10,000-15,000 |
| Clinical equipment | NOK 15,000-30,000 |
| Clinic room deposit | NOK 30,000-60,000 |
| Working capital buffer | NOK 50,000-100,000 |
| **Total Setup** | **NOK 125,000-235,000** |

### Annual Operating Costs
| Item | Cost |
|------|------|
| Professional liability insurance | NOK 20,000-40,000 |
| EPJ system (EG Pasientsky) | NOK 6,700-9,000 |
| NPE tilskudd | NOK 1,000-2,500 |
| Clinic room rental | NOK 120,000-240,000 |
| Cloudflare + domain | NOK 500-1,000 |
| **Total Annual** | **NOK 152,000-317,500** |

### Monthly Break-Even
- **15-18 members** at average NOK 5,000/month = NOK 75,000-90,000/month revenue
- Costs at this level: ~NOK 40,000-60,000/month
- **Break-even achieved:** Month 2-3 with focused execution

---

## Timeline at a Glance

| Phase | Weeks | Key Deliverable |
|-------|-------|-----------------|
| Legal Foundation | 1 | Business registered, contracts drafted |
| Clinical Infrastructure | 2-4 | EPJ live, NPE registered, space secured |
| Systems & Operations | 3-6 | Payment flow, intake forms, protocols ready |
| Marketing & Launch | 6-10 | Website live, outreach materials ready |
| Founder Launch | 10-14 | First 10-15 members onboarded |
| Iterate & Validate | 14-20 | 15+ members, NOK 75K+/month revenue |

**First paying member:** Week 8-10  
**Break-even:** Week 10-14  
**Full validation:** Day 90

---

*Din Personlige Helsesjef  |  Oslo Concierge GP  |  Fully Private Practice Setup  |  Version 1.0*
