#!/usr/bin/node
// A class Square that inherits from class Rectangle

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
