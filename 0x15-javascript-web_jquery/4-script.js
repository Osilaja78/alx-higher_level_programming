const $headerTag = $('header');
const $toggleHeader = $('div#toggle_header');

const handleHeaderClick = () => {
  const current = $headerTag.attr('class');

  if (current === 'green') {
    $headerTag.toggleClass(`${current} red`);
  }

  if (current === 'red') {
    $headerTag.toggleClass(`${current} green`);
  }
};

$toggleHeader.on('click', handleHeaderClick);
