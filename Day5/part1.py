def part1(rules, printed):
    total_sum = 0

    for l in printed:
        flag = True
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                if (l[j], l[i]) in rules:
                    flag = False
                    break
            if not flag:
                break
        
        if flag:
            total_sum += l[len(l) // 2]

    return total_sum