def moveElements(array, target): 
    left = 0 
    right = len(array) - 1

    while left < right:
        while left < right and array[right] == target: # left < right ... This is important !!!
            right -= 1

        if array[left] == target: 
            array[left], array[right] = array[right], array[left]

        left += 1
    
    return array

sample = [2, 1, 2, 2, 2, 3, 4, 2]
pushed_array = moveElements(sample, 2)
print(f"Pushed array: {pushed_array}\n")