def count_stone(input, n):
    stones = {x: input.count(x) for x in input}

    for _ in range(n):
        new_stones = {}

        for stone, c in stones.items():
            if stone == 0:
                if 1 in new_stones:
                    new_stones[1] += c
                else:
                    new_stones[1] = c

            elif len(str(stone)) % 2 == 0: 
                m = len(str(stone)) // 2
                l = int(str(stone)[:m]) if str(stone)[:m] else 0
                r = int(str(stone)[m:]) if str(stone)[m:] else 0
                if l in new_stones:
                    new_stones[l] += c
                else:
                    new_stones[l] = c
                
                if r in new_stones:
                    new_stones[r] += c
                else:
                    new_stones[r] = c
            
            else:
                if stone*2024 in new_stones:
                    new_stones[stone*2024] += c
                else:
                    new_stones[stone*2024] = c
        stones = new_stones

    return sum(stones.values())