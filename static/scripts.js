document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("calculator-form");
    const resultDiv = document.getElementById("result");
    const clearButton = document.getElementById("clear-button");

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
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<h2>Result: ${data.result}</h2>`;
        })
        .catch(error => console.error("Error:", error));
    });

    clearButton.addEventListener("click", function() {
        form.reset();
        resultDiv.innerHTML = "";
    });
});
