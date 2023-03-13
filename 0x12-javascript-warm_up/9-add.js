#!/usr/bin/node
// Prints the addition of two integers

function add (a, b) {
  return a + b;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
