#!/usr/bin/node
// A script that prints x times 'C is fun'

function checkArgs () {
  const args = process.argv.slice(2);
  const num = parseInt(args[0]);
  let index = 1;

  if (isNaN(num)) {
    console.log('Missing number of occurrences');
  } else {
    while (index <= num) {
      console.log('C is fun');
      index += 1;
    }
  }
}

checkArgs();
