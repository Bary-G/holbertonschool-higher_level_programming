#!/usr/bin/node
// A script that adds a li element to a list when the user clicks on the element with id add_item
document.addEventListener("DOMContentLoaded", function() {
	const addItemButton = document.getElementById("add_item");
	const list = document.querySelector("ul.my_list");

	addItemButton.addEventListener("click", function() {
		const newListItem = document.createElement("li");
		newListItem.textContent = "Item";
		list.appendChild(newListItem);
	});
});
