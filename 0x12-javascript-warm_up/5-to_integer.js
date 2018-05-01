#!/usr/bin/node
// Converts argument to a number, if it can't convert, it prints 'Not a number'

var myInt = parseInt(process.argv[2]);

if (typeof myInt === 'number' && isNaN(myInt) === false) {
  console.log('My number: ' + myInt);
} else {
  console.log('Not a number');
}
