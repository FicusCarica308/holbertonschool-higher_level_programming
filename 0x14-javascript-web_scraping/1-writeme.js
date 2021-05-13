#!/usr/bin/node
const fs = require('fs');
const process = require('process');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }
});
