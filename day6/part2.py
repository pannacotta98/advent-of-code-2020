from collections import defaultdict

input = open('input', 'r').read().split('\n\n')

cum_sum = 0
for group_input in input:
  occurences = defaultdict(lambda: 0)
  per_person = group_input.split()
  for person in per_person:
    for char in person:
      occurences[char] += 1
  cum_sum += len([quest for quest in occurences if occurences[quest] == len(per_person)])

print(cum_sum)