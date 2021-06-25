input = open('input', 'r').read().split('\n\n')

cum_sum = 0
for group_input in input:
  newlines_removed = group_input.replace('\n', '')
  cum_sum += len(set(newlines_removed))

print(cum_sum)