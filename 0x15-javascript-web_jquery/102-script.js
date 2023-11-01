$(document).ready(function () {
    const $helloDiv = $('div#hello');

    $("input#btn_translate").click(function () { 
      var lang = $("input#language_code").val();
      const dataUrl = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

      $.get(dataUrl, function(data) {
        const res = data.hello;
        $helloDiv.text(res);
      });
    });
  });
  