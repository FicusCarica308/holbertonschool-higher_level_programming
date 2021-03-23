#!/usr/bin/node
const checkArg = Number(process.argv[2]);
if (Object.is(NaN, checkArg) === true) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(process.argv[2]));
}
