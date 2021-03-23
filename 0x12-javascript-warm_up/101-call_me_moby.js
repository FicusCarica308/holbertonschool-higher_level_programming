#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
  let iter = 0;
  for (iter = 0; iter < x; iter++) {
    theFunction();
  }
};
