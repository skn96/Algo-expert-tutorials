# This will run in O(N log(N)) in time and O(1) in space
# Given an array of coins, return the least non-constructible change 
# that cannot be formed by the coins

def leastNonConstructibleChange(coins:list[int]) -> int:
    current_change = 0 
    coins.sort()
    for coin in coins: 
        print(f"Current change: {current_change}")
        print(f"Coin being considered: {coin}\n")
        if coin > current_change + 1: 
            return current_change + 1
        else: 
            current_change += coin 
    
    return current_change + 1
            
coins = [5, 7, 1, 1, 2, 3, 22]
non_cons = leastNonConstructibleChange(coins)
print(f"Least non constructible change: {non_cons}\n")