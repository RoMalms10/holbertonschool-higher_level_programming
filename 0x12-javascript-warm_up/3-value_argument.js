#!/usr/bin/node
// Print the first arguments passed as argv. undefined acts like NULL

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
