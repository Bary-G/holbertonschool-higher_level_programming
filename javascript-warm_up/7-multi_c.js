#!/usr/bin/node

const args = process.argv.slice(2);
const x = Number(args[0]);

if (isNaN(x)) {
    console.log('Missing number of occurrences');
} else {
    let index = 0;
    while (index < x) {
        console.log('C is fun');
        index++;
    }
}
