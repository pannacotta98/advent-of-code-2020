import math

def seat_ID(code):
  min_row = 0
  max_row = 127
  min_col = 0
  max_col = 7
  
  for char in code:
    if char == 'F': max_row = min_row + math.floor((max_row - min_row) / 2)
    elif char == 'B': min_row = min_row + math.ceil((max_row - min_row) / 2)
    elif char == 'L': max_col = min_col + math.floor((max_col - min_col) / 2)
    elif char == 'R': min_col = min_col + math.ceil((max_col - min_col) / 2)
  
  return min_row * 8 + min_col


f = open('input', 'r')
input = f.read().split()
all_other_seat_IDs = [seat_ID(code) for code in input]
max_seat_ID = max(all_other_seat_IDs)
print(f'Day 5 part 1 solution: {max_seat_ID}')

sorted_IDs = sorted(all_other_seat_IDs)
last_ID = sorted_IDs[0]
for ID in sorted_IDs[1:]:
  if ID != last_ID + 1:
    my_seat = last_ID + 1
    break
  last_ID = ID

print(f'Day 5 part 2 solution: {my_seat}')
