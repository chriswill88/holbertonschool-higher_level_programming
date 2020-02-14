$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  const list = [];
  $.each(data.results, function (key, val) {
    list.push("<li id='" + key + "'>" + val.title + '</li>');
  });

  $('<ul/>', {
    html: list.join('')
  }).appendTo('#list_movies');
  //   for (i of results) {
  //     $('#list_movies').add('li').text(i.title)
  //   }
});
