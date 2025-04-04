# Using a double for loop O(n^2) T, O(1) S
# def two_sum(arr, target_value):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target_value:
#                 return [arr[i], arr[j]]
#     return []

# Use a hash table O(N) in time, O(N) in space 
def two_sum(arr, target_value):
    nums = {}
    for num in range(0, len(arr)): 
        potential_match = target_value - arr[num]
        if potential_match in nums.keys():
            return [potential_match, arr[num]]
        else:
            nums[num] = True
    return []
            
# Using two pointers with O(NlogN) in time, with time-sort and O(1) in Space 
# def two_sum(arr, target_value):
#     first = 0 
#     last = len(arr) - 1
#     arr.sort()
#     while first < last:
#         if arr[first] + arr[last] == target_value:
#             return [arr[first], arr[last]]
#         elif arr[first] + arr[last] < target_value:
#             first += 1
#         elif arr[first] + arr[last] > target_value:
#             last -= 1
#     return []

array = [-1, 2, 3, 4, 5, 7]
target = 5

print(f"{two_sum(array,target)}")
