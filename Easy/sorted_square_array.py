# Implement an algorithm to sort the squares of a sorted array
# Only works if the input array is sorted
# O(n) in space and time

def sortedSquareArray(arr:int) -> list[int]:
    st_ptr = 0
    end_ptr = len(arr) - 1
    sorted_square = [0 for i in range(0,len(arr))]

    counter = end_ptr
    while st_ptr != end_ptr: 
        if abs(arr[st_ptr]) <= abs(arr[end_ptr]): 
            sorted_square[counter] = arr[end_ptr]**2
            end_ptr -=1 
        else: 
            sorted_square[counter] = arr[st_ptr]**2
            st_ptr += 1
        
        counter -= 1

    sorted_square[counter] = arr[st_ptr]**2

    return sorted_square

array = [-4, -3, -2, 0, 2, 3, 4, 5]
print(f"{sortedSquareArray(array)}\n")