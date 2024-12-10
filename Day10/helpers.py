# converts the list of strings to list of lists, stripping '\n'
def parse_input(input):
    return [list(map(int, line.strip())) for line in input]

# finds the trailhead position, that is indices of 0s
def trails(input):
    trailheads = set()
    for r, row in enumerate(input):
        for c, col in enumerate(row):
            if col == 0:
                trailheads.add((r,c ))
    
    return trailheads





