#!/usr/bin/node
const myArgs = process.argv.slice(2);
let i = (parseInt(myArgs[0]));
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    console.log('C is fun');
    i = i - 1;
  }
}
