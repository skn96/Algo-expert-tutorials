def evaluateSmallestDifference(array1, array2):
    array1.sort()
    array2.sort()

    ptr1 = ptr2 = 0
    min_diff = float("inf")
    min_combo = []
    while ptr1 < len(array1) and ptr2 < len(array2): 
        difference = abs(array1[ptr1] - array2[ptr2])
        if difference == 0:
            return [array1[ptr1], array2[ptr2]]
        elif array1[ptr1] < array2[ptr2]:
            ptr1 += 1
        elif array1[ptr1] > array2[ptr2]: 
            ptr2 += 1

        if difference < min_diff: 
            min_combo = [array1[ptr1-1], array2[ptr2 - 1]]

    return min_combo
        
array1 = [-1, 3, 5, 10, 20, 28, 3]
array2 = [15, 17, 26, 134, 135]

min_pair = evaluateSmallestDifference(array1, array2)
print(f"The minimum combination is: {min_pair}\n")