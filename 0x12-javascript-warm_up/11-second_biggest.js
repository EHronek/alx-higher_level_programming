#!/usr/bin/node
let args = process.argv.splice(2);
args = parseInt(args);
len = args.length;
if (len === 0) console.log(0);
if (len === 1) console.log(1);
if (len >= 2) {
  for (let i = 0; i < len; i++) {
    let max = 0;
    max = args[i];
    if (args[i] < args[i + 1]) {
      max = args[ i+ 1];
    } else {
        max = args[i];
}
}
