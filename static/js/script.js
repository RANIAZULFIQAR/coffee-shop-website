function scrollToMenu() {
    document.getElementById("menu").scrollIntoView({ behavior: "smooth" }); 
    // A missing semicolon on the line above often causes this error.
}