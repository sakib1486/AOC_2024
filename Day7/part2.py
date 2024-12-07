from part1 import *

def part2(input):
    count = 0
    for i in input:
        test_value, numbers = int(i.split(': ')[0]), [int(x) for x in i.split(': ')[1].split(' ')]

        if verify("+|*", numbers, test_value):
            count += test_value

    return count
