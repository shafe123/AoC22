from utilities import read_file

def split_ruck(input_list):
    for index in range(len(input_list)):
        size = len(input_list[index])//2
        input_list[index] = input_list[index][0:size], input_list[index][size:].strip()


def shared_items(split_rucks):
    result = []

    for ruck in split_rucks:
        unique_letters = list(set(ruck[0]).intersection(ruck[1]))[0]
        result.append(unique_letters)

    return result

def character_value(character: str):
    if character.isupper():
        return ord(character) - ord('A') + 27
    else:
        return ord(character) - ord('a') + 1

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day3_input')
    else:
        in_lines = read_file('data/day3_sample')

    split_ruck(in_lines)
    shared = shared_items(in_lines)

    scores = []
    for char in shared:
        scores.append(character_value(char))
    
    return sum(scores)

print(part_one(False))