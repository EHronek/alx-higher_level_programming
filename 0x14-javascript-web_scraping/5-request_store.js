#!/usr/bin/node
// Gets the contents of a web page and stores it in a file
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Provide url and filepath');
  process.exit(1);
}
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Status code : ${response.statusCode}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
