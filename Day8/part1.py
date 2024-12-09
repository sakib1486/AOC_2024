from helpers import *
def part1(input):
    count = set()
    rows, cols = len(input), len(input[0])
    
    antennas = create_antenna_map(input, rows, cols)
    
    for i in antennas:
        count = count.union(count_unique_antinodes(input, antennas[i], 1))
    return len(count)