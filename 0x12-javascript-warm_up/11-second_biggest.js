#!/usr/bin/node
let first = 0;
let second = 0;
process.argv.sort();
for (let iter = 2; iter < process.argv.length; iter++) {
  const num = Math.floor(process.argv[iter]);
  if (num > first) {
    second = first;
    first = num;
  }
}
console.log(second);
