def in_boundary(x , y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def search(r, c, char):
        stack = [(r, c)]
        r = []
        while stack:
            x, y = stack.pop()
            if in_boundary(x, y, rows, cols) and not visited[x][y] and grid[x][y] == char:
                visited[x][y] = True
                r.append((x, y))
                for dx, dy in directions:
                    stack.append((x + dx, y + dy))
        return r
    
    regions = []
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region = search(r, c, grid[r][c])
                if region:
                    regions.append(region)
    return regions