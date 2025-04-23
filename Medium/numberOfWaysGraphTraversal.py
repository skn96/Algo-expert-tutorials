# O(2^(n+m) in time and O(n+m) in space) - Not very optimal
def graphTraversal(width, height):
    if width == 1 or height == 1:
        return 1
    
    return graphTraversal(width-1, height) + graphTraversal(width, height-1)

# O(n*m) in time and O(n*m) in space
def graphTraversalDynamic(width, height): 

    def print_2d_array(array):
        for row in array:
            print(row)

    traversed = [[1 for x in range(width)] for y in range(height)]
    # print_2d_array(traversed)
    for y in range(height):
        traversed[y][0] = traversed[y-1][0] 

    for j in range(1, height):
        for i in range(1, width): 
            traversed[j][i] = traversed[j][i-1] + traversed[j-1][i]
    print_2d_array(traversed)

    return traversed[-1][-1]


graphTraversalDynamic(4, 3)
