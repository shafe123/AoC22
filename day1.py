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

#in_lines = read_file('data/day1_sample')
in_lines = read_file('data/day1_input')
calories = count_calories(in_lines)
calories.sort(reverse=True)
print(calories[0:3])
print(sum(calories[0:3]))
