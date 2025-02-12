#!/usr/bin/node
// Prints the title of star wars moview where the episode
// number matches a given integer

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Provide movie id');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Problem fetching data . Status Code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.error('Error parsing Data:', parseError.message);
    }
  }
});
