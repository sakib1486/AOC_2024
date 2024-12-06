def part2(grid):
    def in_boundary(x, y):
        return 0 <= x < rows and 0 <= y < cols

    rows, cols = len(grid), len(grid[0])
    guard_start = (0, 0)
    directions = {
        0: (-1, 0),  # Up
        1: (0, 1),   # Right
        2: (1, 0),   # Down
        3: (0, -1)   # Left
    }

    for i in range(rows):
        if '^' in grid[i]:
            guard_start = (i, grid[i].index('^'))
            break

    def causes_loop(obstacle_pos):
        visited_states = set()
        gp = guard_start
        guard = 0

        while True:
            state = (gp, guard)
            if state in visited_states:
                return True
            visited_states.add(state)


            nx, ny = gp[0] + directions[guard][0], gp[1] + directions[guard][1]

            if not in_boundary(nx, ny):
                return False

            if (nx, ny) == obstacle_pos or grid[nx][ny] == '#':
                guard = (guard + 1) % 4
            elif grid[nx][ny] == '.':
                gp = (nx, ny)
            else:
                gp = (nx, ny)

    loop_positions = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and (i, j) != guard_start:
                if causes_loop((i, j)):
                    loop_positions += 1

    return loop_positions
