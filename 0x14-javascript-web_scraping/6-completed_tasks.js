#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Enter url as argument');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Status code: ${response.statusCode}`);
  } else {
    try {
      const taskData = JSON.parse(body);

      const completedByUser = {};

      taskData.forEach((task) => {
        if (task.completed) {
          const userId = task.userId;

          if (completedByUser[userId]) {
            completedByUser[userId]++;
          } else {
            completedByUser[userId] = 1;
          }
        }
      });

      console.log(completedByUser);
    } catch (parseError) {
      console.error('Error parsing response:', parseError.message);
    }
  }
});
