from helpers import *

def part1(input):
    regions = find_regions(input)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cost = 0
    
    for r in regions:
        area = len(r)
        peri = 0
        for (x, y) in r:
            i = 4
            for dx, dy in directions:
                if (x + dx, y + dy) in r:
                    i -= 1
            peri += i
        cost += (area * peri)


    return cost
    
