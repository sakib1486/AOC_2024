def part2(input):
    rows, cols = len(input), len(input[0]) - 1
    count = 0

    def is_valid(x, y, CHAR):
        return 0 <= x < rows and 0 <= y < cols and input[x][y]==CHAR
    
    for i in range(rows):
        for j in range(cols):
            if input[i][j]=='A':
                # case 1
                if is_valid(i-1, j-1, 'M') and is_valid(i+1, j-1, 'M') and is_valid(i+1, j+1, 'S') and is_valid(i-1, j+1, 'S'):
                    count+=1
                # case 2
                elif is_valid(i-1, j-1, 'M') and is_valid(i+1, j-1, 'S') and is_valid(i+1, j+1, 'S') and is_valid(i-1, j+1, 'M'):
                    count+=1
                # case 3
                elif is_valid(i-1, j-1, 'S') and is_valid(i+1, j-1, 'S') and is_valid(i+1, j+1, 'M') and is_valid(i-1, j+1, 'M'):
                    count+=1
                # case 4
                elif is_valid(i-1, j-1, 'S') and is_valid(i+1, j-1, 'M') and is_valid(i+1, j+1, 'M') and is_valid(i-1, j+1, 'S'):
                    count+=1

    return count