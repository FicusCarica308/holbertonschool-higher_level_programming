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
    if (data.completed === true) {
      if (data.userId in outputDict === false) { outputDict[data.userId] = 0; }
      outputDict[data.userId] += 1;
    }
  }
  console.log(outputDict);
});
