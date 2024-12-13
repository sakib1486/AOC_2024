import re
from sympy import symbols, Eq, linsolve

def parse_input():
    machines = []
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    f.close()
    
    for i in range(0, len(lines), 4):
        # Use regular expressions to extract numbers
        a_match = re.search(r"X\+(\d+), Y\+(\d+)", lines[i])
        b_match = re.search(r"X\+(\d+), Y\+(\d+)", lines[i+1])
        prize_match = re.search(r"X=(\d+), Y=(\d+)", lines[i+2])
        
        if not (a_match and b_match and prize_match):
            raise ValueError("Invalid input format")
        
        # Convert matched groups to integers
        a_x, a_y = map(int, a_match.groups())
        b_x, b_y = map(int, b_match.groups())
        prize_x, prize_y = map(int, prize_match.groups())
        
        machines.append({'A': (a_x, a_y), 'B': (b_x, b_y), 'prize': (prize_x, prize_y)})
    
    return machines

def solve(machines, prize_offset):
    total_cost = 0

    for machine in machines:
        A_X, A_Y = machine['A']
        B_X, B_Y = machine['B']
        P_X, P_Y = machine['prize']

        # Adjust prize positions with offset
        P_X += prize_offset
        P_Y += prize_offset

        # Define variables and equations => eq1: Ax * a + Bx * b = Px; eq2: AY * a + By * b = Py;
        a, b = symbols('a b', integer=True, nonnegative=True)
        eq1 = Eq(A_X * a + B_X * b, P_X)
        eq2 = Eq(A_Y * a + B_Y * b, P_Y)

        # Solve with sympy linsolve
        solution = linsolve([eq1, eq2], (a, b))

        min_cost = float('inf')
        for sol in solution:
            a_val, b_val = sol

            if a_val.is_integer and b_val.is_integer:
                cost = 3 * a_val + b_val
                if cost < min_cost:
                    min_cost = cost

        
        if min_cost != float('inf'):
            total_cost += min_cost

    return total_cost