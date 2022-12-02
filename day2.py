def read_file(input_file):
    results = []
    with open(input_file) as in_file:
        for line in in_file:
            opponent, you = line.strip().split()
            results.append((opponent, you))

    return results

def score_round(opponent, player):
    if player == "X":
        shape_score = 1
        if opponent == "A":
            game_score = 3
        elif opponent == "B":
            game_score = 0
        elif opponent == "C":
            game_score = 6
    elif player == "Y":
        shape_score = 2
        if opponent == "A":
            game_score = 6
        elif opponent == "B":
            game_score = 3
        elif opponent == "C":
            game_score = 0
    elif player == "Z":
        shape_score = 3
        if opponent == "A":
            game_score = 0
        elif opponent == "B":
            game_score = 6
        elif opponent == "C":
            game_score = 3
    return shape_score + game_score

def determine_play(opponent, guide):
    if guide == "X":
        if opponent == "A":
            return "Z"
        elif opponent == "B":
            return "X"
        elif opponent == "C":
            return "Y"
    elif guide == "Y":
        if opponent == "A":
            return "X"
        elif opponent == "B":
            return "Y"
        elif opponent == "C":
            return "Z"
    elif guide == "Z":
        if opponent == "A":
            return "Y"
        elif opponent == "B":
            return "Z"
        elif opponent == "C":
            return "X"

def score_game(lines):
    result = 0
    for line in lines:
        result += score_round(line[0], line[1])
    return result

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day2_input')
    else:
        in_lines = read_file('data/day2_sample')

    score = score_game(in_lines)
    return score

print(part_one(False))

def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day2_input')
    else:
        in_lines = read_file('data/day2_sample')

    for index in range(len(in_lines)):
        in_lines[index] = (in_lines[index][0], determine_play(in_lines[index][0], in_lines[index][1]))
    
    score = score_game(in_lines)
    return score

print(part_two(False))