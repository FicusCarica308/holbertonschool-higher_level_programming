#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (let iter = 0; iter < list.length; iter++) {
    if (searchElement === list[iter]) {
      occur++;
    }
  }
  return (occur);
};
