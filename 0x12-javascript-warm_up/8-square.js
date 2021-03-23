#!/usr/bin/node
const checkArg = Number(process.argv[2]);
if (Object.is(NaN, checkArg) === true) {
  console.log('Missing size');
} else {
  const num = Math.floor(process.argv[2]);
  for (let row = 0; row < num; row++) {
    for (let colm = 0; colm < num; colm++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
