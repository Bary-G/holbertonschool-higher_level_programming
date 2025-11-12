document.addEventListener("DOMContentLoaded", function () {
    const header = document.getElementById("red_header");
    header.addEventListener("click", function () {
        header.classList.add("red");
    });
})