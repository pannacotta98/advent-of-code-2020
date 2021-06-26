# input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.'''.splitlines()

input = open('input', 'r').read().splitlines()

def extract_data_from_line(line):
  [outer_bag, right_part] = line.replace(' bags', '').replace(' bag', '').split(' contain ')
  # Assuming no more than 9 bags of each type (hopefully its fine :)))
  inner_bags = [(int(entry[0]), entry[2:]) for entry in right_part[:-1].split(', ') if 'other' not in entry]
  return(outer_bag, inner_bags)

def num_child_bags(bag, mapping):
  num = 0
  for (num_this_color, this_color) in mapping[bag]:
    num += num_this_color
    num += num_this_color * num_child_bags(this_color, mapping)
  return num


contains_mapping = {}
for line in input:
  (key, val) = extract_data_from_line(line)
  contains_mapping[key] = val

print(num_child_bags('shiny gold', contains_mapping))
