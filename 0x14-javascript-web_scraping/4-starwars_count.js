#!/usr/bin/node
const request = require('request')
const args = process.argv.slice(2)

const endpoint = 'https://swapi-api.alx-tools.com/api/people/18'

request(endpoint, (err, response, body) => {
	if (err) {
		console.error(err);
	} else { 
		console.log(JSON.parse(body).films.length);
	}
});
