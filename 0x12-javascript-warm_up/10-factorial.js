#!/usr/bin/node
// Prints the factorial of a number

function factorial (n) {
  if (isNaN(n) || (parseInt(n) === 1)) {
    return 1;
  } else {
    return parseInt(n) * factorial(parseInt(n) - 1);
  }
}

console.log(factorial(process.argv[2]));
