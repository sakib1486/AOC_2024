from part1 import is_safe
def part2(reports):    
    def is_safe_dampener(report):
        if is_safe(report):
            return True
        
        for i in range(len(report)):
            modified = report[:i]+report[i+1:] # removing each level
            if is_safe(modified):
                return True
        return False
    
    count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_dampener(levels):
            count += 1
    return count