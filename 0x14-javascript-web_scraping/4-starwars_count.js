#!/usr/bin/node
// Prints the number of movies where the character "Wedge Antilles"
// is present

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Provide Api URL as argument');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Status code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      let count = 0;
      movieData.results.forEach((movie) => {
        if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      });

      // Print the count of movies where Wedge Antilles is present
      console.log(count);
    } catch (parseError) {
      // Handle JSON parsing errors
      console.error('Error parsing response:', parseError.message);
    }
  }
});
