#!/usr/bin/env
// prints x times “C is fun”

const langStr = 'C is fun';
console.log(langStr);

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(langStr);
  }
}
