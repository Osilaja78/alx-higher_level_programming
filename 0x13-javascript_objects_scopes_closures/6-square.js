#!/usr/bin/node
// A class Square with an instance method

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
