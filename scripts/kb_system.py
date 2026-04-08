#!/usr/bin/env python3
"""
Aiden Knowledge Base System
Karpathy-style LLM-maintained wiki for Manu Forti, Crab, Doctor, and all operations
"""

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Base directory for knowledge base
KB_DIR = Path.home() / ".openclaw" / "workspace" / "kb"
RAW_DIR = KB_DIR / "raw"
WIKI_DIR = KB_DIR / "wiki"
INDEX_FILE = WIKI_DIR / "index.md"

class AidenKnowledgeBase:
    """Karpathy-style knowledge base for Aiden's operations"""
    
    def __init__(self):
        self.kb_dir = KB_DIR
        self.raw_dir = RAW_DIR
        self.wiki_dir = WIKI_DIR
        self._ensure_dirs()
    
    def _ensure_dirs(self):
        """Create directory structure"""
        # Raw directories by source
        (self.raw_dir / "manuforti").mkdir(parents=True, exist_ok=True)
        (self.raw_dir / "crab").mkdir(parents=True, exist_ok=True)
        (self.raw_dir / "doctor").mkdir(parents=True, exist_ok=True)
        (self.raw_dir / "technical").mkdir(parents=True, exist_ok=True)
        (self.raw_dir / "conversations").mkdir(parents=True, exist_ok=True)
        
        # Wiki directories by topic
        (self.wiki_dir / "products").mkdir(parents=True, exist_ok=True)
        (self.wiki_dir / "agents").mkdir(parents=True, exist_ok=True)
        (self.wiki_dir / "workflows").mkdir(parents=True, exist_ok=True)
        (self.wiki_dir / "learnings").mkdir(parents=True, exist_ok=True)
        (self.wiki_dir / "concepts").mkdir(parents=True, exist_ok=True)
    
    def ingest_file(self, source_path: Path, category: str, metadata: Dict = None):
        """Ingest a file into raw/ directory"""
        target_dir = self.raw_dir / category
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy file with timestamp prefix
        timestamp = datetime.now().strftime("%Y%m%d")
        target_name = f"{timestamp}_{source_path.name}"
        target_path = target_dir / target_name
        
        shutil.copy2(source_path, target_path)
        
        # Create metadata file
        meta = {
            "original_path": str(source_path),
            "ingested_at": datetime.now().isoformat(),
            "category": category,
            "filename": source_path.name,
            **(metadata or {})
        }
        
        meta_path = target_path.with_suffix('.meta.json')
        with open(meta_path, 'w') as f:
            json.dump(meta, f, indent=2)
        
        print(f"Ingested: {source_path} → {target_path}")
        return target_path
    
    def ingest_conversation(self, date: str, platform: str, content: str, topics: List[str]):
        """Ingest a conversation summary"""
        filename = f"{date}_{platform}.md"
        target_path = self.raw_dir / "conversations" / filename
        
        # Format conversation entry
        entry = f"""# Conversation: {date}

**Platform:** {platform}  
**Date:** {date}

## Topics
"""
        for topic in topics:
            entry += f"- {topic}\n"
        
        entry += f"\n## Content\n\n{content}\n"
        
        with open(target_path, 'w') as f:
            f.write(entry)
        
        return target_path
    
    def create_index(self):
        """Create master index of all raw documents"""
        index = {
            "last_updated": datetime.now().isoformat(),
            "total_documents": 0,
            "categories": {}
        }
        
        # Scan all raw directories
        for category_dir in self.raw_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                docs = []
                
                for doc in category_dir.glob("*.md"):
                    # Load metadata if exists
                    meta_path = doc.with_suffix('.meta.json')
                    if meta_path.exists():
                        with open(meta_path, 'r') as f:
                            meta = json.load(f)
                    else:
                        meta = {}
                    
                    docs.append({
                        "filename": doc.name,
                        "path": str(doc.relative_to(self.raw_dir)),
                        **meta
                    })
                
                index["categories"][category] = {
                    "count": len(docs),
                    "documents": docs
                }
                index["total_documents"] += len(docs)
        
        # Save index
        with open(INDEX_FILE, 'w') as f:
            json.dump(index, f, indent=2)
        
        # Also create markdown index
        md_index = self._generate_markdown_index(index)
        with open(WIKI_DIR / "README.md", 'w') as f:
            f.write(md_index)
        
        print(f"Index created: {index['total_documents']} documents")
        return index
    
    def _generate_markdown_index(self, index: Dict) -> str:
        """Generate markdown version of index"""
        md = f"""# Aiden Knowledge Base Index

**Last Updated:** {index['last_updated'][:10]}  
**Total Documents:** {index['total_documents']}

## Quick Stats

"""
        for category, data in index['categories'].items():
            md += f"- **{category.title()}:** {data['count']} documents\n"
        
        md += "\n## Categories\n\n"
        
        for category, data in index['categories'].items():
            md += f"### {category.title()}\n\n"
            for doc in data['documents'][:10]:  # Top 10
                md += f"- {doc['filename']}\n"
            if len(data['documents']) > 10:
                md += f"- ... and {len(data['documents']) - 10} more\n"
            md += "\n"
        
        return md
    
    def query_kb(self, query: str) -> Dict:
        """Query the knowledge base"""
        # Load index
        if not INDEX_FILE.exists():
            return {"error": "Index not found. Run create_index() first."}
        
        with open(INDEX_FILE, 'r') as f:
            index = json.load(f)
        
        # Simple keyword search (placeholder for LLM query)
        results = []
        for category, data in index['categories'].items():
            for doc in data['documents']:
                if query.lower() in doc['filename'].lower():
                    results.append(doc)
        
        return {
            "query": query,
            "results_count": len(results),
            "results": results[:20]  # Top 20
        }
    
    def migrate_existing_memory(self):
        """Migrate existing memory files into KB structure"""
        memory_dir = Path.home() / ".openclaw" / "workspace" / "memory"
        
        migrated = 0
        
        # Migrate daily memory files
        for mem_file in memory_dir.glob("2026-*.md"):
            self.ingest_file(mem_file, "conversations", {
                "type": "daily_memory",
                "original_location": str(mem_file)
            })
            migrated += 1
        
        # Migrate subdirectories
        for subdir in ["manuforti", "statkraft", "technical", "venture"]:
            subdir_path = memory_dir / subdir
            if subdir_path.exists():
                for mem_file in subdir_path.glob("*.md"):
                    self.ingest_file(mem_file, subdir, {
                        "type": "categorized_memory",
                        "original_location": str(mem_file)
                    })
                    migrated += 1
        
        print(f"Migrated {migrated} files to knowledge base")
        return migrated
    
    def get_stats(self) -> Dict:
        """Get knowledge base statistics"""
        stats = {
            "raw_documents": 0,
            "wiki_articles": 0,
            "categories": [],
            "total_size_mb": 0
        }
        
        # Count raw documents
        for category_dir in self.raw_dir.iterdir():
            if category_dir.is_dir():
                docs = list(category_dir.glob("*.md"))
                stats["raw_documents"] += len(docs)
                stats["categories"].append({
                    "name": category_dir.name,
                    "count": len(docs)
                })
                
                # Calculate size
                for doc in docs:
                    stats["total_size_mb"] += doc.stat().st_size / (1024 * 1024)
        
        # Count wiki articles
        if self.wiki_dir.exists():
            stats["wiki_articles"] = len(list(self.wiki_dir.rglob("*.md")))
        
        stats["total_size_mb"] = round(stats["total_size_mb"], 2)
        
        return stats


def main():
    """CLI entry point"""
    import sys
    
    kb = AidenKnowledgeBase()
    
    if len(sys.argv) < 2:
        print("Aiden Knowledge Base System")
        print("")
        print("Usage:")
        print("  python kb_system.py init              # Initialize KB structure")
        print("  python kb_system.py migrate           # Migrate existing memory")
        print("  python kb_system.py index             # Create/update index")
        print("  python kb_system.py stats             # Show KB statistics")
        print("  python kb_system.py query <text>      # Query the KB")
        print("")
        print("Directories:")
        print(f"  Raw:     {RAW_DIR}")
        print(f"  Wiki:    {WIKI_DIR}")
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "init":
        print("Knowledge base initialized")
        print(f"Raw directory: {RAW_DIR}")
        print(f"Wiki directory: {WIKI_DIR}")
    
    elif command == "migrate":
        count = kb.migrate_existing_memory()
        print(f"\nMigrated {count} files")
        kb.create_index()
    
    elif command == "index":
        kb.create_index()
        print(f"\nIndex created at: {INDEX_FILE}")
    
    elif command == "stats":
        stats = kb.get_stats()
        print(json.dumps(stats, indent=2))
    
    elif command == "query" and len(sys.argv) > 2:
        query = " ".join(sys.argv[2:])
        results = kb.query_kb(query)
        print(json.dumps(results, indent=2))
    
    else:
        print("Unknown command")
        sys.exit(1)


if __name__ == "__main__":
    main()
