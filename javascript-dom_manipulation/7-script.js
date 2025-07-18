#!/usr/bin/node
// A script that fetch an element name from an URL
document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const listElement = document.getElementById('list_movies');

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const movies = data.results;
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listElement.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error fetching movie data:', error);
    });
});
