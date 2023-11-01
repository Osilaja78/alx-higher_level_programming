const $headerTag = $('header');
const $updateHeaderDiv = $('div#update_header');

const handleUpdateClick = () => {
  $headerTag.text('New Header!!!');
};

$updateHeaderDiv.on('click', handleUpdateClick);