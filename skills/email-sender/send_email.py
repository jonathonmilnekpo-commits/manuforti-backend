#!/usr/bin/env python3
"""
Email sender script for macOS Mail app
Uses AppleScript to send emails through configured accounts
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

def send_email_applescript(to, subject, body, attachment=None):
    """Send email using AppleScript and Mail.app"""
    
    # Build AppleScript
    script_parts = [
        'tell application "Mail"',
        '    set newMessage to make new outgoing message with properties {subject:"%s", content:"%s"}' % (subject.replace('"', '\\"'), body.replace('"', '\\"')),
        '    tell newMessage',
        '        make new to recipient at end of to recipients with properties {address:"%s"}' % to,
    ]
    
    if attachment:
        # Expand path and verify file exists
        attachment_path = os.path.expanduser(attachment)
        if not os.path.exists(attachment_path):
            print(f"Error: Attachment not found: {attachment_path}")
            sys.exit(1)
        
        script_parts.append('        make new attachment with properties {file name:"%s"} at after last paragraph' % attachment_path)
    
    script_parts.extend([
        '        send newMessage',
        '    end tell',
        'end tell'
    ])
    
    script = '\n'.join(script_parts)
    
    # Execute AppleScript
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"✓ Email sent successfully to {to}")
            if attachment:
                print(f"  Attachment: {os.path.basename(attachment)}")
            return True
        else:
            print(f"Error sending email: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("Error: Email send timed out")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Send email via macOS Mail app')
    parser.add_argument('--to', required=True, help='Recipient email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body text')
    parser.add_argument('--attach', help='Path to attachment file')
    
    args = parser.parse_args()
    
    success = send_email_applescript(args.to, args.subject, args.body, args.attach)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
