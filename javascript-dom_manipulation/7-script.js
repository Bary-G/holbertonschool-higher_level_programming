document.addEventListener("DOMContentLoaded", function () {
    const apiUrl ="https://swapi-api.hbtn.io/api/films/?format=json"
    const list = document.getElementById("list_movies");
    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Request fail');
        }
        return response.json();
    })
    .then(data => {
        data.results.forEach(movies => {
            const newItem = document.createElement("li");
            newItem.textContent = movies.title;
            list.appendChild(newItem);
        })
    });
});
