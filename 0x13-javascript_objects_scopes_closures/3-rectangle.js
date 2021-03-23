#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let colum = 0; colum < this.width; colum++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
};
