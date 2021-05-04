#!/usr/bin/node
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
  console.log('code:', res && res.statusCode);
});
