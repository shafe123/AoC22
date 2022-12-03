def read_file(input_file):
    result = []
    with open(input_file) as in_file:
        for line in in_file:
            result.append(line.strip())

    return result