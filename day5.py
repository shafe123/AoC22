from utilities import read_file
import queue
from typing import List

def split_input(input):
    for index, line in enumerate(input):
        if line == "\n":
            crates, instructions = input[:index-1], input[index + 1:]

    return crates, instructions

def process_crates(crate_lines):
    line_width = len(crate_lines[0])
    num_stacks = (line_width + 1) //4

    stacks = []
    for index in range(num_stacks):
        stacks.append(queue.LifoQueue())

    # since it's lifo we need to process from bottom of file
    for line in crate_lines[::-1]:
        for index in range(num_stacks):
            letter = line[index * 4 + 1]
            if letter != " ":
                stacks[index].put(letter)

    return stacks

def process_instructions(stacks: List[queue.LifoQueue], instructions):
    for line in instructions:
        splits = line.split(' ')

        count = int(splits[1])
        source = int(splits[3])
        destination = int(splits[5])

        for _ in range(count):
            letter = stacks[source - 1].get()
            stacks[destination - 1].put(letter)
    

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day5_input', False)
    else:
        in_lines = read_file('data/day5_sample', False)

    crates, instructions = split_input(in_lines)
    stacks = process_crates(crates)

    process_instructions(stacks, instructions)

    final_letters = ""
    for stack in stacks:
        final_letters += stack.get()
    return final_letters

print(part_one(False))

def process_mult_instructions(stacks: List[queue.LifoQueue], instructions):
    for line in instructions:
        splits = line.split(' ')

        count = int(splits[1])
        source = int(splits[3])
        destination = int(splits[5])

        movers = queue.LifoQueue()
        for _ in range(count):
            movers.put(stacks[source - 1].get())

        while not movers.empty():
            stacks[destination - 1].put(movers.get())

def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day5_input', False)
    else:
        in_lines = read_file('data/day5_sample', False)

    crates, instructions = split_input(in_lines)
    stacks = process_crates(crates)

    process_mult_instructions(stacks, instructions)

    final_letters = ""
    for stack in stacks:
        final_letters += stack.get()
    return final_letters

print(part_two(False))