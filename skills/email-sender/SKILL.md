---
name: email-sender
description: Send emails using macOS Mail app or command line mail
tags: [email, communication, productivity]
user-invocable: true
---

# Email Sender Skill

Send emails via iCloud or configured email accounts on macOS.

## Capabilities

- Send emails with attachments via macOS Mail app
- Use AppleScript for reliable delivery through configured accounts
- Support for iCloud, Gmail, Outlook, or any Mail.app configured account

## Prerequisites

- macOS with Mail app configured
- At least one email account set up in Mail.app (iCloud recommended)

## Usage

### Send a simple email

```bash
openclaw email send --to "recipient@example.com" --subject "Subject" --body "Email body text"
```

### Send with attachment

```bash
openclaw email send --to "recipient@example.com" --subject "Subject" --body "See attached" --attach "/path/to/file.pdf"
```

### Using AppleScript (recommended for iCloud)

The skill uses AppleScript to control Mail.app, which ensures:
- Proper authentication via macOS keychain
- Access to all configured accounts (iCloud, Gmail, etc.)
- Delivery through the user's preferred mail server
- Automatic handling of attachments

## Configuration

No configuration needed — uses macOS Mail app settings automatically.

## Examples

**Send workshop presentation:**
```bash
openclaw email send \\
  --to "Jonathon.Milne137@gmail.com" \\
  --subject "Brazil 400MW Risk Workshop" \\
  --body "Please find the presentation attached." \\
  --attach "~/.openclaw/workspace/Brazil_400MW_Risk_Workshop_Executive.pptx"
```

## Troubleshooting

- **"Mail got an error"**: Ensure Mail.app is configured with at least one account
- **"Message not sent"**: Check Mail.app can send manually first
- **Attachments not sending**: Verify file path is correct and accessible
