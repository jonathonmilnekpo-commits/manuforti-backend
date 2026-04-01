#!/usr/bin/env python3
"""
Generate Morning Briefing with OpenClaw Updates
Called by daily cron job at 07:00 Oslo time
"""

import os
import glob
from datetime import datetime, timezone
from pathlib import Path

def get_latest_openclaw_update():
    """Find and read the latest OpenClaw update file"""
    workspace = Path.home() / ".openclaw" / "workspace" / "memory"
    update_files = list(workspace.glob("openclaw_updates_*.md"))
    
    if not update_files:
        return None
    
    # Get most recent file
    latest = max(update_files, key=lambda p: p.stat().st_mtime)
    
    with open(latest, 'r') as f:
        content = f.read()
    
    # Extract key points (first 500 chars or key sections)
    lines = content.split('\n')
    summary = []
    for line in lines[:30]:  # First 30 lines
        if line.strip() and not line.startswith('---'):
            summary.append(line)
    
    return '\n'.join(summary[:20])  # Limit output

def get_critical_security_flags():
    """Check for critical security updates"""
    workspace = Path.home() / ".openclaw" / "workspace" / "memory"
    update_files = list(workspace.glob("openclaw_updates_*.md"))
    
    critical_items = []
    
    for file in sorted(update_files, key=lambda p: p.stat().st_mtime, reverse=True)[:3]:
        with open(file, 'r') as f:
            content = f.read()
        
        # Look for critical/security keywords
        if any(keyword in content.lower() for keyword in ['critical', 'cve', 'vulnerability', 'security', 'patch']):
            lines = content.split('\n')
            for line in lines:
                if any(keyword in line.lower() for keyword in ['critical', 'cve', 'vulnerability', 'security patch']):
                    critical_items.append(line.strip())
    
    return list(set(critical_items))[:5]  # Unique items, max 5

def generate_briefing():
    """Generate the morning briefing"""
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    
    briefing = f"""# Morning Briefing — {date_str}

> **"Build a life where professional excellence funds family freedom — and use AI to do both better, together."**

---

## 🦞 OpenClaw & AI Tools Update

"""
    
    # Add critical security flags first
    critical = get_critical_security_flags()
    if critical:
        briefing += "### ⚠️ Critical Security Updates\n\n"
        for item in critical:
            briefing += f"- {item}\n"
        briefing += "\n"
    
    # Add latest update summary
    update = get_latest_openclaw_update()
    if update:
        briefing += "### Latest Updates (Last 24h)\n\n"
        briefing += update
        briefing += "\n\n"
    else:
        briefing += "*No new OpenClaw updates in the last 24 hours.*\n\n"
    
    # Add action items
    briefing += """### Recommended Actions

- [ ] Review any breaking changes affecting Venture cron jobs
- [ ] Check if security patches require immediate update
- [ ] Note new features that could improve agent operations

---

## 📋 Other Briefing Sections

*[To be filled by main briefing generator]*

- Career (Statkraft)
- AI Business / Manu Forti
- Family Focus
- Active Projects

---

*OpenClaw research runs nightly at 02:00 GMT | Briefing generated at 07:00 Oslo time*
"""
    
    return briefing

def main():
    briefing = generate_briefing()
    
    # Save to memory
    output_path = Path.home() / ".openclaw" / "workspace" / "memory" / f"morning_briefing_{datetime.now().strftime('%Y-%m-%d')}.md"
    
    with open(output_path, 'w') as f:
        f.write(briefing)
    
    print(f"✓ Morning briefing saved to: {output_path}")
    print("\n" + "="*60)
    print(briefing)

if __name__ == '__main__':
    main()
