document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("madlib-form");
    form.addEventListener("submit", function (event) {
        if (!validateForm()) {
            event.preventDefault();
        }
    });
});


function showSnackbar(message) {
	const snackbar = document.getElementById("snackbar");
	snackbar.innerText = message;
	snackbar.classList.remove("hidden");
	snackbar.classList.add("show"); 
	setTimeout(() => {
		snackbar.classList.remove("show"); 
		snackbar.classList.add("hidden");
	}, 4000);
}

function validateForm() {
	const inputs = document.getElementsByTagName("input");
	let isValid = true;

	function containsInteger(value) {
		return /\d/.test(value);
	}

	for (let input of inputs) {
		if (input.value.trim().length < 3 || containsInteger(input.value)) {
			isValid = false;
			input.classList.add("invalid");
		} else {
			input.classList.remove("invalid");
		}
	}

	// This block should be inside the validateForm function
	if (!isValid) {
		showSnackbar(
			"Please enter at least 3 characters for all fields and avoid using numbers."
		);
	}

	return isValid;
}




function convertInputsToLowerCase() {
	const inputs = document.getElementsByTagName("input");
	for (let input of inputs) {
		input.value = input.value.toLowerCase();
	}
}
