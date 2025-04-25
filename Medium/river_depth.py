def riverDepth(matrix):
    sizes = []
    visited = [[False for element in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,sizes,visited)

    return sizes

def traverseNode(i, j, matrix, sizes, visited):
    current_river_size = 0
    nodes_to_explore = [[i,j]]
    while nodes_to_explore:
        currentNode = nodes_to_explore.pop()
        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j]: 
            continue 
        visited[i][j] = True 
        if matrix[i][j] == 0:
            continue 
        current_river_size += 1
        unvisited_neighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)
    if current_river_size > 0:
        sizes.append(current_river_size)

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisited_neighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisited_neighbors.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisited_neighbors.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisited_neighbors.append([i,j-1])
    if j < len(matrix[0]) - 1 and not visited[i, j+1]:
        unvisited_neighbors.append([i,j+1])
    
    return unvisited_neighbors


