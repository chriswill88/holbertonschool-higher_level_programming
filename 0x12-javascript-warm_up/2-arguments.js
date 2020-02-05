#!/usr/bin/node

const num = process.argv.length - 2;
/* console.log(num)
 * use === instead of == for conditionals
 */
if (num < 1) {
  console.log('No argument');
} else if (num === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
