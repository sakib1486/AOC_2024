def part1(input):
    rows, cols = len(input), len(input[0])-1

    word = "XMAS"
    n = len(word)

    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)
    ]

    def is_valid(x, y, dx, dy):
        endx, endy = x + (n-1) * dx, y + (n-1) * dy
        if not (0 <= endx < rows and 0 <= endy < cols):
            return False

        return True
    
    def count_word_from(x, y, dx, dy):
        for i in range(n):
            nx, ny = x + i * dx, y + i * dy
            if input[nx][ny] != word[i]:
                return 0
        
        return 1
    
    count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy):
                    count += count_word_from(x, y, dx, dy)

    return count