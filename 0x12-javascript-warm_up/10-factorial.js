#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (num) {
  let sum = 1;

  while (num > 0) {
    sum *= num;
    num--;
  }
  return sum;
}

console.log(factorial(num));
