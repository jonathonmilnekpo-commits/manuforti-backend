const express = require('express');
const cors = require('cors');
const path = require('path');
const memoryConnector = require('./memory-connector');

const app = express();
const PORT = process.env.PORT || 3456;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname)));

// API Routes

// Get all memory data organized by month
app.get('/api/memory', (req, res) => {
    try {
        const data = memoryConnector.scanMemoryFiles();
        res.json(data);
    } catch (error) {
        console.error('Error scanning memory files:', error);
        res.status(500).json({ error: 'Failed to scan memory files' });
    }
});

// Get specific memory file
app.get('/api/memory/:date', (req, res) => {
    try {
        const { date } = req.params;
        const content = memoryConnector.readMemoryFile(date);
        
        if (!content) {
            return res.status(404).json({ error: 'Memory file not found' });
        }
        
        res.json({ date, content });
    } catch (error) {
        console.error('Error reading memory file:', error);
        res.status(500).json({ error: 'Failed to read memory file' });
    }
});

// Get long-term memory
app.get('/api/long-term-memory', (req, res) => {
    try {
        const content = memoryConnector.readLongTermMemory();
        res.json({ content });
    } catch (error) {
        console.error('Error reading long-term memory:', error);
        res.status(500).json({ error: 'Failed to read long-term memory' });
    }
});

// Search memory
app.get('/api/search', (req, res) => {
    try {
        const { q } = req.query;
        
        if (!q) {
            return res.status(400).json({ error: 'Query parameter required' });
        }
        
        const results = memoryConnector.searchMemory(q);
        res.json({ query: q, results });
    } catch (error) {
        console.error('Error searching memory:', error);
        res.status(500).json({ error: 'Failed to search memory' });
    }
});

// Create today's memory entry
app.post('/api/memory/today', (req, res) => {
    try {
        const { summary } = req.body;
        const filePath = memoryConnector.createTodayEntry(summary || 'Daily log');
        res.json({ success: true, filePath });
    } catch (error) {
        console.error('Error creating today entry:', error);
        res.status(500).json({ error: 'Failed to create entry' });
    }
});

// Append to today's memory
app.post('/api/memory/today/append', (req, res) => {
    try {
        const { section, content } = req.body;
        
        if (!section || !content) {
            return res.status(400).json({ error: 'Section and content required' });
        }
        
        memoryConnector.appendToToday(section, content);
        res.json({ success: true });
    } catch (error) {
        console.error('Error appending to today:', error);
        res.status(500).json({ error: 'Failed to append' });
    }
});

// Serve the main app
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 Mission Control running at http://localhost:${PORT}`);
    console.log(`📊 Memory directory: ${path.join(__dirname, '..', 'memory')}`);
});

module.exports = app;
