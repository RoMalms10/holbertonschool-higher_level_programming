#!/usr/bin/node
// Print addition of 2 numbers from the command line using a function

function add (a, b) {
  return a + b;
}

const addition = add(parseInt(process.argv[2]), parseInt(process.argv[3]));

console.log(addition);
