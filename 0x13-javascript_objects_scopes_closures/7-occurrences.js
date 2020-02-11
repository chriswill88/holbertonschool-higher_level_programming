#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (const i of list) {
    // console.log("list->", i, "search-->", searchElement);
    if (i === searchElement) {
      occurence++;
    }
  }
  return occurence;
};
