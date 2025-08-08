#!/usr/bin/node
// Prints the full array

function checkArgs () {
  const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
  let index = 0;
  while (arr[index]) {
    console.log(arr[index]);
    index = index + 1;
  }
}

checkArgs();
