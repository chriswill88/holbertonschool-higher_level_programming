#!/usr/bin/node
const arry = process.argv;
let two;
let one = two = 'undefined';

if (arry[2]) {
  one = arry[2];
}
if (arry[3]) {
  two = arry[3];
}
console.log((one) + ' is ' + (two));
