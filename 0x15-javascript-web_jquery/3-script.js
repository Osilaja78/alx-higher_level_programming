const $headerTag = $('header');
const $redHeader = $('div#red_header');

const handleHeaderClick = () => {
  $headerTag.addClass('red');
};

$redHeader.on('click', handleHeaderClick);
