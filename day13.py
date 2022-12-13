from utilities import read_file
from collections import namedtuple


class fricken_thing(object):
    def __init__(self, vals):
        self.vals = vals

    def __lt__(self, other):
        return check_pair(self.vals, other.vals)

    def __eq__(self, other):
        return self.vals == other.vals


Pair = namedtuple('Pair', ['left', 'right'])

def process_lines(input_lines):
    result = []
    for count in range(0, len(input_lines) + 1, 3):
        left = eval(input_lines[count])
        right = eval(input_lines[count + 1])
        result.append(fricken_thing(left))
        result.append(fricken_thing(right))
    return result


def check_pair(left, right):
    for index in range(len(left)):
        try:
            if type(left[index]) == int and type(right[index]) == int:
                if left[index] < right[index]:
                    return True 
                elif left[index] > right[index]:
                    return False
            else:   
                if type(left[index]) == list and type(right[index]) != list:
                    right[index] = [right[index]]

                elif type(left[index]) != list and type(right[index]) == list:
                    left[index] = [left[index]]

                
                result = check_pair(left[index], right[index])
                if result is not None:
                    return result

            
        except:
            return False

    if len(left) < len(right):
        return True
    return None

def filter_pairs(pairs):
    correct_pairs = []
    indices = []
    for index, pair in enumerate(pairs):
        if check_pair(pair.left, pair.right):
            indices.append(index + 1)
            correct_pairs.append(pair)
        
    return indices, correct_pairs

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day13_input')
    else:
        in_lines = read_file('data/day13_sample')

    pairs = process_lines(in_lines)
    indices, good_pairs = filter_pairs(pairs)
    return sum(indices)

    

# print(part_one(False))


def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day13_input')
    else:
        in_lines = read_file('data/day13_sample')

    pairs = process_lines(in_lines)
    val1 = fricken_thing([[2]])
    val2 = fricken_thing([[6]])
    pairs.append(val1)
    pairs.append(val2)
    pairs.sort()
    return (pairs.index(val1) + 1) * (pairs.index(val2) + 1)

print(part_two(False))
