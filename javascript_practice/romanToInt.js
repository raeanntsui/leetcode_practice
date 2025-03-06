function romanToInt(str) {
  const dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
  };

  let total = 0;
  let i = 0;
  while (i < str.length) {
    if (i + 1 < str.length) {
      let pair = str[i] + str[i + 1];
      if (dict[pair]) {
        total += dict[pair];
        i += 2;
        continue;
      }
    }
    total += dict[str[i]];
    i += 1;
  }
  console.log("total", total);
  //   return;
}

romanToInt("III");
romanToInt("LVIII");
romanToInt("MCMXCIV");
