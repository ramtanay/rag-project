/**
 * api.js - Backend API Communication Layer
 */

const API_BASE = CONFIG.API_BASE;

function isPDF(file) {
    return (
        file.type === "application/pdf" ||
        file.name.toLowerCase().endsWith(".pdf")
    );
}

async function uploadFile(file) {
    if (!isPDF(file)) {
        throw new Error("Only PDF files are supported");
    }

    const formData = new FormData();
    formData.append("file", file);

    console.log("Uploading file:", file.name);
    console.log("API URL:", `${API_BASE}/upload`);

    try {
        console.log("FETCH START");

        const response = await fetch(`${API_BASE}/upload`, {
            method: "POST",
            body: formData,
        });

        console.log("FETCH FINISHED");

        console.log("Upload status:", response.status);

        if (!response.ok) {
            const errorText = await response.text();

            console.error("Backend Error:");
            console.error(errorText);

            throw new Error(
                `Upload failed (${response.status}): ${errorText}`
            );
        }

        const data = await response.json();

        console.log("Upload successful:");
        console.log(data);

        return data;

    } catch (error) {

        console.error("Upload Exception:");
        console.error(error);

        if (
            error.name === "TypeError" &&
            error.message.includes("fetch")
        ) {
            throw new Error(
                `Cannot connect to backend (${API_BASE})`
            );
        }

        throw error;
    }
}

async function askQuestion(question) {

    if (!question || question.trim() === "") {
        throw new Error("Question cannot be empty");
    }

    const params = new URLSearchParams({
        question: question.trim()
    });

    const url = `${API_BASE}/ask?${params}`;

    console.log("Question:", question);
    console.log("Request URL:", url);

    try {

        const response = await fetch(url, {
            method: "POST"
        });

        console.log("Ask status:", response.status);

        if (!response.ok) {

            const errorText = await response.text();

            console.error("Backend Error:");
            console.error(errorText);

            throw new Error(
                `Query failed (${response.status}): ${errorText}`
            );
        }

        const data = await response.json();

        console.log("Answer received:");
        console.log(data);

        return data;

    } catch (error) {

        console.error("Ask Exception:");
        console.error(error);

        if (
            error.name === "TypeError" &&
            error.message.includes("fetch")
        ) {
            throw new Error(
                `Cannot connect to backend (${API_BASE})`
            );
        }

        throw error;
    }
}