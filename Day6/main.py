from part1 import part1
from part2 import part2

def main():
    fp = open('input.txt', 'r')
    input = fp.readlines()
    grid = [list(x.strip('\n')) for x in input]
    fp.close()

    p1_ans = part1(grid)
    p2_ans = part2(grid)

    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")
    

if __name__=="__main__":
    main()