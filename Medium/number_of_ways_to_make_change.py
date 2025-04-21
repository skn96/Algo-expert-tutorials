def numWaysDenom(denoms: list[int], target: int) -> int: 
    ways = [0 for i in range(target + 1)]
    ways[0] = 1

    for denom in denoms: 
        for amount in range(1, target + 1):
            if denom <= amount:
                ways[amount] += ways [amount - denom]
    
    return ways[target]

num_ways = numWaysDenom([1, 5, 10, 25], 10)
print(f"Number of ways to make change is {num_ways}\n")