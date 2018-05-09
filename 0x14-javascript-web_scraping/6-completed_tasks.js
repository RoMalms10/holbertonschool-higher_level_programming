#!/usr/bin/node
// Computes number of tasks completed by user id

const request = require('request');

const argv = process.argv.splice(2);

request(argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const newDict = {};
    const jsonList = JSON.parse(body);
    for (let x = 0; x < jsonList.length; x++) {
      let userId = jsonList[x]['userId'].toString();
      if (jsonList[x]['completed'] === true) {
        if (userId in newDict) {
          newDict[userId]++;
        } else {
          newDict[userId] = 1;
        }
      }
    }
    console.log(newDict);
  }
});
