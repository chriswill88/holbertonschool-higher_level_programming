#!/usr/bin/node

const dict = require('./101-data.js').dict;
const retDict = {};
const prev = [];

for (const key in dict) {
  if (prev.indexOf(dict[key])) {
    retDict[dict[key]] = [];
    for (const k in dict) {
      // console.log("k -->", k, "key--->", key)
      if (dict[k] === dict[key]) {
        // console.log("k[", i, "] ----> ", k);
        retDict[dict[k]].push(k);
        // list.push(k);
        // console.log(dict[key], list)
      }
    }
  }
  prev.push(key);
  // console.log(retDict)
}

console.log(retDict);
