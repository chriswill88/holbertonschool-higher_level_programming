#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
request.get(arg, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
