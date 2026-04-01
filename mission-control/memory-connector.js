const fs = require('fs');
const path = require('path');
const glob = require('glob');

// Configuration
const MEMORY_DIR = path.join(__dirname, '..', 'memory');
const LONG_TERM_MEMORY = path.join(__dirname, '..', 'MEMORY.md');

/**
 * Scan memory directory and build data structure
 */
function scanMemoryFiles() {
    const memoryData = {};
    
    // Find all memory files
    const pattern = path.join(MEMORY_DIR, '**/*.md');
    const files = glob.sync(pattern);
    
    files.forEach(filePath => {
        const filename = path.basename(filePath);
        const match = filename.match(/(\d{4})-(\d{2})-(\d{2})\.md$/);
        
        if (match) {
            const [, year, month, day] = match;
            const monthKey = `${year}-${month}`;
            const dateKey = `${year}-${month}-${day}`;
            
            if (!memoryData[monthKey]) {
                memoryData[monthKey] = [];
            }
            
            // Read file stats
            const stats = fs.statSync(filePath);
            const content = fs.readFileSync(filePath, 'utf-8');
            
            // Extract title from first heading or use date
            const titleMatch = content.match(/^# (.+)$/m);
            const title = titleMatch ? titleMatch[1] : `Memory ${dateKey}`;
            
            // Count words
            const words = content.split(/\s+/).length;
            
            memoryData[monthKey].push({
                date: dateKey,
                day: formatDay(dateKey),
                title: title.replace(/^#\s*/, ''),
                words: words.toLocaleString(),
                size: formatBytes(stats.size),
                modified: stats.mtime,
                path: filePath
            });
        }
    });
    
    // Sort each month's entries by date (newest first)
    Object.keys(memoryData).forEach(month => {
        memoryData[month].sort((a, b) => new Date(b.date) - new Date(a.date));
    });
    
    return memoryData;
}

/**
 * Format date for display
 */
function formatDay(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { 
        weekday: 'short', 
        month: 'short', 
        day: 'numeric' 
    });
}

/**
 * Format bytes for display
 */
function formatBytes(bytes) {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
}

/**
 * Read specific memory file content
 */
function readMemoryFile(date) {
    const filePath = path.join(MEMORY_DIR, `${date}.md`);
    
    if (!fs.existsSync(filePath)) {
        return null;
    }
    
    return fs.readFileSync(filePath, 'utf-8');
}

/**
 * Read long-term memory
 */
function readLongTermMemory() {
    if (!fs.existsSync(LONG_TERM_MEMORY)) {
        return '# Long-Term Memory\n\nNo long-term memory file found.';
    }
    
    return fs.readFileSync(LONG_TERM_MEMORY, 'utf-8');
}

/**
 * Search across all memory files
 */
function searchMemory(query) {
    const results = [];
    const pattern = path.join(MEMORY_DIR, '**/*.md');
    const files = glob.sync(pattern);
    
    const searchRegex = new RegExp(query, 'gi');
    
    files.forEach(filePath => {
        const content = fs.readFileSync(filePath, 'utf-8');
        
        if (searchRegex.test(content)) {
            const filename = path.basename(filePath, '.md');
            const matches = [];
            
            // Find context around matches
            const lines = content.split('\n');
            lines.forEach((line, index) => {
                if (searchRegex.test(line)) {
                    matches.push({
                        line: index + 1,
                        text: line.trim()
                    });
                }
            });
            
            results.push({
                date: filename,
                matches: matches.slice(0, 5) // Limit to first 5 matches per file
            });
        }
    });
    
    return results;
}

/**
 * Create a new memory entry for today
 */
function createTodayEntry(summary) {
    const today = new Date().toISOString().split('T')[0];
    const filePath = path.join(MEMORY_DIR, `${today}.md`);
    
    const dayOfWeek = new Date().toLocaleDateString('en-US', { weekday: 'long' });
    
    const template = `# Daily Memory - ${today} (${dayOfWeek})

## Summary
${summary}

## Career (Statkraft)
- 

## Venture (Manu Forti)
- 

## Family
- 

## Key Decisions
- 

## Learnings
- 

## Links & References
- 

---
*Logged by Aiden*
`;
    
    if (!fs.existsSync(filePath)) {
        fs.writeFileSync(filePath, template, 'utf-8');
        console.log(`Created new memory entry: ${filePath}`);
    }
    
    return filePath;
}

/**
 * Append to today's memory
 */
function appendToToday(section, content) {
    const today = new Date().toISOString().split('T')[0];
    const filePath = path.join(MEMORY_DIR, `${today}.md`);
    
    if (!fs.existsSync(filePath)) {
        createTodayEntry('Auto-generated from conversation');
    }
    
    let existingContent = fs.readFileSync(filePath, 'utf-8');
    
    // Find the section and append
    const sectionRegex = new RegExp(`(## ${section}\\n)([\\s\\S]*?)(?=\\n## |\\n---|$)`);
    
    if (sectionRegex.test(existingContent)) {
        existingContent = existingContent.replace(sectionRegex, `$1$2- ${content}\n`);
        fs.writeFileSync(filePath, existingContent, 'utf-8');
        console.log(`Appended to ${section} in ${filePath}`);
    }
}

// Export functions for use in server
module.exports = {
    scanMemoryFiles,
    readMemoryFile,
    readLongTermMemory,
    searchMemory,
    createTodayEntry,
    appendToToday
};

// If run directly, scan and output JSON
if (require.main === module) {
    const data = scanMemoryFiles();
    console.log(JSON.stringify(data, null, 2));
}
