#!/usr/bin/node
const arry = process.argv;

if (!arry[2]) {
  console.log('No argument');
} else {
  console.log(arry[2]);
}
