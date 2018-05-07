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
    rotate () {
      let holder = this.height;
      this.height = this.width;
      this.width = holder;
    }
    double () {
      this.height = 2 * this.height;
      this.width = 2 * this.width;
    }
  }

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}
module.exports = Rectangle;
module.exports = Square;
