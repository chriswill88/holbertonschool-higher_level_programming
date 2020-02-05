#!/usr/bin/node

const arry = process.argv;
const len = process.argv.length - 2;
let num = 0;
let n = 0;
let i;
let x;

if (len < 2) {
  console.log(n);
} else {
  for (x of arry) {
    if (parseInt(x) > num) {
      num = parseInt(x);
    }
  }
  // console.log(num)
  for (i of arry) {
    if (i > n && i < num) {
      // console.log("a --> " + i);
      n = parseInt(i);
    }
  }
  console.log(n);
}
