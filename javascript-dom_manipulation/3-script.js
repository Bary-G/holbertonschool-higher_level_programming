document.addEventListener("DOMContentLoaded", function () {
    const header = document.getElementById("toggle_header");
    header.classList.add("red");
    header.addEventListener("click", function () {
        if (header.classList.contains("red")) {
            header.classList.remove("red");
            header.classList.add("green");
        } else {
            header.classList.remove("green");
            header.classList.add("red");
        }
    });
})