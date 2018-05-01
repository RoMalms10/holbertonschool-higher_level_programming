#!/usr/bin/node
// Print factorial of a number from the command line using a function

function factorial (a) {
  if (a < 2) return 1;
  return (a * factorial(a - 1));
}

const number = parseInt(process.argv[2]);
if (isNaN(number) === false) {
  const result = factorial(number);
  console.log(result);
} else {
  console.log(1);
}
