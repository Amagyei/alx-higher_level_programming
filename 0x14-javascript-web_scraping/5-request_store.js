#!/usr/bin/node
const request = require('request')
const args = process.argv.slice(2)

const endpoint = 'https://swapi-api.alx-tools.com/api/people/18'
const uri = args[0]

const fs = require('fs')

const options = {
  encoding: 'utf8',
  flag: 'w'
};

request(uri, (err, response, body) => {
	if (err) {
		console.error(err);
	} else {
		fs.writeFile(args[1], body, options, err => {
			if (err) {
				console.error(err);
			}
		})
	}
});
