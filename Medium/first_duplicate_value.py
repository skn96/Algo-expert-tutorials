# O(n) in time and O(n) in space
def firstDuplicateValue(array): 
    seen = set()
    for num in array: 
        if num in seen: 
            return num
        else: 
            seen.add(num)
    return -1

# O(n) in time and O(1) in space
# This only works id the numbers are in the range of 1 to n
# and the array is not empty
def firstDuplicateValue(array): 
    for i in range(len(array)): 
        index = abs(array[i]) - 1
        if array[index] < 0: 
            return abs(array[i])
        else: 
            array[index] = -array[index]
    return -1

array = [2, 1, 5, 3, 2, 3, 2]
print(f"The first duplicate value in the array is {firstDuplicateValue(array)}")
