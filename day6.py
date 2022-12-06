from utilities import read_file

def find_marker(line, count):
    for index in range(len(line)):
        if len(set(line[index:index+count])) == count:
            return index + count

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day6_input')
    else:
        in_lines = read_file('data/day6_sample')

    for line in in_lines:
        print(find_marker(line, 4))

part_one(False)

def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day6_input')
    else:
        in_lines = read_file('data/day6_sample')

    for line in in_lines:
        print(find_marker(line, 14))

part_two(False)