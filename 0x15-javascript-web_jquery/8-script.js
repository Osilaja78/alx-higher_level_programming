const $moviesListDiv = $('ul#list_movies');
const dataUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(dataUrl, function(data) {
  const res = data.results;

  for (i = 0; i < res.length; i++) {
    const title = res[i].title;
    console.log(title);
    $moviesListDiv.append(`<li>${title}</li>`);
  };
});
