function sendQuery() {
    const query = document.getElementById('query').value;
    fetch(`http://127.0.0.1:8000/query?query=${query}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('response').innerText = 'An error occurred. Please try again.';
        });
}
