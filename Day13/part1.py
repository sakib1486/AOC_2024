#### ALTERNATIVE BRUTE FORCE SOLUTION, WHICH WILL RUN FOREVER FOR THE SECOND PART ####

'''
def extended_gcd(a, b):
    """Return (gcd, x, y) such that gcd = a * x + b * y."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def part1(machines):
    total_cost = 0
    max_presses = 100
    
    for machine in machines:
        A_X, A_Y = machine['A']
        B_X, B_Y = machine['B']
        P_X, P_Y = machine['prize']
        
        # Helper function to check if a Diophantine equation has a solution
        def has_solution(A, B, P):
            g, _, _ = extended_gcd(A, B)
            return P % g == 0

        # Check if there's a solution for the X and Y axes
        if not has_solution(A_X, B_X, P_X) or not has_solution(A_Y, B_Y, P_Y):
            continue  # No solution possible for this machine
        
        min_cost = float('inf')
        
        # Try all possible values for a (number of presses for A) within the limit
        for a in range(max_presses + 1):
            for b in range(max_presses + 1):
                # Check if this (a, b) satisfies both the X and Y constraints
                if a * A_X + b * B_X == P_X and a * A_Y + b * B_Y == P_Y:
                    # If the solution is valid, calculate the cost
                    cost = 3 * a + b
                    min_cost = min(min_cost, cost)
        
        # If we found a valid solution, add the cost to the total cost
        if min_cost != float('inf'):
            total_cost += min_cost

    return total_cost
'''

from helpers import *

def part1(machines):
    return solve(machines, 0) # offset 0 for part1