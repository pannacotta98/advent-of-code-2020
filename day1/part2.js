const fs = require('fs');

const input = fs.readFileSync('input', 'utf8');
const numArray = input.split('\n').map((d) => +d);

for (const num1 of numArray) {
  for (const num2 of numArray) {
    for (const num3 of numArray) {
      if (num1 + num2 + num3 === 2020) {
        console.log(num1 * num2 * num3);
        return;
      }
    }
  }
}
