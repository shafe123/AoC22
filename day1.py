def read_file(input_file):
    result = []

    with open(input_file) as in_file:
        for line in in_file:
            line = line.strip()
            if line == "":
                result.append(None)
            else:
                result.append(int(line))

    return result

def count_calories(calorie_counts):
    total_calories_by_elf = [0]
    current_index = 0

    for entry in calorie_counts:
        if entry != None:
            total_calories_by_elf[current_index] += entry
        else:
            total_calories_by_elf.append(0)
            current_index += 1

    return total_calories_by_elf

def part_one(sample_file = False):
    if not sample_file:
        in_lines = read_file('data/day1_input')
    else:
        in_lines = read_file('data/day1_sample')

    calories = count_calories(in_lines)
    return max(calories)

def part_two(sample_file = False):
    if not sample_file:
        in_lines = read_file('data/day1_input')
    else:
        in_lines = read_file('data/day1_sample')

    calories = count_calories(in_lines)
    calories.sort(reverse=True)
    print(calories[0:3])
    return sum(calories[0:3])

#in_lines = read_file('data/day1_sample')
print(part_one())
print(part_two())
