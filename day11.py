from utilities import read_file

total_modulus = 1

class monkey():
    def __init__(self):
        pass
    
    def set_attrs(self, num, items, op_type, op_num, test, first_monkey, second_monkey):
        global total_modulus

        self.num = num
        self.items = items
        self.operation = op_type
        self.op_num = op_num
        self.test = test
        self.first = first_monkey
        self.second = second_monkey
        self.count = 0
        total_modulus *= self.test

    def monkey_around(self):
        global total_modulus

        while len(self.items) > 0:
            self.items[0] = self.inspect_item(self.items[0])

            # self.items[0] //= 3
            self.items[0] %= total_modulus
            if self.monkey_see_monkey_do(self.items[0]):
                self.throw_item(self.items[0], self.first)
            else:
                self.throw_item(self.items[0], self.second)

    def inspect_item(self, item):
        self.count += 1
        if self.operation == "*":
            item = item * self.op_num
        if self.operation == "square":
            item = item * item
        if self.operation == "+":
            item = item + self.op_num
        return item

    def monkey_see_monkey_do(self, item):
        return (item % self.test == 0)

    def throw_item(self, item, monkey):
        self.items.remove(item)
        monkey.items.append(item)

    def __str__(self):
        return f"{self.num}: {self.count}"


def process_lines(input_lines):
    index = 0
    monkeys = []
    for index in range((len(input_lines) + 1) // 7):
        monkeys.append(monkey())

    index = 0
    while index < len(input_lines):
        monk = int(input_lines[index].split(' ')[1][:-1])
        index += 1

        items = input_lines[index].split(':')[1].strip().split(',')
        items = [int(x.strip()) for x in items]
        index += 1

        operation = input_lines[index].split(':')[1].strip().split('=')[1].strip()
        if operation.count('old') == 2:
            op = "square"
            num = None
        elif '+' in operation:
            op = '+'
            num = int(operation.split(op)[1].strip())
        elif '*' in operation:
            op = '*'
            num = int(operation.split(op)[1].strip())
        index += 1

        test = int(input_lines[index].split(' ')[-1].strip())
        index += 1

        true = int(input_lines[index].split(' ')[-1].strip())
        index += 1

        false = int(input_lines[index].split(' ')[-1].strip())
        index += 2

        monkeys[monk].set_attrs(monk, items, op, num, test, monkeys[true], monkeys[false])

    return monkeys



def part_one(sample_file = True):
    if not sample_file:
        in_lines = read_file('data/day11_input')
    else:
        in_lines = read_file('data/day11_sample')

    monkeys = process_lines(in_lines)
    for x in range(10000):
        for monkas in monkeys:
            monkas.monkey_around()
        
        if x == 0 or x == 20 or x == 1000 or x == 9999:
            print(f"---{x}---")
            for monkas in monkeys:
                print(str(monkas))
    

print(part_one(False))