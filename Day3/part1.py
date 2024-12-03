import re
def part1(input):
    mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    total_sum = 0

    for i in input:
        matches = re.findall(mul_pattern, i)
        total_sum += sum(int(x)*int(y) for x, y in matches)
    return total_sum