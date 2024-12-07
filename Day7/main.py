from part1 import part1
from part2 import part2
from recursive import rec_part1, rec_part2

def main():
    fp = open('input.txt', 'r')
    input = fp.readlines()
    fp.close()

    # ITERTOOLS
    print("Creating operator sequences to solve....")
    p1_ans = part1(input)
    print(f"Part 1 answer: {p1_ans}")
    p2_ans = part2(input)
    print(f"Part 2 answer: {p2_ans}")

    # RECURSION
    print("Solving recursively.......")
    p1_ans = rec_part1(input)
    print(f"Part 1 answer: {p1_ans}")
    p1_ans = rec_part2(input)
    print(f"Part 2 answer: {p2_ans}")   

if __name__=="__main__":
    main()