document.addEventListener("DOMContentLoaded", function () {
    const header = document.getElementById("update_header");
    header.addEventListener("click", function () {
        header.textContent = "New Header!!!";
    });
})