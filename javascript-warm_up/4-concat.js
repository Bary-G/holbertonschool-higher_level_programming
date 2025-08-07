#!/usr/bin/node
// Concat two arguments passed to it

function checkArgs () {
  const args = process.argv.slice(2);
  console.log(`${args[0]} is ${args[1]}`);
}

checkArgs();
