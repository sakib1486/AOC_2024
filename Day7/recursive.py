def rec_part1(input):
    count = 0
    for i in input:
        test_value, numbers = int(i.split(': ')[0]), [int(x) for x in i.split(': ')[1].split(' ')]
        if rec(numbers, test_value, 1, 1, numbers[0]):
            count += test_value
    
    return count

def rec_part2(input):
    count = 0
    for i in input:
        test_value, numbers = int(i.split(': ')[0]), [int(x) for x in i.split(': ')[1].split(' ')]
        if rec(numbers, test_value, 1, 2, numbers[0]):
            count += test_value
    
    return count

def rec(numbers, test_value, i, variation, current_v):
    if i >= len(numbers) and test_value == current_v:
        return True
    
    elif i >= len(numbers):
        return False
    
    elif variation==2:
        return rec(numbers, test_value, i+1, 2, current_v + numbers[i]) or rec(numbers, test_value, i+1, 2, current_v * numbers[i]) or rec(numbers, test_value, i+1, 2, int(str(current_v)+str(numbers[i])))
    elif variation==1:
        return rec(numbers, test_value, i+1, 1, current_v + numbers[i]) or rec(numbers, test_value, i+1, 1, current_v * numbers[i])
    else:
        return False
