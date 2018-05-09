#!/usr/bin/node

const request = require('request');

const argv = process.argv.slice(2);

request(argv[0], function(err, res, body) {
    if (err) {
        console.log(err);
    } else {
      console.log('code:', res.statusCode);
    }
});
