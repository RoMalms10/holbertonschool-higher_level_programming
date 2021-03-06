#!/usr/bin/node
// Check how many times a person appeared in a movie

const request = require('request');

const argv = process.argv.slice(2);

const person1 = 'https://swapi.co/api/people/18/';
const person2 = 'http://swapi.co/api/people/18/';

request(argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const jsonDict = JSON.parse(body);
    const listMovies = jsonDict['results'];
    for (let i = 0; i < listMovies.length; i++) {
      if (listMovies[i]['characters'].includes(person1) || listMovies[i]['characters'].includes(person2)) count++;
    }
    console.log(count);
  }
});
