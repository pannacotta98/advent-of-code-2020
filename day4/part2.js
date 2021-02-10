const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input', 'utf8').split('\n\n');

const requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];
const validEcl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'];

let numValid = 0;

input.forEach((entry) => {
  // Can i get away with just counting the colons? ans: yes
  const fields = entry.split(/[ \n]/);
  const validFields = [];

  if (fields.length === 8 || fields.length === 7) {
    for (const field of fields) {
      const [fieldName, fieldVal] = field.split(':');

      switch (fieldName) {
        case 'byr':
          if (+fieldVal >= 1920 && +fieldVal <= 2002) validFields.push('byr');
          break;
        case 'iyr':
          if (+fieldVal >= 2010 && +fieldVal <= 2020) validFields.push('iyr');
          break;
        case 'eyr':
          if (+fieldVal >= 2020 && +fieldVal <= 2030) validFields.push('eyr');
          break;
        case 'hgt':
          const unit = fieldVal.slice(-2);
          const num = +fieldVal.slice(0, -2);
          if (
            (unit === 'cm' && num >= 150 && num <= 193) ||
            (unit === 'in' && num >= 59 && num <= 76)
          ) {
            validFields.push('hgt');
          }
          break;
        case 'hcl':
          if (fieldVal.match(/^#[0-9,a-f]{6}$/)) validFields.push('hcl');
          break;
        case 'ecl':
          if (validEcl.includes(fieldVal)) validFields.push('ecl');
          break;
        case 'pid':
          if (fieldVal.match(/^[0-9]{9}$/)) validFields.push('pid');
          break;
      }
    }
    if (!requiredFields.map((f) => validFields.includes(f)).includes(false)) {
      numValid++;
    }
  }
});

console.log(numValid);
