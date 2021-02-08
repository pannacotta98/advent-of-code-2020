const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8');
let numValid = 0;

for (const line of input.split('\n')) {
  if (line === '') continue;
  const [positions, letterTemp, password] = line.split(' ');
  const letter = letterTemp[0];
  const [pos1, pos2] = positions.split('-');
  if (
    (password[pos1 - 1] === letter && password[pos2 - 1] !== letter) ||
    (password[pos1 - 1] !== letter && password[pos2 - 1] === letter)
  ) {
    ++numValid;
  }
}

console.log(numValid);
