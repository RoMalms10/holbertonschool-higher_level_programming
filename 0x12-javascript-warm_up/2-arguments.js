#!/usr/bin/node
/*
Find the length of process.argv by using .length on it. process.argv is
equvalent to argv
*/

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
