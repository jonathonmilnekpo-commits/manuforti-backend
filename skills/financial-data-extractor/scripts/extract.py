#!/usr/bin/env python3
"""
Financial Data Extractor
Extracts standardized metrics from supplier financial documents.
"""

import re
import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

# Regex patterns for financial extraction
PATTERNS = {
    "revenue": [
        r'(?:revenue|turnover|sales)\s*(?:of|:)?\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
        r'(?:total|gross)\s+revenue\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
    ],
    "ebitda": [
        r'(?:ebitda|operating\s+profit)\s*(?:of|:)?\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
        r'ebitda\s+margin\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
    ],
    "net_profit": [
        r'(?:net\s+profit|net\s+income|bottom\s+line)\s*(?:of|:)?\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
    ],
    "gross_debt": [
        r'(?:gross\s+debt|total\s+debt|borrowings)\s*(?:of|:)?\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
    ],
    "net_cash": [
        r'(?:net\s+cash|net\s+debt)\s*(?:of|:|position)?\s*[:\$€£+-]?\s*([\d.,]+\s*[BMK]?)',
        r'cash\s+(?:and\s+)?equivalents\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
    ],
    "debt_ebitda": [
        r'(?:debt/ebitda|leverage|ratio)\s*(?:of|:)?\s*([\d.,]+\s*[xX]?)',
        r'(?:debt\s+to\s+ebitda|leverage\s+ratio)\s*[:\s]+([\d.,]+)',
    ],
    "order_book": [
        r'(?:order\s+book|backlog|contract\s+backlog)\s*(?:of|:)?\s*[:\$€£]?\s*([\d.,]+\s*[BMK]?)',
    ],
    "cagr": [
        r'(?:cagr|compound\s+annual\s+growth)\s*(?:of|:)?\s*([\d.,]+\s*%?)',
        r'(?:annual\s+growth|growth\s+rate)\s*[:\s]+([\d.,]+\s*%)',
    ],
    "ebitda_margin": [
        r'ebitda\s+margin\s*[:\s]+([\d.,]+\s*%)',
        r'margin\s*[:\s]+([\d.,]+\s*%)',
    ],
    "yoy_change": [
        r'(?:change|growth|increase)\s*(?:of|by)?\s*[:\s]+([+-]?[\d.,]+\s*%)',
        r'(?:yoy|year[-\s]on[-\s]year)\s*[:\s]+([+-]?[\d.,]+\s*%)',
    ]
}

def extract_metric(text: str, metric: str) -> Optional[str]:
    """Extract a single metric from text using patterns."""
    patterns = PATTERNS.get(metric, [])
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Return the first match, cleaned
            value = matches[0].strip()
            return value
    
    return None

def calculate_confidence(extracted: Dict) -> float:
    """Calculate confidence score based on extracted fields."""
    required = ["revenue", "ebitda", "gross_debt", "net_cash", "debt_ebitda"]
    found = sum(1 for k in required if extracted.get(k))
    return found / len(required)

def extract_from_text(text: str, supplier_name: str = "") -> Dict:
    """Extract all financial metrics from text."""
    
    text_lower = text.lower()
    
    # Detect currency
    currency = "USD"
    if "eur" in text_lower or "€" in text:
        currency = "EUR"
    elif "gbp" in text_lower or "£" in text:
        currency = "GBP"
    elif "nok" in text_lower:
        currency = "NOK"
    
    # Detect fiscal year
    fy_match = re.search(r'20\d{2}', text)
    fiscal_year = fy_match.group(0) if fy_match else str(datetime.now().year)
    
    # Extract all metrics
    extracted = {
        "supplier": supplier_name,
        "fiscal_year": fiscal_year,
        "currency": currency,
        "revenue": extract_metric(text, "revenue"),
        "revenue_yoy": extract_metric(text, "yoy_change"),
        "ebitda": extract_metric(text, "ebitda"),
        "ebitda_margin": extract_metric(text, "ebitda_margin"),
        "net_profit": extract_metric(text, "net_profit"),
        "cagr_3yr": extract_metric(text, "cagr"),
        "order_book": extract_metric(text, "order_book"),
        "gross_debt": extract_metric(text, "gross_debt"),
        "net_cash": extract_metric(text, "net_cash"),
        "debt_ebitda": extract_metric(text, "debt_ebitda"),
        "extraction_date": datetime.now().isoformat(),
    }
    
    # Add confidence score
    extracted["extraction_confidence"] = round(calculate_confidence(extracted), 2)
    
    return extracted

def extract_from_pdf(pdf_path: str) -> Dict:
    """Extract from PDF file."""
    try:
        # Try to use PyPDF2 or pdfplumber
        import PyPDF2
        
        text = ""
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        
        supplier = Path(pdf_path).stem.replace('_', ' ').title()
        return extract_from_text(text, supplier)
        
    except ImportError:
        return {"error": "PyPDF2 not installed. Run: python3 -m pip install PyPDF2"}
    except Exception as e:
        return {"error": f"PDF extraction failed: {e}"}

def extract_from_html(url: str) -> Dict:
    """Extract from HTML URL."""
    try:
        import requests
        from bs4 import BeautifulSoup
        
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from tables and main content
        text = soup.get_text()
        
        # Try to get supplier name from title
        supplier = ""
        title = soup.find('title')
        if title:
            supplier = title.text.split('|')[0].strip()
        
        result = extract_from_text(text, supplier)
        result["source_url"] = url
        return result
        
    except ImportError:
        return {"error": "requests/BeautifulSoup not installed"}
    except Exception as e:
        return {"error": f"HTML extraction failed: {e}"}

def main():
    parser = argparse.ArgumentParser(description="Extract financial metrics")
    parser.add_argument("--source", "-s", required=True, help="Path or URL to document")
    parser.add_argument("--format", "-f", choices=["pdf", "html", "text"], default="pdf")
    parser.add_argument("--output", "-o", help="Output JSON file")
    parser.add_argument("--supplier", "-n", help="Supplier name override")
    
    args = parser.parse_args()
    
    # Extract based on format
    if args.format == "pdf":
        result = extract_from_pdf(args.source)
    elif args.format == "html":
        result = extract_from_html(args.source)
    else:
        with open(args.source) as f:
            result = extract_from_text(f.read(), args.supplier or "")
    
    # Override supplier name if provided
    if args.supplier and "error" not in result:
        result["supplier"] = args.supplier
    
    # Output
    output = json.dumps(result, indent=2)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Extracted to: {args.output}")
    else:
        print(output)
    
    # Return exit code based on confidence
    if result.get("extraction_confidence", 0) < 0.5:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
