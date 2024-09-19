#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');

fs.readFile(args[0], 'utf8', (err, data) => {
    if (err) {
        console.errer(err);
    } else {
        console.log(data);
    }
}};
