from utilities import read_file


def process_input(instructions):
    operations = []
    for line in instructions:
        if line == "noop":
            operations.append(None)
        if "addx" in line:
            operations.append(None)
            operations.append(int(line.split(' ')[1]))
    return operations

def signal_strength(operations):
    register = 1
    signals = []
    counts = []
    registers = []
    for count, op in enumerate(operations):
        if (count + 1 - 20) % 40 == 0:
            signals.append((count + 1) * register)
            counts.append(count + 1)
            registers.append(register)

        if op is None:
            pass
        else:
            register += op
    
    return signals, counts, registers

def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day10_input')
    else:
        in_lines = read_file('data/day10_sample')

    ops = process_input(in_lines)
    signals, counts, registers = signal_strength(ops)
    print(signals)
    print(counts)
    print(registers)
    return sum(signals)

def draw_crt(operations):
    register = 1
    
    crt = []
    for row in range(6):
        current_crt = []
        for count, op in enumerate(operations[row * 40:(row+1)*40]):
            sprite = [register - 1, register, register + 1]
            if count in sprite:
                current_crt.append("#")
            else:
                current_crt.append(".")

            if op is None:
                pass
            else:
                register += op
        crt.append(current_crt)
    return crt
        

def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day10_input')
    else:
        in_lines = read_file('data/day10_sample')

    ops = process_input(in_lines)
    drawing = draw_crt(ops)
    for row in drawing:
        for char in row:
            print(char, end="")
        print()
    

part_two(False)
