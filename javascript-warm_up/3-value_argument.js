#!/usr/bin/node
// Prints the first argument passed to it

function checkArgs() {
  const args = process.argv.slice(2);
  if (args[0] === undefined) {
    console.log('No argument');
  } else {
    console.log(args[0]);
  }
}

checkArgs();
