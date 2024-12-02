from part1 import part1
from part2 import part2

def main():
    fp = open('input.txt', 'r')

    a, b = [], []

    for line in fp.readlines():
        c1 = line.split()
        a.append(int(c1[0]))
        b.append(int(c1[1]))
    
    p1_ans = part1(a, b)
    p2_ans = part2(a, b)

    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()