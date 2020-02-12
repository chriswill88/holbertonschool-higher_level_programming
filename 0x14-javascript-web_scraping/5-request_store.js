#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request.get(url, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {
    fs.writeFile(filename, body, function (err) {
      if (err) throw err;
    });
  }
});
