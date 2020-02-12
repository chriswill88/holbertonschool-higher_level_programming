#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const results = {};
// console.log(url)
request.get(url, function (err, response, body) {
  if (err) {
    // console.error('error:', err);
  } else {
    const jsony = JSON.parse(body);
    for (const i of jsony) {
      const id = i.userId;
      const cp = i.completed;
      // console.log(i.userId, i.completed);
      if (cp) {
        // console.log(typeof(results[id]))
        if (typeof (results[id]) === 'number') {
          results[id] += 1;
        } else {
          results[id] = 1;
        }
      }
    }
    console.log(results);
  }
});
