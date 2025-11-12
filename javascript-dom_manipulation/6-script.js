document.addEventListener("DOMContentLoaded", function () {
    const apiUrl ="https://swapi-api.hbtn.io/api/people/5/?format=json"
    const textBox = document.getElementById("character");
    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Request fail');
        }
        return response.json();
    })
    .then(data => {
        textBox.textContent = data.name;
    });
});
