from functools import cmp_to_key

def part2(rules, printed):
    total_sum = 0
    def comparator(x, y):
        for a, b in rules:
            if x == a and y ==b:
                return -1
            if x == b and y == a:
                return 1
        return 0

    for l in printed:
        flag = True
        for i in range(len(l) - 1):
            for j in range(i+1, len(l)):
                if(l[j], l[i]) in rules:
                    flag = False
                    break
            
        if not flag:
            sorted_update = sorted(l, key=cmp_to_key(comparator))
            total_sum += sorted_update[len(sorted_update) // 2]

    return total_sum