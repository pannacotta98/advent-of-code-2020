const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8');
const inputLines = input.split('\n');
inputLines.pop(); // Last line is empty

let treeCount = 0;
let horPos = 0;

for (const line of inputLines) {
  const isTreeEncountered = line[horPos % 31] === '#';
  if (isTreeEncountered) ++treeCount;
  horPos += 3;
}

console.log(treeCount);
