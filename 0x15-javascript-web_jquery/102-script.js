window.onload = function () {
  $('#btn_translate:button').click(function () {
    const code = $('#language_code:text').val();
    $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${code}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
};
