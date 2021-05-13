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
  let numFilms = 0;
  const films = JSON.parse(body).results;
  for (let film = 0; film < films.length; film++) {
    for (let chara = 0; chara < films[film].characters.length; chara++) {
      if (films[film].characters[chara].split('/')[5] === '18') {
        numFilms++;
        break;
      }
    }
  }
  console.log(numFilms);
});
