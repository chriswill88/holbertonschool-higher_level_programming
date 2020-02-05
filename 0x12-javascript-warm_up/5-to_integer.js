#!/usr/bin/node
const arry = process.argv;
let num = 'Not a number';

if (arry[2]) {
  num = parseInt(arry[2]);
}
if (isNaN(num)) {
  num = 'Not a number';
}
console.log(num);
