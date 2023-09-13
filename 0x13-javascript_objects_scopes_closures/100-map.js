#!/usr/bin/node
// Computes a new list from a list in ./100-data.js

const list = require('./100-data.js').list;
console.log(list);
const newList = list.map((elem, idx) => elem * idx);
console.log(newList);
