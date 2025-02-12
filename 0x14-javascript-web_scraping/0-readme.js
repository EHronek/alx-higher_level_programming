#!/usr/bin/node
// reads and prints contents of a file

const fs = require('fs');
const path = process.argv[2];

if (!path) {
  console.error('Please providea file path');
  process.exit(1);
}

fs.readFile(path, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
