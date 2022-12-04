from utilities import read_file
from typing import List

def split_numbers(input_lines):
    for index in range(len(input_lines)):
        split = input_lines[index].split(',')
        string_list = split[0].split('-')
        string_list.extend(split[1].split('-'))
        input_lines[index] = [int(x) for x in string_list]

def unwind_numbers(splits):
    for index in range(len(splits)):
        splits[index] = set(range(splits[index][0], splits[index][1]+1)), set(range(splits[index][2], splits[index][3]+1))

def ranges_subset(ranges: List[List[set]]):
    for range in ranges:
        yield range[0].issubset(range[1]) or range[1].issubset(range[0])

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day4_input')
    else:
        in_lines = read_file('data/day4_sample')

    split_numbers(in_lines)
    unwind_numbers(in_lines)

    return sum(1 for x in ranges_subset(in_lines) if x)

print(part_one(False))

def ranges_intersect(ranges: List[List[set]]):
    for range in ranges:
        yield range[0].intersection(range[1])

def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day4_input')
    else:
        in_lines = read_file('data/day4_sample')

    split_numbers(in_lines)
    unwind_numbers(in_lines)

    return sum(1 for x in ranges_intersect(in_lines) if x)

print(part_two(False))