#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

const fs = require('fs');

const options = {
  encoding: 'utf8',
  flag: 'w'
};

request(args[0], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const results = JSON.parse(body);
      fs.writeFile(args[1], JSON.stringify(results), options, err => {
        if (err) {
          console.error(err);
        }
      });
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
