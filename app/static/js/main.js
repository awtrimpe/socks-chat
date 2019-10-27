function menu() {
    let hamburger = document.getElementById("hamburger");
    let sideMenu = document.getElementById("side-menu");
    if (hamburger.classList.contains("hamburger-clicked")) {
        hamburger.classList.remove("hamburger-clicked");
        sideMenu.classList.remove("show");
    } else {
        hamburger.classList.add("hamburger-clicked");
        sideMenu.classList.add("show");
    }
}

window.onload = window.addEventListener('mouseup', function (event) {
    let hamburger = document.getElementById("hamburger");
    let side_menu = document.getElementById('side-menu');
    if (!side_menu.contains(event.target) && !hamburger.contains(event.target)) {
        hamburger.classList.remove("hamburger-clicked");
        side_menu.classList.remove("show");
    }
});