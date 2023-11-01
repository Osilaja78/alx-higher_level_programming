const $characterDiv = $('div#character');
const dataUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(dataUrl, function(data) {
  $characterDiv.text("Character Name: " + data.name);
});
