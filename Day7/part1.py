from itertools import product
def calculate(numbers, ops):
    result =numbers[0]
    for i in range(1, len(numbers)):
        if ops[i-1] == '+':
            result += numbers[i]
        elif ops[i-1] == '*':
            result *= numbers[i]
        else:
            result = int(str(result) + str(numbers[i]))
    return result

def verify(op_string, numbers, test):
    ops = product(op_string, repeat=len(numbers)-1)

    for o in ops:
        if calculate(numbers, o) == test:
            return True
    return False

def part1(input):
    count = 0
    for i in input:
        test_value, numbers = int(i.split(': ')[0]), [int(x) for x in i.split(': ')[1].split(' ')]

        if verify('+*', numbers, test_value):
            count += test_value
    return count