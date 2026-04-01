#!/usr/bin/env python3
"""
Daily Memory Logger
Called by Aiden to log conversations to memory/YYYY-MM-DD.md
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Configuration
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"

def get_today_file():
    """Get today's memory file path"""
    today = datetime.now().strftime("%Y-%m-%d")
    return MEMORY_DIR / f"{today}.md"

def create_daily_template(filepath):
    """Create new daily memory file with template"""
    today = datetime.now()
    day_name = today.strftime("%A")
    date_str = today.strftime("%Y-%m-%d")
    
    template = f"""# Daily Memory - {date_str} ({day_name})

## Summary

## Career (Statkraft)
- 

## Venture (Manu Forti)
- 

## Family
- 

## Key Decisions
- 

## Learnings
- 

## Links & References
- 

---
*Logged by Aiden*
"""
    
    filepath.write_text(template, encoding='utf-8')
    print(f"Created: {filepath}")

def append_to_section(filepath, section, content):
    """Append content to a specific section"""
    if not filepath.exists():
        create_daily_template(filepath)
    
    text = filepath.read_text(encoding='utf-8')
    
    # Find the section
    section_header = f"## {section}"
    if section_header not in text:
        print(f"Section '{section}' not found")
        return False
    
    # Find next section or end of file
    lines = text.split('\n')
    section_idx = None
    next_section_idx = len(lines)
    
    for i, line in enumerate(lines):
        if line.strip() == section_header:
            section_idx = i
        elif section_idx is not None and line.startswith('## ') and i > section_idx:
            next_section_idx = i
            break
    
    if section_idx is None:
        print(f"Section '{section}' not found")
        return False
    
    # Insert content before next section
    new_lines = lines[:next_section_idx]
    new_lines.append(f"- {content}")
    new_lines.extend(lines[next_section_idx:])
    
    filepath.write_text('\n'.join(new_lines), encoding='utf-8')
    print(f"Added to {section}: {content[:60]}...")
    return True

def log_conversation(summary, category="Summary"):
    """Log a conversation summary"""
    filepath = get_today_file()
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    
    if not filepath.exists():
        create_daily_template(filepath)
    
    append_to_section(filepath, category, summary)

def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: log_memory.py <content> [section]")
        print("  section: Summary (default), Career, Venture, Family, Decisions, Learnings")
        sys.exit(1)
    
    content = sys.argv[1]
    section = sys.argv[2] if len(sys.argv) > 2 else "Summary"
    
    log_conversation(content, section)

if __name__ == "__main__":
    main()
