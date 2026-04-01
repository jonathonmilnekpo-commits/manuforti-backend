#!/bin/bash

# Mission Control Startup Script
# Usage: ./start-mission-control.sh

echo "🚀 Starting Mission Control..."
echo ""

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Check if memory directory exists
if [ ! -d "../memory" ]; then
    echo "📁 Creating memory directory..."
    mkdir -p ../memory
fi

# Start the server
echo "🌐 Launching dashboard..."
echo ""
echo "Mission Control will be available at:"
echo "  http://localhost:3456"
echo ""
echo "Press Ctrl+C to stop"
echo ""

node server.js
