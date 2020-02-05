#!/usr/bin/node
const arry = process.argv;
const string = "C is fun";
let num = parseInt(arry[2]);
let i = 0;

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < num) {
    console.log(string);
    i++;
  }
}
