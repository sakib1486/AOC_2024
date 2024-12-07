def in_boundary(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def part1(grid):
    rows, cols = len(grid), len(grid[0])
    gp = (0, 0)
    guard = 0

    directions = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    # Guard position
    for i in range(rows):
        if '^' in grid[i]:
            gp = (i, grid[i].index('^'))
            break
    
    count = 1
    visited = set()
    visited.add(gp)

    while True:
        nx, ny = gp[0] + directions[guard][0], gp[1] + directions[guard][1]

        if not in_boundary(nx, ny, rows, cols):
            return count
        
        if grid[nx][ny] == '.':
            gp = (nx, ny)
            if gp not in visited:
                visited.add(gp)
                count += 1
        elif grid[nx][ny] == '#':
            guard = (guard + 1) % 4
        else:
            gp = (nx, ny)