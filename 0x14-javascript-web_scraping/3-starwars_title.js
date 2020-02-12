#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request.get(`http://swapi.co/api/films/${id}`, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const jsy = JSON.parse(body);
    console.log(jsy.title);
  }
});
