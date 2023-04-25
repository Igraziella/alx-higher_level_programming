#!/usr/bin/node
// A script that writes a string to a file.

const fs = require('fs');
const content = process.argv[2];
const string = process.argv[3];

fs.writeFile(content, string, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
