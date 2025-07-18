#!/usr/bin/node
// A script that adds the class red to the header element when the user clicks on the tag with id red_header
document.getElementById("update_header").addEventListener("click", function () {
	const header = document.querySelector("header");
	header.textContent = "New Header!!!";
});
