from itertools import combinations

num_numbers_considered = 25
puzzle_input = open('input').read().splitlines()

# num_numbers_considered = 5
# puzzle_input = '''35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576'''.splitlines()

for i in range(num_numbers_considered, len(puzzle_input)):
  start = i-num_numbers_considered
  closest_prec = puzzle_input[start:i]
  sum_found = False
  for combination in combinations(closest_prec, 2):
    if int(combination[0]) + int(combination[1]) == int(puzzle_input[i]):
      sum_found = True
      break
  if not sum_found:
    for j in range(len(puzzle_input)-1):
      summation = int(puzzle_input[j])
      for k in range(j+1, len(puzzle_input)):
        summation += int(puzzle_input[k])
        if summation == int(puzzle_input[i]):
          sublist = [int(d) for d in puzzle_input[j:k+1]]
          print(int(max(sublist)) + int(min(sublist)))
        if summation > int(puzzle_input[i]):
          break

# ps. i should probably have parsed the input as numbers heheh