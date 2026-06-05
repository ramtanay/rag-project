/**
 * api.js - Backend API Communication Layer
 * 
 * This file contains all functions that communicate with the FastAPI backend.
 * It handles request formatting, response parsing, and error management.
 */

// Backend API base URL
const API_BASE = CONFIG.API_BASE;
/**
 * Check if a file is a valid PDF
 * 
 * @param {File} file - The file to validate
 * @returns {boolean} True if file is PDF, false otherwise
 */
function isPDF(file) {
    return file.type === 'application/pdf' || file.name.endsWith('.pdf');
}

/**
 * Upload a PDF file to the backend
 * 
 * This function sends the file to the /upload endpoint as multipart/form-data.
 * The backend processes the PDF, extracts text, chunks it, generates embeddings,
 * and stores them in FAISS.
 * 
 * @param {File} file - The PDF file to upload
 * @returns {Promise<Object>} Response with: {filename, total_chunks, embedding_dimension, message}
 * @throws {Error} If upload fails with descriptive error message
 */
async function uploadFile(file) {
    // Validate file is PDF
    if (!isPDF(file)) {
        throw new Error('Only PDF files are supported');
    }

    // Create FormData for multipart/form-data submission
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${API_BASE}/upload`, {
            method: 'POST',
            body: formData
        });

        // Handle HTTP errors
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Upload failed (${response.status}): ${errorText}`);
        }

        // Parse and return JSON response
        const data = await response.json();
        return data;

    } catch (error) {
        // Re-throw with context
        if (error instanceof TypeError) {
            throw new Error('Backend unreachable. Check that the backend is running on ' + API_BASE);
        }
        throw error;
    }
}

/**
 * Ask a question based on uploaded documents
 * 
 * This function sends a question to the /ask endpoint.
 * The backend searches for relevant chunks using embeddings and generates
 * an answer using the Groq LLM.
 * 
 * @param {string} question - The question to ask
 * @returns {Promise<Object>} Response with: {question, answer, retrieved_chunks}
 * @throws {Error} If query fails with descriptive error message
 */
async function askQuestion(question) {
    console.log('askQuestion() called with:', question);
    
    // Encode question as query parameter
    const params = new URLSearchParams({ question });
    const url = `${API_BASE}/ask?${params}`;
    
    console.log('Fetching URL:', url);

    try {
        const response = await fetch(url, {
            method: 'POST'
        });

        console.log('Response status:', response.status);

        // Handle HTTP errors
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Query failed (${response.status}): ${errorText}`);
        }

        // Parse and return JSON response
        const data = await response.json();
        console.log('Response data:', data);
        return data;

    } catch (error) {
        console.error('Error in askQuestion:', error);
        // Re-throw with context
        if (error instanceof TypeError) {
            throw new Error('Backend unreachable. Check that the backend is running on ' + API_BASE);
        }
        throw error;
    }
}
