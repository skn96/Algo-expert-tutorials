# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7

# This runs in O(N) in time and O(N) in space

def spiralTraverse(array): 
    sr = 0 
    er = len(array) - 1
    sc = 0
    ec = len(array[0]) - 1
    result = []

    while sr <= er and sc <= ec: 

        for col in range(sc, ec + 1):
            result.append(array[sr][col])

        for row in range(sr+1,er+1):
            result.append(array[row][ec])

        for col in reversed(range(sc, ec)):
            result.append(array[er][col])
        
        for row in reversed(range(sr+1,er)):
            result.append(array[row][sc])

        sr += 1
        er -= 1
        sc += 1
        ec -= 1

    return result

# Do the recursive method

def spiralTraverseRecursive(array):
    result = []
    sr = 0
    er = len(array) - 1
    sc = 0
    ec = len(array[0]) - 1

    return spiralHelper(array, result, sr, er, sc, ec)

def spiralHelper(array, result, sr, er, sc, ec): 

    if sr > er or sc > ec: 
        return result

    while sr <= er and sc <= ec:

        for col in range(sc, ec + 1):
            result.append(array[sr][col])

        for row in range(sr + 1, er + 1):
            result.append(array[row][ec])

        for col in reversed(range(sc, ec)):
            result.append(array[er][col])

        for row in reversed(range(sr + 1, er)):
            result.append(array[row][sc])

        return spiralHelper(array, result, sr+1, er-1, sc+1, ec-1)


array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

result = spiralTraverseRecursive(array)
print(f"The traversed array is {result}")
