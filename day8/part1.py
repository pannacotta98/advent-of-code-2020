# input = '''nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6'''.splitlines()

input = open('input', 'r').readlines()

acc = 0
index = 0
visited_lines = set()
while index < len(input):
  (operation, argument) = input[index].split()

  if index in visited_lines:
    print(acc)
    break
  visited_lines.add(index)

  if operation == 'acc':
    acc += int(argument)
    index += 1
  elif operation == 'jmp':
    index += int(argument)
  elif operation == 'nop':
    index += 1
