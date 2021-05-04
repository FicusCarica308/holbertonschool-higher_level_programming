#!/usr/bin/node
const request = require('request');
const process = require('process');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const dataDict = JSON.parse(body);
  console.log(dataDict.title);
});
