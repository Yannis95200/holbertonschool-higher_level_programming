document.addEventListener('DOMContentLoaded', function () {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json()) // Convertir la réponse en JSON
        .then(data => {
            let helloText = data.hello; // Récupérer la valeur de "hello"
            let helloElement = document.querySelector('#hello'); // Sélectionner l'élément avec l'ID "hello"
            helloElement.textContent = helloText; // Mettre à jour le texte
        })
        .catch(error => console.error('Error:', error)); // Gérer les erreurs
});
