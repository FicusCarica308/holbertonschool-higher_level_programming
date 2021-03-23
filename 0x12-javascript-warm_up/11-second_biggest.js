#!/usr/bin/node
let first = 0;
let second = 0;
for (let iter = 2; iter < process.argv.length; iter++) {
  const num = Number(process.argv[iter]);
  if (num > first) {
    second = first;
    first = num;
  }
}
console.log(String(second));
