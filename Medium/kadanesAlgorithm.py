# This runs in O(1) in space and O(n) in time 
def kadanesAlgorithm(nums: list[int]) -> int: 
    # To find the maximum sum that can be obtained when we slice the 
    # algorithm at two given indices

    maxSoFar = currentMax = float("-inf")

    for i in range(len(nums)): 
        currentMax = max(currentMax + nums[i], nums[i])
        maxSoFar = max(maxSoFar, currentMax)

    return maxSoFar

my_array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(f"The maximum value by cutting a slice through the kadanes algorithm is given by {kadanesAlgorithm(my_array)}")