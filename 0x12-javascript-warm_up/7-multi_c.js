#!/usr/bin/node
const checkArg = Number(process.argv[2]);
let i = 0;
if (Object.is(NaN, checkArg) === true) {
  console.log('Missing number of occurrences');
} else {
  const num = Math.floor(process.argv[2]);
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
