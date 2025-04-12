def insertionSort(array: list) -> list: 
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array [j], array[j-1] = array[j-1], array[j]
            j -= 1 

    return array 

array = [-1, 4, 2, 0, 2, 12, 5]
sorted_array = insertionSort(array)
print(f"{array}")