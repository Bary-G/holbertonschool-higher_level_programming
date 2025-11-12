document.addEventListener("DOMContentLoaded", function () {
    const apiUrl ="https://hellosalut.stefanbohacek.com/?lang=fr"
    const element = document.getElementById("hello");
    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Request fail');
        }
        return response.json();
    })
    .then(data => {
        element.textContent = data.hello;
    });
});
