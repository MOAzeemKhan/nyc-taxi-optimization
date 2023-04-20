const list1Input = document.getElementById("list1");
const costsContainer = document.getElementById("costs-container");

list1Input.addEventListener("input", () => {
	const list1 = list1Input.value.trim();
	if (list1.length === 0) {
		costsContainer.innerHTML = "";
		return;
	}
	const numLocations = list1.split(",").length;
	costsContainer.innerHTML = "";
	for (let i = 1; i <= numLocations; i++) {
		const label = document.createElement("label");
		label.textContent = `Enter Costs for Location ${i} (separated by commas):`;
		const input = document.createElement("input");
		input.type = "text";
		input.name = `costs${i}`;
		input.required = true;
		costsContainer.appendChild(label);
		costsContainer.appendChild(input);
	}
});
