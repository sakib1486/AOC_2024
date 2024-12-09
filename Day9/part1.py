from helpers import *

def part1(input):
    file_blocks, empty_blocks = create_blocks(input)
    disk = []

    rehash(disk, file_blocks, empty_blocks)

    # index of dots
    dots = dot_indices(disk, '.')

    #remap
    remap1(disk, dots)

    return checksum(disk)
    
