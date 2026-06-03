/**
 * ui.js - UI Utility Functions
 * 
 * This file contains all functions that directly manipulate the DOM.
 * It handles displaying/hiding elements, updating text, and managing UI state.
 */

/**
 * Update the status bar with a message and optional loading spinner
 * 
 * @param {string} message - The status message to display
 * @param {boolean} isLoading - If true, show loading spinner. Default false.
 * @param {string} type - Message type: 'loading', 'success', or 'error'
 */
function updateStatus(message, isLoading = false, type = 'loading') {
    const statusMessage = document.getElementById('status-message');
    const statusSpinner = document.getElementById('status-spinner');
    const statusBar = document.getElementById('status-bar');

    // Update message text
    statusMessage.textContent = message;

    // Remove all type classes
    statusMessage.classList.remove('loading', 'success', 'error');

    // Add appropriate type class
    if (type) {
        statusMessage.classList.add(type);
    }

    // Show/hide spinner
    if (isLoading) {
        statusSpinner.classList.remove('hidden');
    } else {
        statusSpinner.classList.add('hidden');
    }

    // Show status bar
    statusBar.style.display = 'flex';
}

/**
 * Clear the status bar message and hide it after a delay
 * 
 * @param {number} delayMs - Delay before hiding (default 3000ms)
 */
function clearStatus(delayMs = 3000) {
    setTimeout(() => {
        const statusBar = document.getElementById('status-bar');
        const statusMessage = document.getElementById('status-message');
        const statusSpinner = document.getElementById('status-spinner');

        statusMessage.textContent = '';
        statusSpinner.classList.add('hidden');
        statusBar.style.display = 'none';
    }, delayMs);
}

/**
 * Display an error message to the user
 * 
 * @param {string} message - The error message
 */
function displayError(message) {
    updateStatus(message, false, 'error');
    // Keep error visible longer
    clearStatus(5000);
}

/**
 * Display upload success message with file details
 * 
 * @param {Object} data - Response from /upload endpoint
 * @param {string} data.filename - Name of uploaded file
 * @param {number} data.total_chunks - Number of text chunks created
 */
function displayUploadSuccess(data) {
    const message = `✓ ${data.filename} (${data.total_chunks} chunks processed)`;
    updateStatus(message, false, 'success');
    clearStatus(4000);
}

/**
 * Display question and answer results
 * 
 * @param {Object} data - Response from /ask endpoint
 * @param {string} data.question - The user's question
 * @param {string} data.answer - The AI-generated answer
 * @param {Array<string>} data.retrieved_chunks - Relevant text excerpts
 */
function displayResults(data) {
    // Show results section
    const resultsSection = document.getElementById('results-section');
    resultsSection.classList.remove('hidden');

    // Display question
    const questionDisplay = document.getElementById('question-display');
    questionDisplay.textContent = data.question;

    // Display answer with appropriate font styling
    const answerDisplay = document.getElementById('answer-display');
    answerDisplay.textContent = data.answer;
    answerDisplay.style.fontSize = '1.1rem';
    answerDisplay.style.fontWeight = '500';
    answerDisplay.style.lineHeight = '1.8';

    // Display chunks
    displayChunks(data.retrieved_chunks);

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Display retrieved chunks with proper formatting and labels
 * 
 * @param {Array<string>} chunks - Array of text excerpts
 */
function displayChunks(chunks) {
    const chunksDisplay = document.getElementById('chunks-display');
    
    // Clear previous chunks
    chunksDisplay.innerHTML = '';

    // Add "Source Material:" label via CSS ::before
    // Add each chunk as a distinct section with border and label
    chunks.forEach((chunk, index) => {
        const chunkDiv = document.createElement('div');
        chunkDiv.className = 'chunk';

        // Add chunk number label
        const label = document.createElement('div');
        label.className = 'chunk-label';
        label.textContent = `Source ${index + 1} of ${chunks.length}`;

        // Add chunk text
        const text = document.createElement('div');
        text.textContent = chunk;

        chunkDiv.appendChild(label);
        chunkDiv.appendChild(text);
        chunksDisplay.appendChild(chunkDiv);
    });
}

/**
 * Clear the results display
 */
function clearResults() {
    const resultsSection = document.getElementById('results-section');
    resultsSection.classList.add('hidden');

    document.getElementById('question-display').textContent = '';
    document.getElementById('answer-display').textContent = '';
    document.getElementById('chunks-display').innerHTML = '';
}

/**
 * Disable upload button and prevent multiple submissions
 */
function disableUploadButton() {
    document.getElementById('upload-btn').disabled = true;
}

/**
 * Enable upload button
 */
function enableUploadButton() {
    document.getElementById('upload-btn').disabled = false;
}

/**
 * Disable question form and prevent multiple submissions
 */
function disableQuestionForm() {
    document.getElementById('question-input').disabled = true;
    document.getElementById('ask-btn').disabled = true;
}

/**
 * Enable question form
 */
function enableQuestionForm() {
    document.getElementById('question-input').disabled = false;
    document.getElementById('ask-btn').disabled = false;
}

/**
 * Display document status message
 * Shows message when no documents uploaded, or ready state when documents exist
 * 
 * @param {boolean} hasDocuments - True if documents uploaded, false otherwise
 */
function updateDocumentStatus(hasDocuments) {
    const docStatus = document.getElementById('doc-status');

    if (hasDocuments) {
        docStatus.innerHTML = '<strong>✓ Documents ready for queries</strong>';
        docStatus.className = 'doc-status show ready';
    } else {
        docStatus.innerHTML = '<strong>⚠ Please upload a PDF document first</strong>';
        docStatus.className = 'doc-status show warning';
    }
}

/**
 * Add an uploaded document to the upload history display
 * 
 * @param {string} filename - Name of the uploaded file
 * @param {number} chunks - Number of chunks created
 */
function addUploadedDocToUI(filename, chunks) {
    const uploadHistory = document.getElementById('upload-history');

    const item = document.createElement('div');
    item.className = 'upload-item';

    const nameDiv = document.createElement('div');
    nameDiv.innerHTML = `
        <div class="upload-item-name">📁 ${filename}</div>
        <div class="upload-item-chunks">${chunks} chunks extracted</div>
    `;

    item.appendChild(nameDiv);
    uploadHistory.appendChild(item);
}

/**
 * Clear the upload history display
 */
function clearUploadHistory() {
    document.getElementById('upload-history').innerHTML = '';
}
