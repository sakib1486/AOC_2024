# parses input string and create blocks of files and empty space
def create_blocks(input):
    file_blocks = []
    empty_blocks = []
    id = 0

    for i, c in enumerate(input):
        if i%2 == 0:
            file_blocks.append([str(id)] * int(c))
            id += 1
        else:
            empty_blocks.append(['.'] * int(c))
    
    return file_blocks, empty_blocks

# create disk map from file_blocks and empty_blocks
def rehash(disk, file_blocks, empty_blocks):
    for i in range(len(file_blocks)-1):
        disk += (file_blocks[i] + empty_blocks[i])
    disk += file_blocks[len(file_blocks) - 1]

# finds all indices of dots in the initial disk map for PART 1
def dot_indices(lst, element):
    return list(filter(lambda x: lst[x] == element, range(len(lst))))

# returns checksum
def checksum(disk):
    return sum(int(num) * index for index, num in enumerate(disk) if num != '.')

# part1 remapping
def remap1(disk, dots):
    pos, l = 0, len(disk)-1

    while dots[pos]<l:
        if disk[l] != '.':
            disk[dots[pos]] = disk[l]
            disk[l] = '.'
            pos += 1
            l -= 1
        else:
            l -= 1

# part2 remapping
def remap2(file_blocks, empty_blocks):
    for n in range(len(file_blocks)-1, -1, -1):
        l = len(file_blocks[n])
        for i in range(0, n):
            if empty_blocks[i].count('.') >= l:
                e = empty_blocks[i].index('.')
                empty_blocks[i][e:e+l] = file_blocks[n]
                file_blocks[n][0:] = ['.']*len(file_blocks[n])
                break

