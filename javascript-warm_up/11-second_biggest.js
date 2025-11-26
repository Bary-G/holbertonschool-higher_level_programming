#!/usr/bin/node

function secondBiggest (...numbers) {
  if (numbers.length < 2) {
    return 0;
  }
  const nums = numbers.map(Number);
  nums.sort((a, b) => b - a);
  return nums[1];
}

const args = process.argv.slice(2);
console.log(secondBiggest(...args));
