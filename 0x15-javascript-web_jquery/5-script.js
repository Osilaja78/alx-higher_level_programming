const $listTag = $('ul.my_list');
const $addItemDiv = $('div#add_item');

const handleAddItemClick = () => {
  $listTag.append('<li>Item</li>');
};

$addItemDiv.on('click', handleAddItemClick);
