#!/usr/bin/node
// Save contents of a web page into a file

const request = require('request');
const fs = require('fs');

const argv = process.argv.splice(2);

const url = argv[0];
const file = argv[1];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
