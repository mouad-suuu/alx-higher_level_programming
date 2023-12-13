#!/usr/bin/node
const data = require('./101-data').dict;

const reversedData = {};

for (const userId in data) {
  const occurrence = data[userId];

  if (occurrence in reversedData) {
    reversedData[occurrence].push(userId);
  } else {
    reversedData[occurrence] = [userId];
  }
}

console.log(reversedData);
