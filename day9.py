from utilities import read_file

def determine_new_tail(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    if abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1:
        tail_x += (head_x - tail_x) // 2
        tail_y += (head_y - tail_y) // 2

    elif abs(head_x - tail_x) > 1:
        if abs(head_y - tail_y) == 1:
            tail_y += (head_y - tail_y)
        tail_x += (head_x - tail_x) // 2

    elif abs(head_y - tail_y) > 1:
        if abs(head_x - tail_x) == 1:
            tail_x += (head_x - tail_x)
        tail_y += (head_y - tail_y) // 2

    return tail_x, tail_y

def process_input(instructions):
    tail_path = [(0, 0)]

    knots = []
    for _ in range(10):
        knots.append((0, 0))

    head = knots[0]
    tail = knots[9]
    for instruction in instructions:
        direction, count = instruction.split(' ')
        count = int(count)

        for _ in range(count):

            if direction == "R":
                knots[0] = knots[0][0] + 1, knots[0][1]
            elif direction == "L":
                knots[0] = knots[0][0] - 1, knots[0][1]
            elif direction == "U":
                knots[0] = knots[0][0], knots[0][1] + 1
            else:
                knots[0] = knots[0][0], knots[0][1] - 1
            
            for index in range(len(knots) - 1):
                knots[index + 1] = determine_new_tail(knots[index], knots[index + 1])
            tail_path.append(knots[index + 1])

    unique_path = set(tail_path)
    return unique_path

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day9_input')
    else:
        in_lines = read_file('data/day9_sample')

    path = process_input(in_lines)
    return len(path)

print(part_one(False))
