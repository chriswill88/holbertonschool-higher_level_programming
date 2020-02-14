function getlang (event) {
  const code = $('#language_code:text').val();
  $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${code}`, function (data) {
    $('#hello').text(data.hello);
  });
}

window.onload = function () {
  $('#btn_translate:button').click(getlang);

  $('#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13) {
      getlang();
    }
  });
};
