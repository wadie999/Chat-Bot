function sendQuery() {
    const query = document.getElementById('queryInput').value;
    showQuery(query);
    document.getElementById('queryInput').value = ""; // Clear the input

    // Add typing indicator
    const typingIndicator = document.createElement('div');
    typingIndicator.className = "typingIndicator";
    typingIndicator.textContent = '.';
    responseDiv.appendChild(typingIndicator);
    // Add interval to update the text content
    const typingInterval = setInterval(() => {
        typingIndicator.textContent += '.';
        if (typingIndicator.textContent.length > 3) typingIndicator.textContent = '.';
    }, 500)
    
    fetch(`http://127.0.0.1:8000/query?query=${query}`)
        .then(response => response.json())
        .then(data => {
            console.log("Data:", data);
            // Remove typing indicator
           // Remove typing indicator
            clearInterval(typingInterval);
            responseDiv.removeChild(typingIndicator);

            showResponse(data.response)}) // Here you pass the response directly, which is a string
        .catch(error => console.error('An error occurred:', error));
}

function showQuery(query) {
    const responseDiv = document.getElementById('responseDiv');
    const queryDiv = document.createElement('div');
    queryDiv.className = 'userMessage';
    queryDiv.textContent = query;
    responseDiv.appendChild(queryDiv);
    responseDiv.scrollTop = responseDiv.scrollHeight;
  }

function showResponse(response) {
    const responseDiv = document.getElementById('responseDiv');
    const responseDivMessage = document.createElement('div');
    responseDivMessage.className = 'botMessage';
    responseDivMessage.textContent = response.result;
    responseDiv.appendChild(responseDivMessage);

    // Add follow-up message
    const followUpDiv = document.createElement('div');
    followUpDiv.className = "botMessage";
    followUpDiv.textContent = "I hope I answered your question. Do you need any more help?";
    responseDiv.appendChild(followUpDiv);

    responseDiv.scrollTop = responseDiv.scrollHeight; // Scroll to bottom
}
