from utilities import read_file
import math
from queue import PriorityQueue

class square(object):
    def __init__(self, coord, gscore, hscore, parent) -> None:
        self.row = coord[0]
        self.col = coord[1]
        self.coord = coord
        self.g_score = gscore
        self.h_score = hscore
        self.f_score = gscore + hscore
        self.parent = parent

    def __lt__(self, other):
        return self.f_score < other.f_score
            
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


def process_lines(input_lines):
    result = []
    start = ()
    end = ()
    for row, line in enumerate(input_lines):
        new_row = []
        for col, char in enumerate(line):
            if char == 'S':
                start = (row, col)
                new_row.append(0)
            elif char == 'E':
                end = (row, col)
                new_row.append(25)
            else:
                val = ord(char) - ord('a')
                new_row.append(val)
        result.append(new_row)
    return result, start, end


def h(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def rebuild_path(parents, end_point, start_point):
    result = []
    x = parents[end_point[0]][end_point[1]]

    while x != start_point:
        result.append(x[:])
        x = parents[x[0]][x[1]]

    result.append(start_point)
    return result




def path_find(map, start, end):
    to_visit = [square(start, 0, h(start, end), None)]
    fscore = []
    gscore = []
    parent = []

    for row in range(len(map)):
        new_f = []
        new_g = []
        new_parent = []
        for col in range(len(map[0])):
            new_f.append(math.inf)
            new_g.append(math.inf)
            new_parent.append(None)
        fscore.append(new_f)
        gscore.append(new_g)
        parent.append(new_parent)
    
    gscore[start[0]][start[1]] = 0
    fscore[start[0]][start[1]] = 0 + h(start, end)

    while len(to_visit) > 0:
        next = to_visit.pop(0)

        if next.coord == end:
            return rebuild_path(parent, next.coord, start)
        
        # check down
        if next.row + 1 < len(map):
            check_square(map, end, to_visit, fscore, gscore, parent, next, next.row + 1, next.col)
        
        # check up
        if next.row - 1 >= 0:
            check_square(map, end, to_visit, fscore, gscore, parent, next, next.row - 1, next.col)
        
        # check left
        if next.col - 1 >= 0:
            check_square(map, end, to_visit, fscore, gscore, parent, next, next.row, next.col - 1)
        
        # check right
        if next.col + 1 < len(map[0]):
            check_square(map, end, to_visit, fscore, gscore, parent, next, next.row, next.col + 1)
        
        to_visit.sort()

def check_square(map, end, to_visit, fscore, gscore, parent, next, neighbor_row, neighbor_col):
    if map[neighbor_row][neighbor_col] <= map[next.row][next.col] + 1:
        if next.g_score + 1 < gscore[neighbor_row][neighbor_col]:
            parent[neighbor_row][neighbor_col] = (next.row, next.col)
            gscore[neighbor_row][neighbor_col] = next.g_score + 1
            fscore[neighbor_row][neighbor_col] = next.g_score + 1 + h((neighbor_row, neighbor_col), end)

            new_square = square((neighbor_row, neighbor_col), next.g_score + 1, h((neighbor_row, neighbor_col), end), next)
            if new_square not in to_visit:
                to_visit.append(new_square)


def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day12_input')
    else:
        in_lines = read_file('data/day12_sample')

    map, start, end = process_lines(in_lines)
    path = path_find(map, start, end)

    print(path)
    return len(path)



print(part_one(False))