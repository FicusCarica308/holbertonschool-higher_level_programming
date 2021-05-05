#!/usr/bin/node
const request = require('request');
const outputDict = {};
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const dataDict = JSON.parse(body);
  for (const data of dataDict) {
    if (data.userId in outputDict === false) { outputDict[data.userId] = 0; }
    if (data.completed === true) {
      outputDict[data.userId] += 1;
    }
  }
  console.log(outputDict);
});
