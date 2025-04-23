def minNumberOfCoins(denoms:list[int], target:int) -> int:
    amounts = [float("inf") for i in range(target + 1)]
    amounts[0] = 0
    for denom in denoms: 
        for i in range(1, len(amounts)):
            if denom  <= amounts[i]:
                amounts[i] = min(amounts[i], 1 + amounts[i - denom])
    
    return amounts[target] if amounts[target] != float("inf") else -1