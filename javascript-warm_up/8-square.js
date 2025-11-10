#!/usr/bin/node

const args = process.argv.slice(2);
const x = Number(args[0]);
let index = 0;

if (isNaN(x)) {
    console.log('Missing size');
} else {
    while (index < x) {
        console.log('X'.repeat(x));
        index++;
    }
}
