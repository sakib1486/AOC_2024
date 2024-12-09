from part1 import part1
from part2 import part2
def main():
    fp = open('input.txt', 'r')
    input = fp.readlines()


    p1_ans = part1(input)
    p2_ans = part2(input)

    print(f"part 1 answer: {p1_ans}")
    print(f"part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()