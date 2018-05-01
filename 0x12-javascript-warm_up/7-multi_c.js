#!/usr/bin/node
// Create and array of string and print them in a loop

const times = parseInt(process.argv[2]);

if (typeof times === 'number' && isNaN(times) === false) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
