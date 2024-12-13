from part1 import part1
from part2 import part2

from helpers import *

def main():
    machines = parse_input()
    
    # part1
    p1_ans = part1(machines)
    # p1_ans = solve_claw_machines(machines)
    print(f"part 1 answer: {p1_ans}")

    p2_ans = part2(machines)
    print(f"part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()