from part1 import part1
from part2 import part2

def main():
    fp = open('rules.txt', 'r')

    input = fp.readlines()

    rules = [(int(x), int(y)) for x, y in [x.split('|') for x in input]]
    fp.close()

    fp = open('prints.txt', 'r')
    input = fp.readlines()
    printed = [[int(value) for value in s.split(",")] for s in input]
    fp.close()
    
    p1_ans = part1(rules, printed)
    p2_ans = part2(rules, printed)

    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()