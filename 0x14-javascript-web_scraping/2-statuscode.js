#!/usr/bin/node
// Displays the satus code of a GET request

const args = process.argv;
const request = require('request');
request(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else console.log('code:', response && response.statusCode);
});
