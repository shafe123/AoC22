from utilities import read_file
import math

def process_lines(input_lines):
    min_x = 0
    min_y = 0
    max_x = -math.inf
    max_y = -math.inf
    
    all_paths = []
    # read lines
    for line in input_lines:
        segments = line.split(' -> ')
        new_path = []
        for segment in segments:
            x, y = segment.split(',')
            x, y = int(x), int(y)
            new_path.append((x, y))

            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            
        all_paths.append(new_path)

    # build empty map
    map = []
    for row in range(min_y, max_y + 3):
        new_row = []
        for col in range(min_x, max_x + 500):
            new_row.append('None')
        map.append(new_row)

    # fill map with rocks
    for path in all_paths:
        start = path[0]
        for end_point in path[1:]:
            draw(map, start, end_point, min_x)
            start = end_point

    # bottom row part 2
    for col in range(min_x, max_x + 500):
        map[row][col - min_x] = 'rock'

    return map, min_x
    

def draw(map, start, end, min_x):
    # row is the same
    if start[0] == end[0]:
        sign = int(math.copysign(1, end[1] - start[1]))
        for row in range(start[1], end[1] + sign, sign):
            map[row][start[0] - min_x] = 'rock'

    elif start[1] == end[1]:
        sign = int(math.copysign(1, end[0] - start[0]))
        for col in range(start[0], end[0] + sign, sign):
            map[start[1]][col - min_x] = 'rock'


def fill_sand(map, start_point, min_x):
    count = 0
    start_point = (start_point[0] - min_x, start_point[1])

    while True:
        count += 1

        if drop_sand(map, start_point):
            return map, count - 1

def drop_sand(map, start_point):
    col, row = start_point

    try:
        # check below
        if map[row + 1][col] == 'None':
            return drop_sand(map, (col, row + 1))
        # check left
        elif map[row + 1][col - 1] == 'None':
            return drop_sand(map, (col - 1, row + 1))
        # check right
        elif map[row + 1][col + 1] == 'None':
            return drop_sand(map, (col + 1, row + 1))
        # part 2, map is filled
        elif map[row][col] == 'sand':
            return True
        # place sand
        else:
            map[row][col] = 'sand'
            return False
    except:
        return True
    

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day14_input')
    else:
        in_lines = read_file('data/day14_sample')

    map, min_x = process_lines(in_lines)
    map, sands_of_time = fill_sand(map, (500, 0), min_x)
    return sands_of_time

print(part_one(False))