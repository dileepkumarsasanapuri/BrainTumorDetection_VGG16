document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("fileInput");
    const fileNameDisplay = document.getElementById("fileName");
    const uploadBtn = document.getElementById("uploadBtn");
    const form = document.getElementById("uploadForm");
    const loading = document.getElementById("loading");
    const resultContainer = document.querySelector(".result");
    const uploadedImage = document.querySelector(".result img");


    function resetForm() {
        if (!resultContainer || resultContainer.innerHTML.trim() === "") {
            form.reset(); 
            fileNameDisplay.textContent = "No file chosen";
            uploadBtn.disabled = true;
            uploadBtn.textContent = "Upload & Predict";
            loading.classList.add("hidden");
            if (uploadedImage) uploadedImage.src = "";
        }
    }


    if (!sessionStorage.getItem("formSubmitted")) {
        window.addEventListener("load", resetForm);
    }

  
    form.addEventListener("submit", function () {
        sessionStorage.setItem("formSubmitted", "true"); 
        loading.classList.remove("hidden");
        uploadBtn.textContent = "Processing...";
        uploadBtn.disabled = true;
    });

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = fileInput.files[0].name;
            uploadBtn.disabled = false;
        } else {
            fileNameDisplay.textContent = "No file chosen";
            uploadBtn.disabled = true;
        }
    });

    window.addEventListener("beforeunload", function () {
        sessionStorage.removeItem("formSubmitted");
    });
});
