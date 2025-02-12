#!/usr/bin/node
// Script writes a string to a file

const fs = require('fs');

const path = process.argv[2];
const dataString = process.argv[3];

if (!path) {
  console.error('Provide a file path as second argument');
  process.exit(1);
}
fs.writeFile(path, dataString, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
