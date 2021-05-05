#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const process = require('process');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) {
      return console.error(err);
    }
  });
});
