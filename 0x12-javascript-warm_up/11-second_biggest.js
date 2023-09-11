#!/usr/bin/node
// Prints the second greatest number in a list of args

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list[list.length - 2]);
}
