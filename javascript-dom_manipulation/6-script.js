#!/usr/bin/node
// A script that fetch an element name from an URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
	.then(response => {
		if (!response.ok) {
			throw new Error(`HTTP error! Status: ${response.status}`);
		}
		return response.json();
	})
	.then(data => {
		document.getElementById('character').textContent = data.name;
	})
	.catch(error => {
		console.error('Error fetching character:', error);
		document.getElementById('character').textContent = 'Character not found';
	});
