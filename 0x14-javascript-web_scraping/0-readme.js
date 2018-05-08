#!/usr/bin/node
// Read file and print contents

const fs = require('fs');

const argv = process.argv.slice(2);

fs.readFile(argv[0], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
