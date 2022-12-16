from utilities import read_file
import math

class node():
    def __init__(self, name) -> None:
        self.name = name
        self.neighbors = set()
        self.flow_rate = 0

def process_lines(input_lines):
    valves = {}
    for line in input_lines:
        valve = line[6:8]
        rate = line[23:]
        rate = int(rate[:rate.index(';')])


        if valve in valves.keys():
            this_node = valves[valve]
        else:
            this_node = node(valve)
            valves[valve] = this_node
        
        this_node.flow_rate = rate

        neighbors = line[line.index('valve') + 6:].split(',')
        for neighbor in neighbors:
            neighbor = neighbor.strip()
            if neighbor not in valves.keys():
                valves[neighbor] = node(neighbor)
            
            this_node.neighbors.add(valves[neighbor])

    for name, valve in valves.items():
        valve.neighbors = list(valve.neighbors)

    return valves


# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
def compute_distance(valves):
    distance_map = {}
    for name_1 in valves.keys():
        new_row = {}
        for name_2 in valves.keys():
            if name_1 not in distance_map:
                distance_map[name_1] = {}
            if name_1 == name_2:
                distance_map[name_1][name_2] = 0    
            else:
                distance_map[name_1][name_2] = math.inf
            
    for name, valve in valves.items():
        for neighbor in valves[name].neighbors:
            distance_map[name][neighbor.name] = 1

    for k in valves.keys():
        for i in valves.keys():
            for j in valves.keys():
                if distance_map[i][j] > distance_map[i][k] + distance_map[k][j]:
                    distance_map[i][j] = distance_map[i][k] + distance_map[k][j]

    return distance_map


def search(valves, start, time, open_list, distances, good_valves):
    if time <= 0:
        return 0
    start_point = valves[start]
    best = 0

    to_check = [valve for valve in good_valves if valve not in open_list]
    if len(to_check) == 0 or time <= 0:
        return 0

    for valve in to_check:
        time_remaining = time
        if valve == start:
            continue
        
        # go to valve then open it
        time_remaining = time_remaining - distances[start][valve] - 1
        if time_remaining > 0:
            new_open = open_list[:]
            new_open.append(valve)
            valve_score = valves[valve].flow_rate * time_remaining
            test = search(valves, valve, time_remaining, new_open, distances, good_valves)
            best = max(test + valve_score, best)

    return best
    

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day16_input')
    else:
        in_lines = read_file('data/day16_sample')

    valves = process_lines(in_lines)
    distances = compute_distance(valves)
    good_valves = [name for name, valve in valves.items() if valve.flow_rate > 0]
    best = search(valves, 'AA', 30, [], distances, good_valves)
    return best

# print(part_one(False))

def search_with_elephant(valves, my_position, my_time_to_next, elephant_position, elephant_time_to_next, time, open_list, distances, good_valves):
    if len(good_valves) - len(open_list) == 0 or time <= 0:
        return 0
    best = 0

    if my_time_to_next == 0 or elephant_time_to_next == 0:
        to_check = [valve for valve in good_valves if valve not in open_list]

        if elephant_time_to_next == 0 and my_time_to_next == 0:
            for my_valve in to_check:
                if my_valve == my_position:
                    continue
                for ele_valve in to_check:
                    if ele_valve == elephant_position or my_valve == ele_valve:
                        continue
                    new_open = open_list[:]
                    valve_score = valves[my_valve].flow_rate * (time - distances[my_position][my_valve] - 1) \
                                  + valves[ele_valve].flow_rate * (time - distances[elephant_position][ele_valve] - 1)
                    new_open.append(my_valve)
                    new_open.append(ele_valve)
                    best = max(best, valve_score + 
                                     search_with_elephant(valves, my_valve, distances[my_position][my_valve], ele_valve, distances[elephant_position][ele_valve], time - 1, new_open, distances, good_valves))

        elif my_time_to_next == 0:

            for my_valve in to_check:
                if my_valve == my_position:
                    continue
                new_open = open_list[:]
                new_open.append(my_valve)
                valve_score = valves[my_valve].flow_rate * (time - distances[my_position][my_valve] - 1)
                best = max(best, valve_score + 
                                  search_with_elephant(valves, my_valve, distances[my_position][my_valve], elephant_position, elephant_time_to_next - 1, time - 1, new_open, distances, good_valves))
        
        elif elephant_time_to_next == 0:
            valve_score = valves[elephant_position].flow_rate * (time - 1)

            for ele_valve in to_check:
                if ele_valve == elephant_position:
                    continue
                valve_score = valves[ele_valve].flow_rate * (time - distances[elephant_position][ele_valve] - 1)
                new_open = open_list[:]
                new_open.append(ele_valve)
                best = max(best, valve_score + 
                                  search_with_elephant(valves, my_position, my_time_to_next - 1, ele_valve, distances[elephant_position][ele_valve], time - 1, new_open, distances, good_valves))
    else:
        return search_with_elephant(valves, my_position, my_time_to_next - 1, elephant_position, elephant_time_to_next - 1, time - 1, open_list, distances, good_valves)

    return best

def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day16_input')
    else:
        in_lines = read_file('data/day16_sample')

    valves = process_lines(in_lines)
    distances = compute_distance(valves)
    good_valves = [name for name, valve in valves.items() if valve.flow_rate > 0]
    best = search_with_elephant(valves, 'AA', 0, 'AA', 0, 26, [], distances, good_valves)
    return best

print(part_two(False))