function toggleDarkMode() {
    const body = document.body;
    const catOutline = document.getElementById("catOutline");

    body.classList.toggle("dark-mode");

    const isDarkMode = body.classList.contains("dark-mode");
    catOutline.src = isDarkMode ? "cat-white-outline.png" : "cat-black-outline.png";
}

function sendPrompt() {
    const userInput = document.getElementById("userPrompt").value.toLowerCase();
    const chatHistory = document.getElementById("chatHistory");

    chatHistory.innerHTML += `<div class="user-message">${userInput}</div>`;

    document.getElementById("userPrompt").value = "";

    // the emotions logic and actual gifs will get implemented here but for now this is an example of how it will work for visual purposes 
    const placeholderCatGif = '<img src="placeholder-cat.gif" alt="Cat Response">';
    chatHistory.innerHTML += `<div class="cat-response">${placeholderCatGif}</div>`;
}
