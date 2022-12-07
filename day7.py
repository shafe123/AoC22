from utilities import read_file

class directory():
    def __init__(self, name, parent) -> None:
        self.name = name
        self.files = []
        self.subdirectories = {}
        self.parent = parent

    def add_file(self, name, size):
        self.files.append((name, size))

    def directory_exists(self, name):
        return name in self.subdirectories

    def add_subdirectory(self, name, subdirectory):
        self.subdirectories[name] = subdirectory

    def find_dir(self, name):
        if name in self.subdirectories:
            return self.subdirectories[name]
        
        return None

    def directory_size(self):
        size = 0

        for file in self.files:
            size += file[1]

        for name, sub in self.subdirectories.items():
            size += sub.directory_size()

        return size

    def get_sizes(self):
        results = []
        results.append((self.name, self.directory_size()))
        for name, sub in self.subdirectories.items():
            results.extend(sub.get_sizes())
        return results


    def __str__(self) -> str:
        result = ""
        result += f"{self.name}\n"
        for directory in self.subdirectories.values():
            result += f"{directory.name}\n"
            result += str(directory)
        for file in self.files:
            result += f"{file}\n"
        return result


def process_lines(input_lines):
    file_system = directory("/", None)
    current_dir = file_system
    count = 1
    while count < len(input_lines):
        line = input_lines[count]

        if "$ ls" in line:
            # get first listing after ls
            count += 1
            line = input_lines[count]        

            # process lines until we get back to the bash
            while "$" not in line and count < len(input_lines):
                line = input_lines[count]

                # handle directories
                if "dir" in line:
                    subdir_name = line.split(' ')[1]
                    if not current_dir.directory_exists(subdir_name):
                        current_dir.add_subdirectory(line.split(' ')[1], directory(subdir_name, current_dir))

                # handle files
                elif "$" not in line:
                    size, name = line.split(' ')
                    size = int(size)
                    current_dir.add_file(name, size)
                
                else:
                    count -= 2
                # go to next line
                count += 1
                
        
        elif "$ cd" in line:
            dir_name = line.split(' ')[2]
            if dir_name == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.find_dir(dir_name)

        count += 1

    return file_system




def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day7_input')
    else:
        in_lines = read_file('data/day7_sample')

    file_system = process_lines(in_lines)

    directory_sizes = file_system.get_sizes()

    total_size_sum = 0
    for name, size in directory_sizes:
        if size <= 100000:
            total_size_sum += size
    return total_size_sum

print(part_one(False))


def part_two(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day7_input')
    else:
        in_lines = read_file('data/day7_sample')

    file_system = process_lines(in_lines)

    space_remaining = 70000000 - file_system.directory_size()
    space_needed = 30000000 - space_remaining

    directory_sizes = file_system.get_sizes()

    smallest_name = ""
    smallest_necessary = 30000000
    for name, size in directory_sizes:
        if space_needed < size < smallest_necessary:
            smallest_necessary = size
            smallest_name = name

    return smallest_necessary


print(part_two(False))