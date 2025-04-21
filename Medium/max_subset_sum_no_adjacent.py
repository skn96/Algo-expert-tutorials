# This runs in O(n) in time and O(n) in space. 
def maxSubsetSumNoAdjacent(nums: list[int]) -> int:
    if not nums: 
        return -1
    elif len(nums) == 1: 
        return nums[0]
    
    maxSums = nums[:]
    maxSums[1] = max(nums[0], nums[1])

    current = 2
    prev = 1
    prev_prev = 0

    while current < len(maxSums):
        maxSums[current] = max(maxSums[prev_prev] + nums[current], maxSums[prev])
        prev += 1
        current += 1
        prev_prev += 1

    print(f"Max sums: {maxSums}")
    return maxSums[-1]

def maxSubsetSumNoAdjacentOptimal(nums:list[int]) -> int: 
    if not nums: 
        return -1 
    elif len(nums) == 1:
        return nums[0]
    # elif len(nums) == 2:
    #     return(max(nums[0], nums[1]))
    
    current_max = max(nums[0], nums[1])
    prev_max = nums[0]

    for i in range(2, len(nums)):
        temp = current_max
        current_max = max(nums[i] + prev_max, current_max)
        prev_max = temp
        print(f"Current max: {current_max}, Prev max: {prev_max}")

    return current_max



nums = [7, 10, 12, 7, 9, 14]
print(f"The max non-adjacent sum is {maxSubsetSumNoAdjacentOptimal(nums)}")




    
