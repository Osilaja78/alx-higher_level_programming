#!/usr/bin/node
// This function  prints the number of arguments
// already printed and the new argument value.

let numArg = 0;

exports.logMe = function (item) {
  console.log(`${numArg++}: ${item}`);
};
