from part1 import part1
from part2 import part2
from helpers import *
def main():
    fp = open('input.txt', 'r')
    input = fp.readlines()
    fp.close()

    numbers = input[0].strip().split()
    ns = [int(x) for x in numbers]

    # part1
    p1_ans = part1(ns, 25)
    print(f"part 1 answer: {p1_ans}")

    p2_ans = part2(ns, 75)
    print(f"part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()