const $headerTag = $('header');
const $redHeader = $('div#red_header');

const handleHeaderClick = () => {
  $headerTag.css('color', '#FF0000');
};

$redHeader.on('click', handleHeaderClick);
