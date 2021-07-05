from itertools import combinations

num_numbers_considered = 25
puzzle_input = open('input').readlines()

for i in range(num_numbers_considered, len(puzzle_input)):
  start = i-num_numbers_considered
  closest_prec = puzzle_input[start:i]
  sum_found = False
  for combination in combinations(closest_prec, 2):
    if int(combination[0]) + int(combination[1]) == int(puzzle_input[i]):
      sum_found = True
      break
  if not sum_found:
    print(puzzle_input[i])