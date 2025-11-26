#!/usr/bin/node

function second_biggest(...numbers) {
    if (numbers.length < 2) return 0;
    numbers = numbers.map(Number);
    numbers.sort((a, b) => b - a);
    return numbers[1];
}

const args = process.argv.slice(2);
console.log(second_biggest(...args));
