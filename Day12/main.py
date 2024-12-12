from part1 import part1
from part2 import part2
from helpers import *
def main():
    fp = open('input.txt', 'r')
    input = fp.readlines()
    fp.close()

    grid = [list(x.strip()) for x in input]

    # part1
    p1_ans = part1(grid)
    print(f"part 1 answer: {p1_ans}")

    p2_ans = part2(grid)
    print(f"part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()