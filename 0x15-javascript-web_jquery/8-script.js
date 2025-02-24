$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(movie_data) {
        $('ul#list_movies').append(...movie_data.results.map(movie => `<li>${movie.title}</li>`))
    });
});