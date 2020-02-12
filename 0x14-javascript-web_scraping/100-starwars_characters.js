#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request.get(`http://swapi.co/api/films/${id}`, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const jsy = JSON.parse(body);
    const names = jsy.characters;
    for (const i of names) {
      // console.log(i);
      request.get(i, function (err, response, body) {
        if (err) {
          console.error('error:', err);
        } else {
          const jsony = JSON.parse(body);
          console.log(jsony.name);
        }
      });
    }
  }
});
