window.onload = function () {
  $('#add_item').click(function () {
    $('ul').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('li:first').remove();
  });

  $('#clear_list').click(function () {
    $('li').remove();
  });
};
