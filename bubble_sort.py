# Bubble sort:
# O(N^2) in time and O(1) in space

def bubbleSort(array:list)->list:
    isSorted = False 
    counter = 0
    while not isSorted: 
        isSorted = True 
        for i in range(0, len(array) - 1 - counter): 
            if array[i+1] < array[i]:
                swap(array, i, i+1)
                isSorted = False
        counter += 1 
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

array = [24, 11, 3, 21, 16]
sorted_array = bubbleSort(array)
print(f"{array}\n")

