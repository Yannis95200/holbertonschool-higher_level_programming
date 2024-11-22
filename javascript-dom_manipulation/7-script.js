fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        let movies = data.results;
        let movieList = document.querySelector('#list_movies');
        movies.forEach(movie => {
            let listItem = document.createElement('li');
            listItem.textContent = movie.title;
            movieList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
