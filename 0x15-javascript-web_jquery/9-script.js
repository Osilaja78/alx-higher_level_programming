$(document).ready(function () {
  const $helloDiv = $('div#hello');
  const dataUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(dataUrl, function(data) {
    const res = data.hello;
    $helloDiv.text(res);
  });
});
