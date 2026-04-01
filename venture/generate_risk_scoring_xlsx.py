#!/usr/bin/env python3
"""
Product 1 Risk Scoring System - Excel Generator
Creates a comprehensive .xlsx workbook with:
- Risk Criteria (weighted scoring framework)
- Scoring Worksheet (interactive calculator)
- Example Calculation (Nel ASA sample)
- Risk Matrix (visual reference)
"""

import xlsxwriter
import os

# Output path
output_path = "/Users/jonathonmilne/.openclaw/workspace/venture/Product1_Risk_Scoring_System.xlsx"

# Create workbook
workbook = xlsxwriter.Workbook(output_path)

# Define formats
header_format = workbook.add_format({
    'bold': True,
    'bg_color': '#002147',  # Navy
    'font_color': 'white',
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})

category_format = workbook.add_format({
    'bold': True,
    'bg_color': '#2B6CB0',  # Steel Blue
    'font_color': 'white',
    'border': 1,
    'align': 'left',
    'valign': 'vcenter'
})

subheader_format = workbook.add_format({
    'bold': True,
    'bg_color': '#EBF4FF',  # Light blue
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})

cell_format = workbook.add_format({
    'border': 1,
    'align': 'left',
    'valign': 'top',
    'text_wrap': True
})

center_format = workbook.add_format({
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})

number_format = workbook.add_format({
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'num_format': '0.0'
})

percent_format = workbook.add_format({
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'num_format': '0%'
})

# RAG formats
low_format = workbook.add_format({
    'bg_color': '#48BB78',  # Green
    'font_color': 'white',
    'bold': True,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})

medium_format = workbook.add_format({
    'bg_color': '#ED8936',  # Amber
    'font_color': 'white',
    'bold': True,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})

high_format = workbook.add_format({
    'bg_color': '#E53E3E',  # Red
    'font_color': 'white',
    'bold': True,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})

formula_format = workbook.add_format({
    'bg_color': '#FFF5F5',  # Light red background for formula cells
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'num_format': '0.0'
})

title_format = workbook.add_format({
    'bold': True,
    'font_size': 16,
    'font_color': '#002147',
    'align': 'left',
    'valign': 'vcenter'
})

subtitle_format = workbook.add_format({
    'italic': True,
    'font_size': 10,
    'font_color': '#718096',
    'align': 'left',
    'valign': 'vcenter'
})

# ============================================================================
# SHEET 1: Risk Criteria Reference
# ============================================================================
ws1 = workbook.add_worksheet('Risk Criteria')
ws1.set_tab_color('#002147')

# Title
ws1.merge_range('A1:H1', 'Product 1 - Risk Scoring Criteria', title_format)
ws1.merge_range('A2:H2', 'Manu Forti Intelligence | Supplier Risk Assessment Framework', subtitle_format)
ws1.write('A3', '')

# Headers
headers = ['Risk Category', 'Risk Factor', 'Weight', 'Low (0-33)', 'Medium (34-66)', 'High (67-100)', 'Data Sources', 'Notes']
for col, header in enumerate(headers):
    ws1.write(3, col, header, header_format)

# Risk data
risk_data = [
    # Financial
    ('FINANCIAL', 'Revenue Trend', '10%', 
     'Revenue growing >10% CAGR', 'Revenue flat or volatile ±10%', 'Revenue declining >10% CAGR',
     'Annual reports; Bloomberg', '3-year trend'),
    ('FINANCIAL', 'EBITDA Margin', '10%',
     '>15% margin stable', '5-15% margin or declining', '<5% or negative margin',
     'Annual reports; Capital IQ', 'Operating profitability'),
    ('FINANCIAL', 'Leverage (Debt/EBITDA)', '10%',
     '<2.0x with stable cash flow', '2.0-4.0x or covenant pressure', '>4.0x or restructuring risk',
     'Credit reports; Annual reports', 'Debt sustainability'),
    
    # Operational
    ('OPERATIONAL', 'Manufacturing Capacity', '8%',
     'Capacity >120% of demand; diversified', 'Capacity 100-120%; some constraints', 'Capacity <100%; single point of failure',
     'Company reports; Site visits', 'Utilization vs demand'),
    ('OPERATIONAL', 'Customer Concentration', '8%',
     'No customer >20% revenue', 'One customer 20-40% revenue', 'One customer >40% revenue',
     'Annual reports; Contracts', 'Revenue stability risk'),
    ('OPERATIONAL', 'Certifications & Track Record', '9%',
     'ISO certified; >10 years track record', 'Some certifications; 5-10 years history', 'Certification gaps; <5 years or poor record',
     'ISO registry; Industry databases', 'Quality assurance'),
    
    # Geopolitical
    ('GEOPOLITICAL', 'Country Risk Rating', '10%',
     'OECD member; stable democracy', 'Emerging market; moderate risk', 'High risk; sanctions; conflict zone',
     'OECD; World Bank; OFAC', 'Political stability'),
    ('GEOPOLITICAL', 'Sanctions Exposure', '8%',
     'No sanctions; clean screening', 'Minor sanctions (non-blocking)', 'Primary sanctions; SDN list match',
     'OFAC; EU; UN sanctions lists', 'Compliance risk'),
    ('GEOPOLITICAL', 'Currency & Regulatory', '7%',
     'Stable currency; favorable regulations', 'Moderate FX risk; evolving regulations', 'Volatile currency; restrictive regulations',
     'IMF; Central bank; Local counsel', 'Financial predictability'),
    
    # ESG
    ('ESG', 'Environmental Record', '7%',
     'No violations; strong sustainability', 'Minor violations; improvement plans', 'Major violations; legal action; poor ratings',
     'EcoVadis; EPA; Media screening', 'Environmental compliance'),
    ('ESG', 'Social & Labor', '7%',
     'Clean record; strong labor practices', 'Minor labor issues; ongoing disputes', 'Major labor disputes; human rights concerns',
     'Media; Labor unions; NGO reports', 'Social license'),
    ('ESG', 'Governance & Ethics', '6%',
     'Transparent ownership; strong governance', 'Governance gaps; minor controversies', 'Poor governance; corruption issues; sanctions',
     'Beneficial ownership registries; FCPA', 'Corporate integrity'),
]

# Write risk data
row = 4
for category, factor, weight, low, med, high, sources, notes in risk_data:
    ws1.write(row, 0, category, category_format)
    ws1.write(row, 1, factor, cell_format)
    ws1.write(row, 2, weight, center_format)
    ws1.write(row, 3, low, cell_format)
    ws1.write(row, 4, med, cell_format)
    ws1.write(row, 5, high, cell_format)
    ws1.write(row, 6, sources, cell_format)
    ws1.write(row, 7, notes, cell_format)
    row += 1

# Set column widths
ws1.set_column('A:A', 15)
ws1.set_column('B:B', 25)
ws1.set_column('C:C', 8)
ws1.set_column('D:F', 35)
ws1.set_column('G:G', 30)
ws1.set_column('H:H', 25)

# Set row heights for wrapped text
for r in range(4, row):
    ws1.set_row(r, 45)

# ============================================================================
# SHEET 2: Scoring Worksheet (Interactive Calculator)
# ============================================================================
ws2 = workbook.add_worksheet('Scoring Calculator')
ws2.set_tab_color('#2B6CB0')

# Title
ws2.merge_range('A1:F1', 'Risk Scoring Calculator', title_format)
ws2.merge_range('A2:F2', 'Enter raw scores (0-100) for each risk factor to calculate overall risk rating', subtitle_format)
ws2.write('A3', '')

# Headers
ws2.write('A4', 'Risk Factor', header_format)
ws2.write('B4', 'Weight', header_format)
ws2.write('C4', 'Raw Score\n(0-100)', header_format)
ws2.write('D4', 'Weighted\nScore', header_format)
ws2.write('E4', 'Rating', header_format)
ws2.write('F4', 'Notes', header_format)

# Risk factors for calculator
calc_factors = [
    ('Revenue Trend', 0.10),
    ('EBITDA Margin', 0.10),
    ('Leverage (Debt/EBITDA)', 0.10),
    ('Manufacturing Capacity', 0.08),
    ('Customer Concentration', 0.08),
    ('Certifications & Track Record', 0.09),
    ('Country Risk Rating', 0.10),
    ('Sanctions Exposure', 0.08),
    ('Currency & Regulatory', 0.07),
    ('Environmental Record', 0.07),
    ('Social & Labor', 0.07),
    ('Governance & Ethics', 0.06),
]

row = 4
for factor, weight in calc_factors:
    ws2.write(row, 0, factor, cell_format)
    ws2.write(row, 1, weight, percent_format)
    ws2.write(row, 2, 0, formula_format)  # User enters raw score here
    ws2.write_formula(row, 3, f'=C{row+1}*B{row+1}', formula_format)
    
    # Rating formula based on score
    rating_formula = f'=IF(C{row+1}<=33,"LOW",IF(C{row+1}<=66,"MEDIUM","HIGH"))'
    ws2.write_formula(row, 4, rating_formula, center_format)
    ws2.write(row, 5, '', cell_format)
    row += 1

# Category subtotals
row += 1
ws2.write(row, 0, 'CATEGORY SUBTOTALS', header_format)
ws2.merge_range(f'B{row+1}:F{row+1}', '', header_format)

row += 1
ws2.write(row, 0, 'Financial Subtotal', subheader_format)
ws2.write_formula(row, 1, '=SUM(B5:B7)', percent_format)
ws2.write(row, 2, '', center_format)
ws2.write_formula(row, 3, '=SUM(D5:D7)', number_format)
ws2.write(row, 4, '', center_format)
ws2.write(row, 5, '30% weight', cell_format)

row += 1
ws2.write(row, 0, 'Operational Subtotal', subheader_format)
ws2.write_formula(row, 1, '=SUM(B8:B10)', percent_format)
ws2.write(row, 2, '', center_format)
ws2.write_formula(row, 3, '=SUM(D8:D10)', number_format)
ws2.write(row, 4, '', center_format)
ws2.write(row, 5, '25% weight', cell_format)

row += 1
ws2.write(row, 0, 'Geopolitical Subtotal', subheader_format)
ws2.write_formula(row, 1, '=SUM(B11:B13)', percent_format)
ws2.write(row, 2, '', center_format)
ws2.write_formula(row, 3, '=SUM(D11:D13)', number_format)
ws2.write(row, 4, '', center_format)
ws2.write(row, 5, '25% weight', cell_format)

row += 1
ws2.write(row, 0, 'ESG Subtotal', subheader_format)
ws2.write_formula(row, 1, '=SUM(B14:B16)', percent_format)
ws2.write(row, 2, '', center_format)
ws2.write_formula(row, 3, '=SUM(D14:D16)', number_format)
ws2.write(row, 4, '', center_format)
ws2.write(row, 5, '20% weight', cell_format)

# Final calculation
row += 2
ws2.write(row, 0, 'RAW TOTAL', header_format)
ws2.write_formula(row, 1, '=SUM(B5:B16)', percent_format)
ws2.write(row, 2, '', center_format)
ws2.write_formula(row, 3, '=SUM(D5:D16)', number_format)
ws2.merge_range(f'E{row+1}:F{row+1}', '', header_format)

row += 1
ws2.write(row, 0, 'ESG Override Check', cell_format)
ws2.merge_range(f'B{row+1}:D{row+1}', 'If ESG=MEDIUM and others avg=LOW → Overall=MEDIUM', cell_format)
ws2.merge_range(f'E{row+1}:F{row+1}', '', cell_format)

row += 1
ws2.write(row, 0, 'FINAL SCORE', header_format)
ws2.merge_range(f'B{row+1}:C{row+1}', '', header_format)
ws2.write_formula(row, 3, '=D22', number_format)
ws2.write_formula(row, 4, '=IF(D23<=33,"LOW",IF(D23<=66,"MEDIUM","HIGH"))', center_format)
ws2.write(row, 5, '', cell_format)

row += 1
ws2.write(row, 0, 'RECOMMENDATION', header_format)
ws2.merge_range(f'B{row+1}:F{row+1}', 
    '=IF(D23<=33,"✅ APPROVE",IF(D23<=50,"✅ APPROVE with minor conditions",IF(D23<=66,"⚠️ CONDITIONAL",IF(D23<=80,"⚠️ CONDITIONAL with safeguards","❌ REJECT"))))',
    center_format)

# Set column widths
ws2.set_column('A:A', 28)
ws2.set_column('B:B', 10)
ws2.set_column('C:C', 12)
ws2.set_column('D:D', 12)
ws2.set_column('E:E', 12)
ws2.set_column('F:F', 35)

# ============================================================================
# SHEET 3: Example Calculation (Nel ASA)
# ============================================================================
ws3 = workbook.add_worksheet('Example - Nel ASA')
ws3.set_tab_color('#48BB78')

# Title
ws3.merge_range('A1:F1', 'Example Calculation: Nel ASA (Hydrogen/Electrolyser)', title_format)
ws3.merge_range('A2:F2', 'Sample risk assessment for demonstration purposes', subtitle_format)
ws3.write('A3', '')

# Headers
ws3.write('A4', 'Risk Factor', header_format)
ws3.write('B4', 'Weight', header_format)
ws3.write('C4', 'Raw Score', header_format)
ws3.write('D4', 'Weighted Score', header_format)
ws3.write('E4', 'Rating', header_format)
ws3.write('F4', 'Justification', header_format)

# Nel ASA example data
nel_data = [
    ('Revenue Trend', 0.10, 45, 'Growth slowing but still positive'),
    ('EBITDA Margin', 0.10, 55, 'Negative EBITDA in recent quarters'),
    ('Leverage (Debt/EBITDA)', 0.10, 40, 'Moderate debt levels'),
    ('Manufacturing Capacity', 0.08, 35, 'Capacity expansion ongoing'),
    ('Customer Concentration', 0.08, 30, 'Diversified customer base'),
    ('Certifications & Track Record', 0.09, 25, 'Strong track record in hydrogen'),
    ('Country Risk Rating', 0.10, 15, 'Norway - very low risk'),
    ('Sanctions Exposure', 0.08, 5, 'No sanctions exposure'),
    ('Currency & Regulatory', 0.07, 20, 'Stable NOK, favorable regulations'),
    ('Environmental Record', 0.07, 50, 'Some project concerns raised'),
    ('Social & Labor', 0.07, 40, 'Generally positive record'),
    ('Governance & Ethics', 0.06, 30, 'Standard governance practices'),
]

row = 4
for factor, weight, score, justification in nel_data:
    ws3.write(row, 0, factor, cell_format)
    ws3.write(row, 1, weight, percent_format)
    ws3.write(row, 2, score, number_format)
    ws3.write_formula(row, 3, f'=C{row+1}*B{row+1}', number_format)
    
    # Rating based on score
    if score <= 33:
        rating_format = low_format
        rating_text = 'LOW'
    elif score <= 66:
        rating_format = medium_format
        rating_text = 'MEDIUM'
    else:
        rating_format = high_format
        rating_text = 'HIGH'
    
    ws3.write(row, 4, rating_text, rating_format)
    ws3.write(row, 5, justification, cell_format)
    row += 1

# Category subtotals
row += 1
ws3.write(row, 0, 'CATEGORY SUBTOTALS', header_format)
ws3.merge_range(f'B{row+1}:F{row+1}', '', header_format)

row += 1
ws3.write(row, 0, 'Financial Subtotal', subheader_format)
ws3.write(row, 1, 0.30, percent_format)
ws3.write(row, 2, '', center_format)
ws3.write_formula(row, 3, '=SUM(D5:D7)', number_format)
ws3.write(row, 4, 'MEDIUM', medium_format)
ws3.write(row, 5, 'Mixed financial signals', cell_format)

row += 1
ws3.write(row, 0, 'Operational Subtotal', subheader_format)
ws3.write(row, 1, 0.25, percent_format)
ws3.write(row, 2, '', center_format)
ws3.write_formula(row, 3, '=SUM(D8:D10)', number_format)
ws3.write(row, 4, 'LOW', low_format)
ws3.write(row, 5, 'Strong operational profile', cell_format)

row += 1
ws3.write(row, 0, 'Geopolitical Subtotal', subheader_format)
ws3.write(row, 1, 0.25, percent_format)
ws3.write(row, 2, '', center_format)
ws3.write_formula(row, 3, '=SUM(D11:D13)', number_format)
ws3.write(row, 4, 'LOW', low_format)
ws3.write(row, 5, 'Excellent geopolitical position', cell_format)

row += 1
ws3.write(row, 0, 'ESG Subtotal', subheader_format)
ws3.write(row, 1, 0.20, percent_format)
ws3.write(row, 2, '', center_format)
ws3.write_formula(row, 3, '=SUM(D14:D16)', number_format)
ws3.write(row, 4, 'MEDIUM', medium_format)
ws3.write(row, 5, 'Some environmental concerns', cell_format)

# Final calculation
row += 2
ws3.write(row, 0, 'RAW TOTAL', header_format)
ws3.write(row, 1, 1.00, percent_format)
ws3.write(row, 2, '', center_format)
ws3.write_formula(row, 3, '=SUM(D5:D16)', number_format)
ws3.merge_range(f'E{row+1}:F{row+1}', '', header_format)

row += 1
ws3.write(row, 0, 'ESG Override Check', cell_format)
ws3.merge_range(f'B{row+1}:F{row+1}', 'ESG=MEDIUM (40 avg), Others avg=28 → Apply elevator rule', cell_format)

row += 1
ws3.write(row, 0, 'FINAL SCORE', header_format)
ws3.merge_range(f'B{row+1}:C{row+1}', '', header_format)
ws3.write(row, 3, 48, number_format)
ws3.write(row, 4, 'MEDIUM', medium_format)
ws3.write(row, 5, 'After ESG override applied', cell_format)

row += 1
ws3.write(row, 0, 'RECOMMENDATION', header_format)
ws3.merge_range(f'B{row+1}:F{row+1}', '⚠️ CONDITIONAL APPROVAL', center_format)

row += 2
ws3.write(row, 0, 'RECOMMENDED CONDITIONS:', header_format)
ws3.merge_range(f'B{row+1}:F{row+1}', '', header_format)

conditions = [
    '1. Milestone-based payments tied to delivery',
    '2. Monitor Q4 results for EBITDA improvement',
    '3. Reassess in 6 months',
    '4. Require parent guarantee for large contracts',
]

row += 1
for condition in conditions:
    ws3.merge_range(f'A{row+1}:F{row+1}', condition, cell_format)
    row += 1

# Set column widths
ws3.set_column('A:A', 28)
ws3.set_column('B:B', 10)
ws3.set_column('C:C', 12)
ws3.set_column('D:D', 15)
ws3.set_column('E:E', 12)
ws3.set_column('F:F', 40)

# ============================================================================
# SHEET 4: Risk Rating Reference
# ============================================================================
ws4 = workbook.add_worksheet('Rating Reference')
ws4.set_tab_color('#ED8936')

# Title
ws4.merge_range('A1:E1', 'Risk Rating Reference Guide', title_format)
ws4.write('A2', '')

# Score ranges
ws4.write('A4', 'Score Range', header_format)
ws4.write('B4', 'Risk Level', header_format)
ws4.write('C4', 'Color Code', header_format)
ws4.write('D4', 'Recommendation', header_format)
ws4.write('E4', 'Approval Authority', header_format)

rating_data = [
    ('0-33', 'LOW', '#48BB78', '✅ APPROVE', 'Aiden'),
    ('34-50', 'MEDIUM-LOW', '#ECC94B', '✅ APPROVE with minor conditions', 'Aiden'),
    ('51-66', 'MEDIUM', '#ED8936', '⚠️ CONDITIONAL', 'Aiden'),
    ('67-80', 'MEDIUM-HIGH', '#FC8181', '⚠️ CONDITIONAL with significant safeguards', 'Jonathon'),
    ('81-100', 'HIGH', '#E53E3E', '❌ REJECT / EXTREME CAUTION', 'CEO approval only'),
]

row = 4
for score_range, level, color, recommendation, authority in rating_data:
    ws4.write(row, 0, score_range, center_format)
    ws4.write(row, 1, level, center_format)
    ws4.write(row, 2, color, center_format)
    ws4.write(row, 3, recommendation, cell_format)
    ws4.write(row, 4, authority, cell_format)
    row += 1

# ESG Override Rules
row += 2
ws4.merge_range(f'A{row+1}:E{row+1}', 'ESG Override Rules', header_format)

row += 1
ws4.write(row, 0, 'Rule', subheader_format)
ws4.write(row, 1, 'Condition', subheader_format)
ws4.merge_range(f'C{row+1}:E{row+1}', 'Result', subheader_format)

row += 1
ws4.write(row, 0, 'ESG Elevator', cell_format)
ws4.write(row, 1, 'ESG=MEDIUM + All Others=LOW', cell_format)
ws4.merge_range(f'C{row+1}:E{row+1}', 'Overall rating elevated to MEDIUM (not LOW)', cell_format)

row += 1
ws4.write(row, 0, 'ESG Cap', cell_format)
ws4.write(row, 1, 'ESG=HIGH', cell_format)
ws4.merge_range(f'C{row+1}:E{row+1}', 'Overall rating elevated by one tier minimum', cell_format)

# Tier-specific thresholds
row += 2
ws4.merge_range(f'A{row+1}:E{row+1}', 'Tier-Specific Risk Thresholds', header_format)

row += 1
ws4.write(row, 0, 'Tier', subheader_format)
ws4.write(row, 1, 'Max Acceptable Risk', subheader_format)
ws4.write(row, 2, 'Approval Authority', subheader_format)
ws4.merge_range(f'D{row+1}:E{row+1}', 'Notes', subheader_format)

row += 1
ws4.write(row, 0, 'Standard ($249)', cell_format)
ws4.write(row, 1, '66 (MEDIUM)', center_format)
ws4.write(row, 2, 'Aiden', center_format)
ws4.merge_range(f'D{row+1}:E{row+1}', 'Conditional approval acceptable', cell_format)

row += 1
ws4.write(row, 0, 'Premium ($349)', cell_format)
ws4.write(row, 1, '66 (MEDIUM)', center_format)
ws4.write(row, 2, 'Aiden', center_format)
ws4.merge_range(f'D{row+1}:E{row+1}', 'Enhanced due diligence for 51-66 range', cell_format)

row += 1
ws4.write(row, 0, 'Enterprise ($499)', cell_format)
ws4.write(row, 1, '80 (MEDIUM-HIGH)', center_format)
ws4.write(row, 2, 'Jonathon', center_format)
ws4.merge_range(f'D{row+1}:E{row+1}', 'All HIGH risk require Jonathon sign-off', cell_format)

# Set column widths
ws4.set_column('A:A', 20)
ws4.set_column('B:B', 20)
ws4.set_column('C:C', 20)
ws4.set_column('D:D', 35)
ws4.set_column('E:E', 20)

# ============================================================================
# SHEET 5: Risk Mitigation Conditions
# ============================================================================
ws5 = workbook.add_worksheet('Mitigation Conditions')
ws5.set_tab_color('#718096')

# Title
ws5.merge_range('A1:C1', 'Risk Mitigation Conditions', title_format)
ws5.write('A2', '')

# Headers
ws5.write('A4', 'Risk Level', header_format)
ws5.write('B4', 'Sample Conditions', header_format)
ws5.write('C4', 'Implementation', header_format)

mitigation_data = [
    ('MEDIUM\n(34-66)', 
     '• Milestone-based payments\n• Parent guarantee\n• Performance bond\n• Quarterly business reviews',
     'Standard contract clauses'),
    ('MEDIUM-HIGH\n(67-80)',
     '• Letter of credit\n• Escrow arrangement\n• Reduced contract value\n• Monthly monitoring\n• Board approval required',
     'Enhanced contract terms'),
    ('HIGH\n(81-100)',
     '• Do not proceed\n• Alternative supplier required\n• Exceptional circumstances only\n• CEO approval required',
     'Exception process only'),
]

row = 4
for level, conditions, implementation in mitigation_data:
    ws5.write(row, 0, level, cell_format)
    ws5.write(row, 1, conditions, cell_format)
    ws5.write(row, 2, implementation, cell_format)
    ws5.set_row(row, 80)
    row += 1

# Set column widths
ws5.set_column('A:A', 15)
ws5.set_column('B:B', 40)
ws5.set_column('C:C', 25)

# Close workbook
workbook.close()

print(f"✅ Risk Scoring System created: {output_path}")
print(f"   Sheets: Risk Criteria, Scoring Calculator, Example (Nel ASA), Rating Reference, Mitigation Conditions")
