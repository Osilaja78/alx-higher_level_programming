#!/usr/bin/node
// Prints the second greatest number in a list.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const intList = process.argv.sort();
  console.log(intList[intList.length - 2]);
}
