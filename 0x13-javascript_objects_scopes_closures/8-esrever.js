#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const array = [];
  while (len-- > 0) {
    array.push(list[len]);
  }
  return array;
};
