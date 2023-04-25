#!/usr/bin/node
// Displays the status code of a GET request.

const request = require('request');
const URL = process.argv[2];

get.request(URL, function (response, err) {
  if ('code: ' + response.statuscode) {
    console.log(response);
  } else {
    console.log(err);
  }
});
