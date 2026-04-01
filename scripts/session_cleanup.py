#!/usr/bin/env python3
"""
Session Cleanup - Cleans up stale agent session files.
Removes temporary, backup, and stale files from agent sessions.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime, timedelta

# Configuration
AGENTS_DIR = Path("/Users/jonathonmilne/.openclaw/agents")
SESSION_RETENTION_DAYS = 7  # Keep sessions for 7 days
DRY_RUN = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")

def get_file_age_days(path: Path) -> float:
    """Get file age in days."""
    try:
        stat = path.stat()
        mtime = datetime.fromtimestamp(stat.st_mtime)
        return (datetime.now() - mtime).total_seconds() / 86400
    except Exception:
        return 0

def delete_file(path: Path, dry_run: bool = False) -> bool:
    """Delete a file, respecting dry-run mode."""
    try:
        if dry_run:
            print(f"  [DRY-RUN] Would delete: {path}")
            return True
        path.unlink()
        print(f"  Deleted: {path}")
        return True
    except Exception as e:
        print(f"  ERROR deleting {path}: {e}")
        return False

def remove_pattern(directory: Path, pattern: str, dry_run: bool = False) -> int:
    """Remove files matching pattern in directory."""
    count = 0
    if not directory.exists():
        return count
    
    for file_path in directory.glob(pattern):
        if file_path.is_file():
            if delete_file(file_path, dry_run):
                count += 1
    return count

def cleanup_agent_sessions(agent_dir: Path, dry_run: bool = False) -> dict:
    """Clean up sessions for a single agent."""
    results = {
        "temp_deleted": 0,
        "backup_deleted": 0,
        "stale_deleted": 0,
        "sessions_scanned": 0
    }
    
    sessions_dir = agent_dir / "sessions"
    if not sessions_dir.exists():
        return results
    
    # Clean up temp files
    results["temp_deleted"] += remove_pattern(sessions_dir, "*.tmp", dry_run)
    results["temp_deleted"] += remove_pattern(sessions_dir, "*.temp", dry_run)
    
    # Clean up backup files
    results["backup_deleted"] += remove_pattern(sessions_dir, "*.bak", dry_run)
    results["backup_deleted"] += remove_pattern(sessions_dir, "*.backup", dry_run)
    results["backup_deleted"] += remove_pattern(sessions_dir, "*.bak-*", dry_run)
    
    # Clean up lock files
    remove_pattern(sessions_dir, "*.lock", dry_run)
    
    # Clean up reset/deleted session files
    results["temp_deleted"] += remove_pattern(sessions_dir, ".reset.*", dry_run)
    results["temp_deleted"] += remove_pattern(sessions_dir, ".deleted.*", dry_run)
    
    # Scan session folders for stale content
    for session_dir in sessions_dir.iterdir():
        if not session_dir.is_dir():
            continue
        
        results["sessions_scanned"] += 1
        
        # Check session age
        age_days = get_file_age_days(session_dir)
        
        # Clean old checkpoint files
        for checkpoint in session_dir.glob("checkpoint-*.json"):
            cp_age = get_file_age_days(checkpoint)
            if cp_age > SESSION_RETENTION_DAYS:
                if delete_file(checkpoint, dry_run):
                    results["stale_deleted"] += 1
        
        # Clean old cache files
        for cache_file in session_dir.glob("*.cache"):
            cache_age = get_file_age_days(cache_file)
            if cache_age > SESSION_RETENTION_DAYS:
                if delete_file(cache_file, dry_run):
                    results["stale_deleted"] += 1
        
        # Remove empty session directories older than retention period
        if age_days > SESSION_RETENTION_DAYS * 2:  # 2x retention for entire sessions
            try:
                # Check if directory is empty or only contains metadata
                files = list(session_dir.iterdir())
                if len(files) == 0 or (len(files) == 1 and files[0].name == "sessions.json"):
                    if dry_run:
                        print(f"  [DRY-RUN] Would remove stale session dir: {session_dir.name}")
                    else:
                        # Only remove if truly empty
                        if len(files) == 0:
                            session_dir.rmdir()
                            print(f"  Removed empty session dir: {session_dir.name}")
                        else:
                            # Check if sessions.json is old
                            json_age = get_file_age_days(files[0])
                            if json_age > SESSION_RETENTION_DAYS * 2:
                                files[0].unlink()
                                session_dir.rmdir()
                                print(f"  Removed stale session dir: {session_dir.name}")
            except Exception as e:
                print(f"  ERROR removing session dir {session_dir.name}: {e}")
    
    return results

def main():
    """Main cleanup function."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting session cleanup...")
    
    if DRY_RUN:
        print("*** DRY RUN MODE - No files will actually be deleted ***\n")
    
    if not AGENTS_DIR.exists():
        print(f"ERROR: Agents directory not found: {AGENTS_DIR}")
        return
    
    total_results = {
        "agents_scanned": 0,
        "temp_deleted": 0,
        "backup_deleted": 0,
        "stale_deleted": 0,
        "sessions_scanned": 0
    }
    
    # Process each agent
    for agent_dir in AGENTS_DIR.iterdir():
        if not agent_dir.is_dir():
            continue
        
        agent_name = agent_dir.name
        print(f"\nScanning agent: {agent_name}")
        
        results = cleanup_agent_sessions(agent_dir, DRY_RUN)
        
        total_results["agents_scanned"] += 1
        total_results["temp_deleted"] += results["temp_deleted"]
        total_results["backup_deleted"] += results["backup_deleted"]
        total_results["stale_deleted"] += results["stale_deleted"]
        total_results["sessions_scanned"] += results["sessions_scanned"]
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Complete:")
    print(f"  Agents scanned: {total_results['agents_scanned']}")
    print(f"  Sessions scanned: {total_results['sessions_scanned']}")
    print(f"  Temp files removed: {total_results['temp_deleted']}")
    print(f"  Backup files removed: {total_results['backup_deleted']}")
    print(f"  Stale files removed: {total_results['stale_deleted']}")
    
    if DRY_RUN:
        print("\n*** This was a dry run. No files were actually deleted. ***")
        print("Set DRY_RUN=false to perform actual cleanup.")

if __name__ == "__main__":
    main()
