import re
def part2(input):
  mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
  control_pattern = r"do\(\)|don't\(\)"
  total_sum = 0

  combined = f"{mul_pattern}|{control_pattern}"
  enabled = True
  for i in input: 
    tokens = re.finditer(combined, i)
    for token in tokens:
        if token.group(0) == "do()":
          enabled=True
        elif token.group(0) =="don't()":
          enabled=False
        else:
          if enabled:
            x,y = int(token.group(1)), int(token.group(2))
            total_sum += x*y

  return total_sum