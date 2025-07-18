document.addEventListener('DOMContentLoaded', () => {
	fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
		.then(response => {
			if (!response.ok) {
				throw new Error(`HTTP error! Status: ${response.status}`);
			}
			return response.json();
		})
		.then(data => {
			const helloElement = document.getElementById('hello');
			if (helloElement) {
				helloElement.textContent = data.hello;
			} else {
				console.warn('Element with id "hello" not found.');
			}
		})
		.catch(error => {
			console.error('Error fetching greeting:', error);
		});
	});
