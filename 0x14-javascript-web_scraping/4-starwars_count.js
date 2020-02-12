#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let num = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const jsy = JSON.parse(body);
    // console.log(jsy.results[0].characters);
    for (const i of jsy.results) {
      for (const x of i.characters) {
        // console.log(x);
        if (x.includes('18')) {
          num++;
        }
      }
    }
  }
  console.log(num);
});
