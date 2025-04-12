# Using a recursive algorithm
def binarySearch(array, target): 
    return binarySearchHelper(array, target, 0, len(array) - 1)

# O(log(N)) time complexity and O(log(N)) space complexity : Recursive algorithm 
def binarySearchHelper2(array, target, left, right):
    if left > right: 
        return -1 

    middle = (left + right) // 2
    potential = array[middle]
    if potential == target:
        return middle
    elif potential > target:
        return binarySearchHelper2(array, target, left, middle - 1)
    elif potential < target:
        return binarySearchHelper2(array, target, middle + 1, right)


# O(log(N)) time complexity and O(1) in space complexity : Iterative algorithm 
def binarySearchHelper(array, target, left, right):

    while left <= right:
        middle = (left + right) // 2
        potential = array[middle]
        print(f"middle: {middle}   potential: {potential}")
        if potential == target:
            return middle
        elif potential > target:
            right = middle - 1 
        elif potential < target:
            left = middle + 1

array = [-11, 2, 4, 15, 22, 31, 35, 47, 51]
target = 15

location = binarySearch(array, target)
print(f"The location of the target was found at {location}\n")
