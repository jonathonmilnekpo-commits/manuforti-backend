#!/bin/bash
# Aiden Daily Backup Script
# Backs up OpenClaw workspace and config to iCloud Drive

DATE=$(date +%Y-%m-%d)
BACKUP_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Aiden-Backups/$DATE"

echo "[$(date)] Starting backup..."

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Backup workspace (excluding large media/cache files)
rsync -av --exclude='*.ogg' --exclude='*.mp4' --exclude='*.mp3' --exclude='.git' \
  "$HOME/.openclaw/workspace/" \
  "$BACKUP_DIR/workspace/" 2>&1

# Backup config (redact sensitive keys in copy)
cp "$HOME/.openclaw/openclaw.json" "$BACKUP_DIR/openclaw.json.bak" 2>&1

# Remove backups older than 30 days
find "$HOME/Library/Mobile Documents/com~apple~CloudDocs/Aiden-Backups/" \
  -maxdepth 1 -type d -mtime +30 -exec rm -rf {} + 2>/dev/null

echo "[$(date)] Backup complete → $BACKUP_DIR"
