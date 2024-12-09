from helpers import *

def part2(input):
    file_blocks, empty_blocks = create_blocks(input)
    remap2(file_blocks, empty_blocks)

    disk = []

    rehash(disk, file_blocks, empty_blocks)

    return checksum(disk)

