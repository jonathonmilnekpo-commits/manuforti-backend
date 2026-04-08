#!/usr/bin/env python3
"""
Conversation Logger for Aiden
Automatically logs Telegram/Terminal conversations to daily memory files
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"

def log_conversation(date_str, platform, topics, decisions, links):
    """Log a conversation to the daily memory file"""
    
    # Ensure directory exists
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    
    # File path
    memory_file = MEMORY_DIR / f"{date_str}.md"
    
    # Build content
    content = f"""## {date_str} — {platform.title()}

**Platform:** {platform.title()}  
**Time:** {datetime.now().strftime('%H:%M')} Oslo time

### Topics Discussed

"""
    
    for topic in topics:
        content += f"- {topic}\n"
    
    if decisions:
        content += "\n### Key Decisions\n\n"
        for decision in decisions:
            content += f"- {decision}\n"
    
    if links:
        content += "\n### Links & References\n\n"
        for link in links:
            content += f"- {link}\n"
    
    # Append to file (create if doesn't exist)
    if memory_file.exists():
        with open(memory_file, 'a') as f:
            f.write("\n" + content)
    else:
        with open(memory_file, 'w') as f:
            f.write(f"# {date_str}\n\n" + content)
    
    print(f"Logged to: {memory_file}")


def retroactive_log(date_str, platform, summary, topics, outcomes):
    """Create a retroactive log entry"""
    
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    memory_file = MEMORY_DIR / f"{date_str}.md"
    
    content = f"""## {date_str} — {platform.title()} (Retroactive)

**Platform:** {platform.title()}  
**Summary:** {summary}

### Topics Discussed

"""
    
    for topic in topics:
        content += f"- {topic}\n"
    
    if outcomes:
        content += "\n### Outcomes & Links\n\n"
        for outcome in outcomes:
            content += f"- {outcome}\n"
    
    # Write file
    with open(memory_file, 'w') as f:
        f.write(f"# {date_str}\n\n" + content)
    
    print(f"Created retroactive log: {memory_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python conversation_logger.py log <date> <platform> '<topics>' '<decisions>' '<links>'")
        print("  python conversation_logger.py retro <date> <platform> '<summary>' '<topics>' '<outcomes>'")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "log":
        # log <date> <platform> '<topics>' '<decisions>' '<links>'
        date_str = sys.argv[2]
        platform = sys.argv[3]
        topics = sys.argv[4].split('|') if len(sys.argv) > 4 else []
        decisions = sys.argv[5].split('|') if len(sys.argv) > 5 else []
        links = sys.argv[6].split('|') if len(sys.argv) > 6 else []
        
        log_conversation(date_str, platform, topics, decisions, links)
    
    elif command == "retro":
        # retro <date> <platform> '<summary>' '<topics>' '<outcomes>'
        date_str = sys.argv[2]
        platform = sys.argv[3]
        summary = sys.argv[4] if len(sys.argv) > 4 else ""
        topics = sys.argv[5].split('|') if len(sys.argv) > 5 else []
        outcomes = sys.argv[6].split('|') if len(sys.argv) > 6 else []
        
        retroactive_log(date_str, platform, summary, topics, outcomes)
    
    else:
        print("Unknown command")
        sys.exit(1)


if __name__ == "__main__":
    main()
