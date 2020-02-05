#!/usr/bin/node
const arry = process.argv;
const num = parseInt(arry[2]);
let i = 0;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
}
