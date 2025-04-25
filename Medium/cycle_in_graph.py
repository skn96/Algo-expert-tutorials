# We are given an adjacency list representing a graph
# We have to return a boolean representing if the graph has a cycle or not


# # This algorithm runs in O(v+e) in time and O(v) in space 
# def findCycle(edges): 
#     num_nodes = len(edges)
#     visited = [0 for _ in len(num_nodes)]
#     in_stack = [0 for _ in len(num_nodes)]

#     for node in range(num_nodes): 
#         if visited[node]:
#             continue

#         is_cycle = find_cycle(node, edges, visited, in_stack)

#     return is_cycle 

# def find_cycle(node, edges, visited, in_stack): 
#     visited[node] = 1
#     in_stack[node] = 1

#     neighbors = edges[node]

#     for neighbor in neighbors:
#         if not visited[neighbor]:
#             contains_cycle = find_cycle(neighbor, edges, visited, in_stack)
#             if contains_cycle: 
#                 return True 
#         elif in_stack[neighbor]:
#             return True 
       
#     in_stack[node] = 0
#     return False 

white, gray, black = 0, 1, 2
def findCycle(edges): 
    num_nodes = len(edges)
    colors = [0 for _ in range(len(num_nodes))]

    for node in range(num_nodes): 
        if colors[node] != white:
            continue

        contains_cycle = find_cycle_recursive(node, edges, colors)

    return contains_cycle

def find_cycle_recursive(node, edges, colors): 
    colors[node] = gray # This is a gray node 

    for neighbor in edges[node]: 
        
        if neighbor == gray: 
            return True 
        
        if neighbor != white: 
            continue 

        is_cycle = find_cycle_recursive(neighbor, edges, colors)
        if is_cycle:
            return True 
        
    colors[node] = black
    return False 





            

