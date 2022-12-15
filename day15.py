from utilities import read_file
import math

def process_lines(input_lines):
    max_x = 0
    max_y = 0
    max_distance = 0

    pairs = []
    for line in input_lines:
        sensor, beacon = line.split(': ')
        sensor = sensor[10:]
        sensor_x, sensor_y = sensor.split(', ')
        sensor_x, sensor_y = int(sensor_x[2:]), int(sensor_y[2:])

        if sensor_x > max_x:
            max_x = sensor_x
        if sensor_y > max_y:
            max_y = sensor_y

        beacon = beacon[21:]
        beacon_x, beacon_y = beacon.split(', ')
        beacon_x, beacon_y = int(beacon_x[2:]), int(beacon_y[2:])

        if beacon_x > max_x:
            max_x = beacon_x
        if beacon_y > max_y:
            max_y = beacon_y

        sensor = sensor_x, sensor_y
        beacon = beacon_x, beacon_y

        distance = manhattan_distance(sensor, beacon)
        if distance > max_distance:
            max_distance = distance

        pairs.append((sensor, beacon))
    
    max = max_x if max_x > max_y else max_y
    max += distance * 2

    for index in range(len(pairs)):
        pairs[index] = ((pairs[index][0][0], pairs[index][0][1]), 
                        (pairs[index][1][0], pairs[index][1][1]),
                        manhattan_distance((pairs[index][0][0], pairs[index][0][1]), 
                                            (pairs[index][1][0], pairs[index][1][1])))

    return pairs, max, max_y


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def in_boundaries(map, row, col):
    return row >= 0 and row < len(map) and col >= 0 and col < len(map[0])


def check_sensor(listing, point):
    #if point in [pair[1] for pair in listing]:
    #    return False
    #if point in [pair[0] for pair in listing]:
    #    return False

    for pair in listing:
        sensor, beacon, sensor_detection = pair
        
        sensor_distance = manhattan_distance(point, sensor)
        if sensor_distance <= sensor_detection:
            return True, pair

    return False, None


def count_nos(pairs, max_x, row):
    return sum(1 for col in range(-max_x, max_x) if check_sensor(pairs, (col, row)))


def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day15_input')
    else:
        in_lines = read_file('data/day15_sample')

    sensor_beacon, max, max_y = process_lines(in_lines)
    spots = count_nos(sensor_beacon, max, 2000000)
    return spots


# print(part_one(False))

def check_cols(sensor_list, sensor_max, row):
    # print(row)
    col = 0
    while col < sensor_max:
        result, pair = check_sensor(sensor_list, (col, row))
        if not result:
            return row + col * 4000000
        else:
            sensor_distance = pair[2]
            sensor_col = pair[0][0]
            sensor_row = pair[0][1]
            col = sensor_col + sensor_distance - abs(sensor_row - row) + 1


def log_result(val):
    if val is not None:
        print(val)

from multiprocessing import Pool
def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day15_input')
    else:
        in_lines = read_file('data/day15_sample')

    sensor_beacon, max, max_y = process_lines(in_lines)

    sensor_max = 4000000
    pool = Pool(processes=10)
    for row in range(sensor_max):
        pool.apply_async(check_cols, args=(sensor_beacon, sensor_max, row), callback=log_result)
        # check_cols(sensor_beacon, sensor_max, row)
    pool.close()
    pool.join()

if __name__ == "__main__":
    print(part_two(False))