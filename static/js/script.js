document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("fileInput");
    const fileNameDisplay = document.getElementById("fileName");
    const uploadBtn = document.getElementById("uploadBtn");
    const form = document.getElementById("uploadForm");
    const loading = document.getElementById("loading");
    const resultContainer = document.querySelector(".result");
    const uploadedImage = document.querySelector(".result img");

    // Function to reset form **ONLY if there are no results**
    function resetForm() {
        if (!resultContainer || resultContainer.innerHTML.trim() === "") {
            form.reset(); // Reset form elements only if no result exists
            fileNameDisplay.textContent = "No file chosen";
            uploadBtn.disabled = true;
            uploadBtn.textContent = "Upload & Predict";
            loading.classList.add("hidden");
            if (uploadedImage) uploadedImage.src = "";
        }
    }

    // Ensure form resets only on full page reload (not after form submit)
    if (!sessionStorage.getItem("formSubmitted")) {
        window.addEventListener("load", resetForm);
    }

    // Mark that the form was submitted to prevent reset
    form.addEventListener("submit", function () {
        sessionStorage.setItem("formSubmitted", "true"); // Store form submission flag
        loading.classList.remove("hidden");
        uploadBtn.textContent = "Processing...";
        uploadBtn.disabled = true;
    });

    // Update file name display when a file is selected
    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = fileInput.files[0].name;
            uploadBtn.disabled = false;
        } else {
            fileNameDisplay.textContent = "No file chosen";
            uploadBtn.disabled = true;
        }
    });

    // Clear sessionStorage when the user navigates away
    window.addEventListener("beforeunload", function () {
        sessionStorage.removeItem("formSubmitted");
    });
});
