#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0) w = '';
    if (h <= 0) h = '';
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
