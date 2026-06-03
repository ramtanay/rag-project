# AI Study Assistant Frontend

A simple, clean web interface for the AI Study Assistant RAG backend. Built with vanilla HTML, CSS, and JavaScript - no framework dependencies required.

## Overview

This frontend provides a user-friendly interface for:
- **📄 Uploading PDFs** - Select and upload study materials
- **❓ Asking Questions** - Submit natural language queries about uploaded documents
- **📖 Viewing Answers** - See AI-generated answers with source material references

## Getting Started

### Quick Start

1. **Make sure backend is running:**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. **Open frontend in browser:**
   
   Option A - Direct open:
   ```bash
   open frontend/index.html
   ```
   
   Option B - Local server (recommended):
   ```bash
   python -m http.server 8080 --directory frontend
   # Visit: http://localhost:8080
   ```

## Files Overview

| File | Purpose |
|------|---------|
| `index.html` | Semantic HTML structure |
| `styles.css` | Responsive CSS styling (~350 lines) |
| `app.js` | Application logic & state management (~250 lines) |
| `ui.js` | DOM manipulation & rendering (~200 lines) |
| `api.js` | Backend API communication (~90 lines) |

**Total: ~1000 lines of code, zero external dependencies**

## How It Works

### User Flow

**Upload:**
```
1. User selects/drags PDF
2. Frontend validates it's a PDF
3. Shows "Uploading..." status
4. Sends file to /upload endpoint
5. Backend processes: extract → chunk → embed → store
6. Shows success with filename and chunk count
7. Document added to tracking
```

**Question:**
```
1. User enters question
2. Frontend validates question and documents exist
3. Shows "Searching..." status
4. Sends question to /ask endpoint
5. Backend searches embeddings and generates answer
6. Shows results with answer and source chunks
```

## Architecture

```
Frontend (HTML/CSS/JS)
    ↓ (HTTP Fetch)
Backend (FastAPI)
    ↓ (JSON)
Frontend (Display)
```

## Features

✅ **Upload PDFs** - File picker + drag-drop support  
✅ **Ask Questions** - Natural language queries  
✅ **Display Results** - Answers + source material  
✅ **Status Feedback** - Loading spinners, messages  
✅ **Responsive** - Works on desktop and mobile  
✅ **Session State** - Track uploads during session  
✅ **Simple Code** - Direct, readable, well-commented  

## State Management

Simple state object in `app.js`:
```javascript
appState = {
    uploadedDocs: [],      // Uploaded files
    hasDocuments: false,   // Ready for queries
    isUploading: false,    // Upload in progress
    isQuerying: false,     // Query in progress
    currentQuestion: null, // Current question
    currentAnswer: null,   // Current answer
    currentChunks: [],     // Retrieved chunks
    lastError: null        // Error state
}
```

## Customization

### Change Backend URL
Edit `api.js`:
```javascript
const API_BASE = 'http://your-backend-url:8000';
```

### Modify Colors
Edit `styles.css`:
- Primary color: `#667eea`
- Accent color: `#764ba2`

## Browser Support

Works in modern browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Backend unreachable" | Backend not running on port 8000 |
| Frontend won't load | Check file paths are correct |
| Upload fails | Ensure backend has write permission to uploads/ |
| No answers | Verify PDF was processed (check chunk count) |

## Code Style

Matches backend approach:
- Direct, readable functions
- Clear naming conventions
- Minimal abstractions
- Helpful comments
- No complex patterns

## Next Steps

1. Run backend server
2. Open frontend in browser
3. Upload a PDF
4. Ask a question
5. See AI-powered answer with sources
