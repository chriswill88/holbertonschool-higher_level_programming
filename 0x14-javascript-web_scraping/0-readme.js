#!/usr/bin/node
const fs = require('fs');
const src1 = process.argv[2];
// const src2 = process.argv[3];
// const dest = process.argv[4];

// console.log(src1);
fs.readFile(src1, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
