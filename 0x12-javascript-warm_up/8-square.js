#!/usr/bin/node
// Grab a number from the command line then print a square

const times = parseInt(process.argv[2]);
const char = 'X';

if (typeof times === 'number' && isNaN(times) === false) {
  for (let i = 0; i < times; i++) {
    console.log(char.repeat(times)); // string.repeat() will repeat the string based on the number passed
  }
} else {
  console.log('Missing size');
}
