
// Animaciones para el init

document.addEventListener("DOMContentLoaded", function () {
    // Function to write text with a blinking cursor
    function typeWriter(text, i, elementId, fnCallback, delay) {
        if (i < text.length) {
            document.getElementById(elementId).innerHTML += text.charAt(i);
            i++;
            setTimeout(function () {
                typeWriter(text, i, elementId, fnCallback, delay);
            }, delay);
        } else if (typeof fnCallback == "function") {
            setTimeout(fnCallback, 200);
        }
    }

    // Main function to initiate typing animation for both titles
    function startTextAnimation() {
        typeWriter("WELCOME TO MY SPACE DISCOVER && ENJOY MY PROFILE", 0, "welcome-title", function () {
            // Execute more code after the first title
            typeWriter("MMORE INFO IN THE FOLLOWING LINKS ;", 1, "sub-text", null, 15);
        }, 45);
    }

    // Start the animation
    startTextAnimation();
});

document.addEventListener("DOMContentLoaded", function () {
    // Function to update loading animation
    function updateLoadingAnimation(elementId, progress) {
        const loadingElement = document.getElementById(elementId);
        const numOfHashes = Math.floor(progress / 10); // Divide by 10 for desired scale
        const hashes = Array(numOfHashes + 1).join("#");
        loadingElement.textContent = hashes;
    }

    // Function to simulate loading animation
    function simulateLoadingAnimation(elementId) {
        let progress = 0;
        setInterval(function () {
            progress = (progress + 1) % 1010; // Increment progress and reset to 0 at 100
            updateLoadingAnimation(elementId, progress);
        }, 100); // Adjust the interval time as needed
    }

    // Start loading animation for each link
    simulateLoadingAnimation("loading-start-here");
    simulateLoadingAnimation("loading-projects");
});