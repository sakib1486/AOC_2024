from helpers import *

def trails_rating(input, r, c, h):
    
    if input[r][c] != h:
        return 0
    if h == 9:
        return 1 # valid trail
        
    # explore neighbour nodes, and do recursive DFS
    distinct = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = r + dx, c + dy
        if 0 <= nx < len(input) and 0 <= ny < len(input[0]):  # Within bounds
            if input[nx][ny] == h + 1: # we can proceed to this
                distinct += trails_rating(input, nx, ny, h + 1)

    return distinct


def part2(input):
    trailheads = trails(input)
    rating = 0

    for t in trailheads:
        rating += trails_rating(input, t[0], t[1], h=0)

    return rating
