// darkmode.js

function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle("dark-mode");
}

// Guardar el modo actual en localStorage o en una cookie para recordar la preferencia del usuario
function saveModePreference() {
    const body = document.body;
    if (body.classList.contains("dark-mode")) {
        localStorage.setItem("mode", "dark");
    } else {
        localStorage.setItem("mode", "light");
    }
}

// Cargar la preferencia del modo almacenada por el usuario
function loadModePreference() {
    const mode = localStorage.getItem("mode");
    if (mode === "dark") {
        document.body.classList.add("dark-mode");
    }
}

// Evento para cambiar entre los modos
const modeButton = document.getElementById("mode-button");
modeButton.addEventListener("click", () => {
    toggleDarkMode();
    saveModePreference();
});

// Cargar la preferencia del usuario cuando se carga la página
window.addEventListener("load", () => {
    loadModePreference();
});
