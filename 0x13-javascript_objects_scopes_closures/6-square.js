#!/usr/bin/node
const SQ1 = require('./5-square');
module.exports = class Square extends SQ1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      for (let colum = 0; colum < this.width; colum++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
};
