def create_antenna_map(input, rows, cols):
    antennas = {}

    # figuring out same freq antenna locations
    for i in range(rows):
        for j in range(cols):
            if input[i][j] != '.':
                if input[i][j] not in antennas:
                    antennas[input[i][j]] = []
                antennas[input[i][j]].append((i, j))
    return antennas

def dist(x1, y1, x2, y2):
    return (x2-x1), (y2-y1)

def in_boundary(x, y, rows, cols):
    return (0 <= x < rows) and (0 <= y < cols)

def count_unique_antinodes(input, antenna_list, variation):
    antinodes = set()
    rows, cols = len(input), len(input[0])

    for i in range(len(antenna_list) - 1):
        x1, y1 = antenna_list[i]
        for j in range(i + 1, len(antenna_list)):
            x2, y2 = antenna_list[j]
            dx, dy = dist(x1, y1, x2, y2)
            step = 0
            while in_boundary(x2 + step * dx, y2 + step*dy, rows, cols):
                if variation == 1 and step == 1:
                    antinodes.add((x2 + step * dx, y2 + step * dy))
                    break

                else:
                    if variation == 2:
                        antinodes.add((x2 + step * dx, y2 + step *  dy))
                        step += 1
                    else:
                        step += 1
            
            step = 0
            while in_boundary(x1 - step * dx, y1 - step * dy, rows, cols):
                if variation == 1 and step == 1:
                    antinodes.add((x1 - step * dx, y1 - step * dy))
                    break

                else:
                    if variation == 2:
                        antinodes.add((x1 - step * dx, y1 - step * dy))
                        step += 1
                    else:
                        step += 1

    return antinodes


            