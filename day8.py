from utilities import read_file
import copy

def process_input(input_lines):
    grid = []
    for row in input_lines:
        new_row = []
        for col in row:
            new_row.append(int(col))
        grid.append(new_row)
    return grid

def count_visible(tree_heights):
    tree_heights = copy.deepcopy(tree_heights)
    temp_row = [False] * len(tree_heights[0])
    visibility_mask = []
    for x in range(len(tree_heights)):
        visibility_mask.append(copy.deepcopy(temp_row))

    # print(visibility_mask)

    for row in range(len(tree_heights)):
        for col in range(len(tree_heights[0])):
            if row == 0 or row == len(tree_heights) - 1  or \
                    col == 0 or col == len(tree_heights[0]) - 1:
                visibility_mask[row][col] = True    
            else:
                visibility_mask[row][col] = False

    # count from left
    for row in range(1, len(tree_heights)):
        max_height = tree_heights[row][0]
        for col in range(1, len(tree_heights[row])):
            if tree_heights[row][col] > max_height:
                max_height = tree_heights[row][col]
                visibility_mask[row][col] = True
    
    # count from right
    for row in range(1, len(tree_heights)):
        max_height = tree_heights[row][-1]
        for col in range(len(tree_heights[row]) - 1, -1, -1):
            if tree_heights[row][col] > max_height:
                max_height = tree_heights[row][col]
                visibility_mask[row][col] = True

    # count from top
    for col in range(1, len(tree_heights[0])):
        max_height = tree_heights[0][col]
        for row in range(1, len(tree_heights)):
            if tree_heights[row][col] > max_height:
                max_height = tree_heights[row][col]
                visibility_mask[row][col] = True

    # count from bottom
    for col in range(1, len(tree_heights[0])):
        max_height = tree_heights[-1][col]
        for row in range(len(tree_heights) - 1, -1, -1):
            if tree_heights[row][col] > max_height:
                max_height = tree_heights[row][col]
                visibility_mask[row][col] = True

    count = 0
    for row in range(len(visibility_mask)):
        for col in range(len(visibility_mask[0])):
            if visibility_mask[row][col]:
                count += 1

    return count


def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day8_input')
    else:
        in_lines = read_file('data/day8_sample')

    tree_grid = process_input(in_lines)
    return count_visible(tree_grid)

print(part_one(False))


def viewing_score(tree_heights):
    max_score = 0
    for row in range(len(tree_heights)):
        for col in range(len(tree_heights[0])):
            score = calculate_score(tree_heights, row, col)
            if score > max_score:
                max_score = score

    return max_score


def calculate_score(tree_heights, start_row, start_col):
    counts = [0, 0, 0, 0]

    # check left
    for col in range(start_col - 1, -1, -1):
        counts[0] += 1
        if tree_heights[start_row][col] >= tree_heights[start_row][start_col]:            
            break

    # check right
    for col in range(start_col + 1, len(tree_heights[0])):
        counts[1] += 1
        if tree_heights[start_row][col] >= tree_heights[start_row][start_col]:
            break

    # check up
    for row in range(start_row - 1, -1, -1):
        counts[2] += 1
        if tree_heights[row][start_col] >= tree_heights[start_row][start_col]:
            break

    # check down
    for row in range(start_row + 1, len(tree_heights)):
        counts[3] += 1
        if tree_heights[row][start_col] >= tree_heights[start_row][start_col]:
            break

    score = 1
    for count in counts:
        score *= count

    return score


def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day8_input')
    else:
        in_lines = read_file('data/day8_sample')

    tree_grid = process_input(in_lines)
    return viewing_score(tree_grid)


print(part_two(False))