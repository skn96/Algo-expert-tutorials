# Runs in O(N^2) in time and O(1) in space
def selectionSort(array:list)->list:
    currentIdx = 0 # id of the unsorted array 
    while currentIdx < len(array) - 1: 
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)): 
            if array[i] < array[smallestIdx]:
                smallestIdx = i 
        swap(array, smallestIdx, currentIdx)
        currentIdx += 1

    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

array = [-1, 4, 2, 0, 2, 12, 5]
sorted_array = selectionSort(array)
print(f"{array}")
