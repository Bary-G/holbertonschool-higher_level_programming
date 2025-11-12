document.addEventListener("DOMContentLoaded", function () {
    const itemButton = document.getElementById("add_item");
    const list = document.getElementById("my_list");
    itemButton.addEventListener("click", function () {
        const newItem = document.createElement("li");
        newItem.classList.add("my_list");
        newItem.textContent = "Item";
        list.appendChild(newItem);
    });
})