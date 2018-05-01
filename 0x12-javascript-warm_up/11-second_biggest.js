#!/usr/bin/node
// Print factorial of a number from the command line using a function

if (process.argv.length < 4) {
  console.log(0);
} else {
  let highest = -Infinity;
  let secondhighest = -Infinity;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > highest) {
      secondhighest = highest;
      highest = process.argv[i];
    } else if (highest > process.argv[i] && process.argv[i] > secondhighest) {
      secondhighest = process.argv[i];
    }
  }
  console.log(secondhighest);
}
