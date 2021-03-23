#!/usr/bin/node
let first = 0;
let second = 0;
for (let iter = 3; iter < process.argv.length; iter++) {
  const num = Math.floor(process.argv[iter]);
  if (num > first) {
    second = first;
    first = num;
  }
}
console.log(second);
