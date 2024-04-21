#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0) w = undefined;
    if (h <= 0) h = undefined;
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
