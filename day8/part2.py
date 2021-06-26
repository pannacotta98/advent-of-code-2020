import copy

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

def run(input):
  acc = 0
  index = 0
  visited_lines = set()
  while index < len(input):
    (operation, argument) = input[index].split()

    if index in visited_lines:
      return False
    visited_lines.add(index)

    if operation == 'acc':
      acc += int(argument)
      index += 1
    elif operation == 'jmp':
      index += int(argument)
    elif operation == 'nop':
      index += 1

  return acc


# Simple brute force
for index in range(len(input)):
  modified_input = copy.copy(input)
  (operation, argument) = input[index].split()

  if operation == 'jmp':
    modified_input[index] = 'nop ' + argument
  elif operation == 'nop':
    modified_input[index] = 'jmp ' + argument

  run_result = run(modified_input)
  if run_result != False:
    print(run_result)
    break


