const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8');
let numValid = 0;

for (const line of input.split('\n')) {
  if (line === '') continue;
  const [range, required, password] = line.split(' ');
  const [low, high] = range.split('-');
  const pattern = new RegExp(required[0], 'g');
  const occurences = (password.match(pattern) || []).length;
  if (occurences >= low && occurences <= high) {
    ++numValid;
  }
}

console.log(numValid);
