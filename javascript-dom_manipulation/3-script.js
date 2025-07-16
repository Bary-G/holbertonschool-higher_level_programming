#!/usr/bin/node
// A script that adds the class red to the header element when the user clicks on the tag with id red_header
document.getElementById("toggle_header").addEventListener("click", function () {
	const header = document.querySelector("header");

	if (header.classList.contains("red")) {
		header.classList.remove("red");
		header.classList.add("green");
	} else {
		header.classList.remove("green");
		header.classList.add("red");
	}
});
