def part2(reports):
    def is_safe(report):
        n = len(report)
        if n<2:
            return True # single level is usually safe
        
        direction = None
        for i in range(1, n):
            diff = report[i] - report[i-1]

            if not(1<=abs(diff)<=3):
                return False
            if direction is None:
                direction = diff
            elif (direction > 0 and diff < 0) or (direction < 0 and diff > 0):
                return False
        return True
    
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