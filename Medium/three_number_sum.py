def threeNumberSum(array, target): 
    array.sort()
    combinations = []
    for id in range(0,len(array) - 2): 
        #target_sum = target - array[id]
        left = id + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[id] + array[left] + array[right]
            if current_sum == target:
                combinations.append([array[id], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1

    return combinations

my_array = [12, 3, 1, 2, -6, 5, -8, 6]
print(f"The list of combinations is {threeNumberSum(my_array, 0)}\n")