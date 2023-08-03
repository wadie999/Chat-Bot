function sendQuery() {
    const query = document.getElementById('queryInput').value;
    showQuery(query);
    fetch(`http://127.0.0.1:8000/query?query=${query}`)
        .then(response => response.json())
        .then(data => showResponse(data.response)) // Here you pass the response directly, which is a string
        .catch(error => console.error('An error occurred:', error));
}

function showQuery(query) {
    const responseDiv = document.getElementById('responseDiv');
    const queryBubble = document.createElement('div');
    queryBubble.className = 'queryBubble';
    queryBubble.textContent = `You: ${query}`;
    responseDiv.appendChild(queryBubble);
  }

function showResponse(response) {
    const responseDiv = document.getElementById('responseDiv');
    const responseBubble = document.createElement('div');
    responseBubble.className = 'responseBubble';
    responseBubble.textContent = `Bot: ${response.result}`;
    responseDiv.appendChild(responseBubble);
}
