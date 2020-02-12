#!/usr/bin/node
const fs = require('fs');
const src1 = process.argv[2];
const string = process.argv[3];
// const dest = process.argv[4];

// console.log(src1);
fs.writeFile(src1, string, function (err) {
  if (err) throw err;
});
