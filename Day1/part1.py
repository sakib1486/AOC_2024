def part1(a, b):
    a.sort()
    b.sort()

    abs_diff = [abs(a - b) for a, b in zip(a, b)]

    return sum(abs_diff)
