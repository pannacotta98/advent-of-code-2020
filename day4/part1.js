const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8').split('\n\n');

let numValid = 0;

input.forEach((entry) => {
  // Can i get away with just counting the colons? ans: yes
  const numColons = (entry.match(/:/g) || []).length;

  if (numColons === 8 || (numColons === 7 && !entry.match(/cid/))) {
    numValid++;
  }
});

console.log(numValid);
