#!/usr/bin/node
var functioncalls = 0;

exports.logMe = function (item) {
  console.log(`${functioncalls}: ${item}`);
  functioncalls += 1;
};
