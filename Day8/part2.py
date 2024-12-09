from helpers import *
def part2(input):
    count = set()
    rows, cols = len(input), len(input[0])
    antennas = {}

    antennas = create_antenna_map(input, rows, cols)

    for i in antennas:
        count = count.union(count_unique_antinodes(input, antennas[i], 2))
    return len(count)