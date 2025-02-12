#!/usr/bin/node
// Script prints all characters of a star wars movie
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('provide the Movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Status code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);

      const characterUrls = movieData.characters;

      const fetchCharacterNamesSequentially = (urls) => {
        let index = 0;

        const fetchNextCharacter = () => {
          if (index >= urls.length) {
            return;
          }

          const characterUrl = urls[index];
          request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              console.error(charError);
            } else if (charResponse.statusCode !== 200) {
              console.error(`Error: Unable to fetch character data. Status code: ${charResponse.statusCode}`);
            } else {
              try {
                const characterData = JSON.parse(charBody);

                console.log(characterData.name);
              } catch (parseError) {
                console.error('Error parsing character response:', parseError.message);
              }
            }

            index++;
            fetchNextCharacter();
          });
        };

        fetchNextCharacter();
      };

      fetchCharacterNamesSequentially(characterUrls);
    } catch (parseError) {
      console.error('Error parsing movie response:', parseError.message);
    }
  }
});
