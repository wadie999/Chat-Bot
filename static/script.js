function sendQuery() {
    const query = document.getElementById('queryInput').value;
    fetch(`http://127.0.0.1:8000/query?query=${query}`)
        .then(response => response.json())
        .then(data => showResponse(data.response)) // Here you pass the response directly, which is a string
        .catch(error => console.error('An error occurred:', error));
}

function showResponse(response) {
    const responseDiv = document.getElementById('responseDiv');
    responseDiv.textContent = response.result  ; // Set the text content to the response string
}
