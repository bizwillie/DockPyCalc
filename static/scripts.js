document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("calculator-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const num1 = formData.get("num1");
        const num2 = formData.get("num2");
        const operation = formData.get("operation");

        fetch("/", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            resultDiv.innerHTML = data;
        })
        .catch(error => console.error("Error:", error));
    });
});
