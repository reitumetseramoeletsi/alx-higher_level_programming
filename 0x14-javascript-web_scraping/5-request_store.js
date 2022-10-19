#!/usr/bin/node
// Reads and stores contents of a web page

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
