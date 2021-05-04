#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let iter = list.length - 1; iter >= 0; iter--) {
    newList.push(list[iter]);
  }
  return (newList);
};
