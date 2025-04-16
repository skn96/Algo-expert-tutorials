def checkMonotonicity(array: list[int]) -> bool: 
    isNonIncreasing = True 
    isNonDecreasing = True 

    for i in range(1, len(array)): 
        if array[i] - array[i-1] > 0: 
            isNonIncreasing = False 
        if array[i] - array[i - 1] < 0:
            isNonDecreasing = False

    return isNonIncreasing or isNonDecreasing

array = [1,1,2,3,5,5,3]
mono = checkMonotonicity(array)
print(f"Is monotonic: {mono}\n")
