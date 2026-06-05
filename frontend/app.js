/**
 * app.js - Application Logic & State Management
 * 
 * This file contains the application state, initialization, event handlers,
 * and orchestration between UI and API layers.
 */

// ============================================
// APPLICATION STATE
// ============================================

/**
 * Central application state object
 * This tracks all relevant data about the current session
 */
const appState = {
    // Document tracking
    uploadedDocs: [],      // Array of {filename, chunks, uploadedAt}
    hasDocuments: false,   // Whether any documents have been uploaded

    // UI states
    isUploading: false,    // True while upload operation in progress
    isQuerying: false,     // True while query operation in progress

    // Current results
    currentQuestion: null,  // The question that was asked
    currentAnswer: null,    // The AI-generated answer
    currentChunks: [],      // The retrieved text chunks

    // Error tracking
    lastError: null        // Most recent error message
};

// ============================================
// INITIALIZATION
// ============================================

/**
 * Initialize the application when DOM is loaded
 * Sets up all event listeners and initial UI state
 */
function initializeApp() {
    console.log('Initializing AI Study Assistant...');


    // File upload events
    const fileInput = document.getElementById('file-input');
    const uploadBtn = document.getElementById('upload-btn');
    const dropArea = document.getElementById('file-drop-area');

    uploadBtn.addEventListener('click', handleUploadButtonClick);
    fileInput.addEventListener('change', handleFileSelect);

    // Drag and drop events
    dropArea.addEventListener('dragover', handleDragOver);
    dropArea.addEventListener('drop', handleDrop);

    // Question form events
    const questionForm = document.getElementById('question-form');
    questionForm.addEventListener('submit', handleQuestionSubmit);

    // Initialize UI state
    updateDocumentStatus(false);
    clearResults();

    console.log('Application initialized successfully');
}

// ============================================
// FILE UPLOAD HANDLERS
// ============================================

/**
 * Handle upload button click - trigger file picker
 */
function handleUploadButtonClick() {
    document.getElementById('file-input').click();
}

/**
 * Handle file selection from input or drag-drop
 * 
 * @param {Event} event - The change or drop event
 */
function handleFileSelect(event) {
    event.preventDefault();

    let files;
    if (event.dataTransfer) {
        // Drag and drop
        files = event.dataTransfer.files;
    } else {
        // File input
        files = event.target.files;
    }

    if (files && files.length > 0) {
        // Process each file
        for (let i = 0; i < files.length; i++) {
            handleUpload(files[i]);
        }

        // Reset file input
        document.getElementById('file-input').value = '';
    }
}

/**
 * Handle drag over event - provide visual feedback
 * 
 * @param {Event} event - The dragover event
 */
function handleDragOver(event) {
    event.preventDefault();
    event.stopPropagation();
    event.currentTarget.style.backgroundColor = '#f0f0ff';
}

/**
 * Handle drop event
 * 
 * @param {Event} event - The drop event
 */
function handleDrop(event) {
    event.preventDefault();
    event.stopPropagation();
    event.currentTarget.style.backgroundColor = '#fafafa';

    handleFileSelect(event);
}

/**
 * Orchestrate the file upload process
 * 
 * @param {File} file - The file to upload
 */
async function handleUpload(file) {


    try {


        const response = await uploadFile(file);

        console.log(response);

        addUploadedDoc(response.filename, response.total_chunks);


        displayUploadSuccess(response);


        updateDocumentStatus(appState.hasDocuments);

    } catch (error) {

        console.log("ERROR BLOCK");
        console.error(error);

    } finally {

        console.log("FINALLY BLOCK");

        appState.isUploading = false;
        enableUploadButton();
    }
}

// ============================================
// STATE MANAGEMENT FUNCTIONS
// ============================================

/**
 * Add an uploaded document to the application state
 * 
 * @param {string} filename - Name of the file
 * @param {number} chunks - Number of chunks created
 */
function addUploadedDoc(filename, chunks) {

    // Keep only the latest document
    appState.uploadedDocs = [];

    // Clear upload history UI
    clearUploadHistory();

    // Add new document
    appState.uploadedDocs.push({
        filename: filename,
        chunks: chunks,
        uploadedAt: new Date()
    });

    // Update UI
    addUploadedDocToUI(filename, chunks);

    // Mark documents available
    setHasDocuments(true);
}

/**
 * Update hasDocuments flag and UI accordingly
 * 
 * @param {boolean} value - True if documents uploaded
 */
function setHasDocuments(value) {
    appState.hasDocuments = value;
    updateDocumentStatus(value);
}

// ============================================
// QUESTION HANDLERS
// ============================================

/**
 * Handle form submission for question
 * 
 * @param {Event} event - The submit event
 */
function handleQuestionSubmit(event) {
    event.preventDefault();
    console.log('Question form submitted');

    const questionInput = document.getElementById('question-input');
    const question = questionInput.value.trim();

    console.log('Question value:', question);
    console.log('Has documents:', appState.hasDocuments);

    // Validate question is not empty
    if (!question) {
        displayError('Please enter a question');
        return;
    }

    // Validate documents are uploaded
    if (!appState.hasDocuments) {
        displayError('Please upload a PDF document first');
        return;
    }

    handleAskQuestion(question);
}

/**
 * Orchestrate the question asking process
 * 
 * @param {string} question - The question to ask
 */
async function handleAskQuestion(question) {
    console.log('handleAskQuestion() called');
    
    // Prevent concurrent queries
    if (appState.isQuerying) {
        console.log('Already querying, preventing concurrent request');
        displayError('Query already in progress');
        return;
    }

    // Update state
    appState.isQuerying = true;
    console.log('Setting isQuerying to true');
    disableQuestionForm();

    try {
        // Show loading status
        updateStatus('Searching...', true, 'loading');

        // Clear previous results
        clearResults();

        // Call API
        console.log('About to call askQuestion API');
        const response = await askQuestion(question);
        console.log('Got response from API');

        // Store results in state
        appState.currentQuestion = response.question;
        appState.currentAnswer = response.answer;
        appState.currentChunks = response.retrieved_chunks;

        // Display results
        displayResults(response);

        // Update status
        updateStatus('✓ Answer generated', false, 'success');
        clearStatus(3000);

    } catch (error) {
        // Handle error
        console.error('Query error:', error);
        appState.lastError = error.message;
        displayError(error.message);

    } finally {
        // Always re-enable form
        appState.isQuerying = false;
        console.log('Setting isQuerying to false');
        enableQuestionForm();

        // Clear input
        document.getElementById('question-input').value = '';
        document.getElementById('question-input').focus();
    }
}

// ============================================
// INITIALIZE ON PAGE LOAD
// ============================================

document.addEventListener('DOMContentLoaded', initializeApp);
