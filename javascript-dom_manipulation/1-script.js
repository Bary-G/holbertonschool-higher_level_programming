#!/usr/bin/node
// A script that change color of text into red header when clicking
document.addEventListener("DOMContentLoaded", function () {
	const redHeader = document.getElementById("red_header");
	redHeader.addEventListener("click", function () {
		redHeader.style.color = "#FF0000";
	});
});
