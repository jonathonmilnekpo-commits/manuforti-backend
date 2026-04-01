# Mission Control - Daily Memory Tracker

A smart command center for tracking daily interactions with Aiden, featuring a navigation sidebar and expandable date-based memory browser.

![Mission Control Interface](mission-control-preview.png)

## Features

### 🧠 Memory System
- **Daily Journal**: Automatic logging of every conversation (Telegram + Terminal)
- **Long-Term Memory**: Curated knowledge base from MEMORY.md
- **Month/Date Navigation**: Click months to expand, click days to view logs
- **Search**: Full-text search across all memory files

### 🎨 Dashboard Design
- **Sidebar Navigation**: 15+ icons matching Alex Finn's Mission Control
- **Dark Theme**: Sleek navy/black gradient design
- **Expandable Months**: Collapsible date tree
- **Real-time Updates**: Auto-refresh when new memories are added

### 📊 Data Integration
- Reads from `memory/YYYY-MM-DD.md` files
- Syncs with `MEMORY.md` for long-term context
- Captures both Telegram and Terminal conversations
- Tracks word counts and file sizes

## Installation

```bash
cd mission-control
npm install
npm start
```

Then open: http://localhost:3456

## How It Works

### Automatic Logging
Every conversation we have gets summarized and saved to `memory/YYYY-MM-DD.md`:

```markdown
# Daily Memory - 2026-03-27 (Friday)

## Summary
Discussed Mission Control dashboard implementation and memory tracking system.

## Career (Statkraft)
- Reviewed SVP Procurement succession timeline

## Venture (Manu Forti)
- Built Mission Control memory dashboard
- Planned Canva API integration

## Family
- Ragnhild's pregnancy update
- Gordon due June 1, 2026

## Key Decisions
- Implemented expandable month/day navigation
- Set up automatic conversation logging

## Links & References
- [GitHub Pages Guide](Manu_Forti_Website_Deployment_Guide.docx)
- [Canva API Guide](Canva_API_Setup_Guide.docx)
```

### Navigation Structure
```
Mission Control
├── Tasks
├── Agents
├── Content
├── Approvals
├── Calendar
├── Radar
├── Projects
├── Memory (ACTIVE)
│   ├── Long-Term Memory
│   ├── March 2026 ▼
│   │   ├── Fri, Mar 27 - Mission Control Setup (856 words)
│   │   ├── Thu, Mar 26 - YouTube Video Review (1,203 words)
│   │   └── Wed, Mar 25 - Daily Briefing (645 words)
│   └── February 2026 ▼
├── Docs
├── People
├── Office
├── Team
├── System
├── Radar
├── Factory
├── Pipeline
├── AI Lab
└── Feedback
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/memory` | GET | Get all memory data by month |
| `/api/memory/:date` | GET | Get specific day (YYYY-MM-DD) |
| `/api/long-term-memory` | GET | Get MEMORY.md content |
| `/api/search?q=query` | GET | Search all memory files |
| `/api/memory/today` | POST | Create today's entry |
| `/api/memory/today/append` | POST | Append to today's section |

## Usage Example

```javascript
// Fetch today's memory
fetch('/api/memory/2026-03-27')
  .then(r => r.json())
  .then(data => console.log(data.content));

// Search for "Manu Forti"
fetch('/api/search?q=Manu+Forti')
  .then(r => r.json())
  .then(data => console.log(data.results));

// Add to today's log
fetch('/api/memory/today/append', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    section: 'Venture (Manu Forti)',
    content: 'Completed Mission Control dashboard'
  })
});
```

## Integration with Aiden

### What Gets Logged
1. **Telegram conversations** → Saved to daily memory
2. **Terminal sessions** → Saved to daily memory  
3. **File modifications** → Tracked with metadata
4. **Cron job outputs** → Captured and summarized
5. **Decisions made** → Highlighted in Key Decisions section

### Referencing Past Conversations
When you ask "What did we discuss about X on Tuesday?", Aiden will:
1. Search the memory index for "X" and "Tuesday"
2. Find the relevant daily memory file
3. Extract the specific section
4. Provide context with date and related decisions

## File Structure

```
mission-control/
├── index.html              # Main dashboard UI
├── server.js               # Express API server
├── memory-connector.js     # File system integration
├── package.json            # Dependencies
├── README.md               # This file
└── mission-control-preview.png  # Screenshot
```

## Customization

### Adding New Sections
Edit `index.html` and add to the sidebar:

```html
<div class="nav-item" data-section="analytics">
    <svg>...</svg>
    <span>Analytics</span>
</div>
```

### Changing Colors
Modify the CSS variables in `index.html`:

```css
:root {
    --primary: #3b82f6;
    --secondary: #06b6d4;
    --background: #0f1419;
}
```

## Next Steps

1. **Install dependencies**: `npm install`
2. **Start server**: `npm start`
3. **Open dashboard**: http://localhost:3456
4. **Begin logging**: Every conversation now auto-saves
5. **Search memories**: Use the search bar to find past discussions

## Troubleshooting

**Issue**: Memory files not showing
- Check that `memory/` directory exists
- Verify files are named `YYYY-MM-DD.md`

**Issue**: Server won't start
- Check if port 3456 is in use: `lsof -i :3456`
- Try different port: `PORT=3000 npm start`

**Issue**: Search not working
- Ensure `glob` package is installed
- Check file permissions on memory directory

## Future Enhancements

- [ ] Real-time sync via WebSocket
- [ ] Mobile-responsive design
- [ ] Export to PDF/Word
- [ ] Graph visualization of topics
- [ ] Integration with calendar events
- [ ] Voice memo transcription
- [ ] AI-powered memory summarization

---

Built for Jonathon Milne | Aiden Mission Control v1.0
