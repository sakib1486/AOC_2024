from helpers import *

def part2(input):
    regions = find_regions(input)
    d = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    cost = 0

    for r in regions:
        area = len(r)
        corners = 0
        
        for (x, y) in r:
            # Possible Perpendicular neighbours
            adjacent = [
                (x + d["up"][0], y + d["up"][1]),
                (x + d["down"][0], y + d["down"][1]),
                (x + d["left"][0], y + d["left"][1]),
                (x + d["right"][0], y + d["right"][1]),
            ]
            
            # Perpendicular neighbors
            if adjacent[0] not in r and adjacent[3] not in r:  # Top-Right
                corners += 1
            if adjacent[0] not in r and adjacent[2] not in r:  # Top-Left
                corners += 1
            if adjacent[1] not in r and adjacent[3] not in r:  # Bottom-Right
                corners += 1
            if adjacent[1] not in r and adjacent[2] not in r:  # Bottom-Left
                corners += 1

            # Inner corners
            if adjacent[0] in r and adjacent[3] in r and (x - 1, y + 1) not in r:
                corners += 1  # Inner Top-Right
            if adjacent[0] in r and adjacent[2] in r and (x - 1, y - 1) not in r:
                corners += 1  # Inner Top-Left
            if adjacent[1] in r and adjacent[3] in r and (x + 1, y + 1) not in r:
                corners += 1  # Inner Bottom-Right
            if adjacent[1] in r and adjacent[2] in r and (x + 1, y - 1) not in r:
                corners += 1  # Inner Bottom-Left

        #print(f"Area: {area}, Corners: {corners}, Cost: {area * corners}")
        cost += area * corners

    return cost
