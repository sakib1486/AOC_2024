def part2(a, b):
    intersection = list(set(a).intersection(set(b)))

    # counting each similar items' occurrence
    s = {item: b.count(item) for item in intersection}

    result = sum(key*value for key, value in s.items())

    return result