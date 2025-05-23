document.getElementById('theme-toggle').addEventListener('click', async () => {
    const response = await fetch('/toggle-theme/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json'
        }
    });
    
    if (response.ok) {
        document.body.classList.toggle('dark-mode');
        document.body.classList.toggle('light-mode');
    }
});