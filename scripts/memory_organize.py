#!/usr/bin/env python3
"""
Memory Organizer - Organizes memory files into topic folders.
Categorizes files by topic and updates indexes.
"""

import re
import os
from pathlib import Path
from datetime import datetime

# Configuration
MEMORY_ROOT = Path("/Users/jonathonmilne/.openclaw/workspace/memory")
TOPICS = ["manuforti", "statkraft", "technical", "venture"]
FALLBACK_TOPIC = "misc"

# Keywords for categorization
TOPIC_KEYWORDS = {
    "manuforti": ["manuforti", "manufacturing", "supplier", "procurement", "vendor", "sourcing", "purchase", "acquisition"],
    "statkraft": ["statkraft", "energy", "power", "renewable", "electricity", "grid", "transmission"],
    "technical": ["technical", "technology", "software", "api", "system", "infrastructure", "engineering", "development"],
    "venture": ["venture", "business", "strategy", "market", "customer", "sales", "revenue", "growth", "investment"]
}

def extract_date_from_filename(filename: str) -> str:
    """Extract date from filename if present (YYYY-MM-DD format)."""
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        return date_match.group(1)
    return datetime.now().strftime('%Y-%m-%d')

def has_yaml_frontmatter(content: str) -> bool:
    """Check if content already has YAML frontmatter."""
    return content.strip().startswith('---')

def add_yaml_frontmatter(content: str, topic: str, date: str) -> str:
    """Add YAML frontmatter to content."""
    # Extract any existing tags from content (simple approach)
    tags = []
    hashtag_matches = re.findall(r'#(\w+)', content)
    tags.extend(hashtag_matches)
    
    # Add topic as tag
    if topic not in tags:
        tags.append(topic)
    
    frontmatter = f"""---
date: {date}
topic: {topic}
"""
    if tags:
        # Remove duplicates and format
        unique_tags = list(dict.fromkeys(tags))
        frontmatter += f"tags: {unique_tags}\n"
    
    frontmatter += "---\n\n"
    return frontmatter + content

def categorize_file(filename: str, content: str) -> str:
    """Determine topic category for a file based on filename and content."""
    filename_lower = filename.lower()
    content_lower = content.lower()
    
    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            if keyword in filename_lower or keyword in content_lower:
                return topic
    
    return FALLBACK_TOPIC

def update_index_md(topic_folder: Path):
    """Update INDEX.md in topic folder with file list."""
    index_path = topic_folder / "INDEX.md"
    md_files = list(topic_folder.glob("*.md"))
    md_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    lines = ["# Memory Index\n"]
    lines.append(f"**Topic:** {topic_folder.name}\n")
    lines.append(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    lines.append("## Files\n\n")
    
    for md_file in md_files:
        if md_file.name == "INDEX.md":
            continue
        stat = md_file.stat()
        mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')
        lines.append(f"- [{md_file.name}](./{md_file.name}) ({mtime})\n")
    
    index_path.write_text("".join(lines), encoding="utf-8")

def main():
    """Main function to organize memory files."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting memory organization...")
    
    # Ensure memory root exists
    if not MEMORY_ROOT.exists():
        print(f"Creating memory root: {MEMORY_ROOT}")
        MEMORY_ROOT.mkdir(parents=True)
    
    # Create topic folders
    for topic in TOPICS + [FALLBACK_TOPIC]:
        topic_folder = MEMORY_ROOT / topic
        topic_folder.mkdir(exist_ok=True)
    
    # Process loose .md files in memory root
    loose_files = [f for f in MEMORY_ROOT.glob("*.md") if f.is_file()]
    print(f"Found {len(loose_files)} loose files to process.")
    
    processed = 0
    skipped = 0
    errors = 0
    
    for file_path in loose_files:
        try:
            filename = file_path.name
            content = file_path.read_text(encoding="utf-8")
            
            # Determine topic
            topic = categorize_file(filename, content)
            print(f"  Processing: {filename} -> {topic}/")
            
            # Extract date from filename
            date = extract_date_from_filename(filename)
            
            # Add YAML frontmatter if missing
            if not has_yaml_frontmatter(content):
                new_content = add_yaml_frontmatter(content, topic, date)
                content = new_content
                print(f"    Added YAML frontmatter")
            
            # Move to topic folder
            topic_folder = MEMORY_ROOT / topic
            destination = topic_folder / filename
            
            # Avoid overwriting unless content is identical
            if destination.exists():
                existing_content = destination.read_text(encoding="utf-8")
                if existing_content == content:
                    print(f"    File identical, deleting source")
                    file_path.unlink()
                    skipped += 1
                    continue
                else:
                    # Add timestamp to filename to avoid conflict
                    stem = file_path.stem
                    suffix = file_path.suffix
                    timestamp = datetime.now().strftime('%H%M%S')
                    new_filename = f"{stem}_{timestamp}{suffix}"
                    destination = topic_folder / new_filename
                    print(f"    Renaming to {new_filename} to avoid conflict")
            
            # Write and remove source
            destination.write_text(content, encoding="utf-8")
            file_path.unlink()
            print(f"    Moved to {topic}/{destination.name}")
            processed += 1
            
        except Exception as e:
            print(f"    ERROR processing {file_path.name}: {e}")
            errors += 1
    
    # Update INDEX.md in each topic folder
    for topic in TOPICS + [FALLBACK_TOPIC]:
        topic_folder = MEMORY_ROOT / topic
        if topic_folder.exists():
            update_index_md(topic_folder)
            print(f"Updated index for {topic}/")
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Complete: {processed} processed, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
