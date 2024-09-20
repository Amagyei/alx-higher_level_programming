#!/usr/bin/node
const request = require('request')
const args = process.argv.slice(2)

const endpoint = 'https://swapi-api.alx-tools.com/api/people/18'
const uri = args[0]

request(uri, (err, response, body) => {
	if (err) {
		console.error(err);
	} else { 
		const tasks = JSON.parse(body);

		const completed = {}

		tasks.forEach(tasks => { 
			if (completed[task.userId.toString()]) {
				if (task.completed) {
					completed[task.userId.toString()]++;
				}
			} else {
				if (task.completed) {
					completed[task.userId.toString()] = 1;
				}
			}
		});
		console.log(n)
	}
});
