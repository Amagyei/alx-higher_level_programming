#!/usr/bin/node
const request = require('request')
const args = process.argv.slice(2)

const endpoint = 'https://swapi-api.alx-tools.com/api/people/18'

request(endpoint, (args[0], response, body) => {
	if (err) {
		console.error(err);
	} else { 
		const results = JSON.parse.body.results;
		let n = 0;

		resutls.forEach(result => { 
			const characters = result.characters;

			characters.forEach(character => {
				if(character.endsWith('18/')) {
					n++;
				}
			});
		 });
		console.log(n)
	}
});
