#!/usr/bin/node
// Star wars API call

const request = require('request');

const argv = process.argv.slice(2);

const url = 'http://swapi.co/api/films/' + argv[0];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonDict = JSON.parse(body);
    console.log(jsonDict['title']);
  }
});
