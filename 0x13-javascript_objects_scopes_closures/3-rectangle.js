#!/usr/bin/node
// Write class Rectangle with width and height

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    const str1 = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(str1.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
