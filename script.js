async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const responseDiv = document.getElementById('response');

    const res = await fetch('/api/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await res.json();
    responseDiv.innerText = data.response;
}
