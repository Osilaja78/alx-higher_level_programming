#!/usr/bin/node
// Concatenates two files into one.

const fs = require('fs');

const fileOne = process.argv[2];
const fileTwo = process.argv[3];
const destFile = process.argv[4];

try {
  const firstContent = fs.readFileSync(fileOne, 'utf-8');
  const secondContent = fs.readFileSync(fileTwo, 'utf-8');
  fs.writeFileSync(destFile, firstContent + secondContent);
} catch (error) {
  console.log(error);
}
