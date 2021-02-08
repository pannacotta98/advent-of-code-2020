const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8');
const numArray = input.split('\n').map((d) => +d);

for (const num1 of numArray) {
  for (const num2 of numArray) {
    if (num1 + num2 === 2020) {
      console.log(num1 * num2);
      return;
    }
  }
}
