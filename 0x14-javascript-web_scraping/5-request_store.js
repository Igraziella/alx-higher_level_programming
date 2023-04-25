#!/usr/bin/node
// A script that gets the content of a page and stores it in a file.

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const filePath = process.argv[3];

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8');
  }
});
