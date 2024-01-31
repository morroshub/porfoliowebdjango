

document.addEventListener("DOMContentLoaded", function () {
    // Function to write text with a blinking cursor
    function typeWriter(text, i, fnCallback) {
        if (i < text.length) {
            document.getElementById("welcome-title").innerHTML += text.charAt(i);
            i++;
            setTimeout(function () {
                typeWriter(text, i, fnCallback)
            }, 800);
        } else if (typeof fnCallback == "function") {
            setTimeout(fnCallback, 700);
        }
    }

    // Main function to initiate typing animation
    function startTextAnimation(i) {
        if (typeof dataText[i] == "undefined") {
            setTimeout(function () {
                startTextAnimation(0);
            }, 20000); // Delay before starting over
        }
        if (i < dataText[i].length) {
            typeWriter(dataText[i], 0, function () {
                startTextAnimation(i + 1);
            });
        }
    }

    // Array containing the terminal art strings
    var dataText = ["WELCOME - DISCOVER MY PROFILE"];
    startTextAnimation(0);

    // Other animations or functionalities can be added here
});



function startLoadingAnimation() {
    var loadingElement = document.querySelector('.loading-animation');
    loadingElement.innerHTML = '##########'; // Initial loading animation
}
