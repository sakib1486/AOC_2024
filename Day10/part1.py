from helpers import *

def visit_trails(input, r, c, visited):
    reachable = set()
    node_stack = [(r, c)]

    while node_stack:
        x, y = node_stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if input[x][y] == 9:
            reachable.add((x, y))
        
        # explore neighbour nodes
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[0]):  # Within bounds
                if input[nx][ny] == input[x][y] + 1: 
                    node_stack.append((nx, ny))

    return len(reachable)


def part1(input):
    trailheads = trails(input)
    score = 0

    for t in trailheads:
        visited = set()
        score += visit_trails(input, t[0], t[1], visited)

    return score
    
