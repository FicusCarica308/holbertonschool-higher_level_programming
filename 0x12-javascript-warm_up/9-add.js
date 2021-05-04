#!/usr/bin/node
function add (a, b) {
  const num = Number(a) + Number(b);
  console.log(num);
}
add(process.argv[2], process.argv[3]);
