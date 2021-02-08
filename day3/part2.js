const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8');
const inputLines = input.split('\n');
inputLines.pop(); // Last line is empty

let prod = 1;
const slopes = [
  // [right, down]
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2],
];

for (const [rSlope, dSlope] of slopes) {
  let treeCount = 0;
  let pos = [0, 0]; // [r, d]

  while (pos[1] < inputLines.length) {
    const isTreeEncountered = inputLines[pos[1]][pos[0] % 31] === '#';
    if (isTreeEncountered) ++treeCount;

    pos = [pos[0] + rSlope, pos[1] + dSlope];
  }

  prod *= treeCount;
}

console.log(prod);
