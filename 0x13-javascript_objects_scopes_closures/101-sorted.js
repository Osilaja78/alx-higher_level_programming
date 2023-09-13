#!/usr/bin/node
// computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data.js');

const occurrencesDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!(occurrences in occurrencesDict)) {
    occurrencesDict[occurrences] = [];
  }

  occurrencesDict[occurrences].push(userId.toString());
}

console.log(occurrencesDict);
