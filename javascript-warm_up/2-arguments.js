#!/usr/bin/node
// Prints a message depending on the number of arguments passed

function checkArgs() {
	const args = process.argv.slice(2);
	if (args.length === 0) {
		console.log('No argument');
	} else if (args.length === 1) {
		console.log('Argument found');
	} else {
		console.log('Arguments found');
	}
}

checkArgs();
