class Node: 
    def __init__(self, value, ancestor):
        self.value = value 
        self.ancestor = ancestor

def youngestCommonAncestor(the_great_one, child_1, child_2): 
    height_child_1 = 0 
    height_child_2 = 0

    current_ancestor_1 = child_1.ancestor
    current_ancestor_2 = child_2.ancestor

    while current_ancestor_1 is not the_great_one:
        height_child_1 += 1
        current_ancestor_1 = current_ancestor_1.ancestor

    while current_ancestor_2 is not the_great_one:
        height_child_2 += 1
        current_ancestor_2 = current_ancestor_2.ancestor
    
    if height_child_2 != height_child_1:
        if height_child_2 > height_child_1:
            height_diff = height_child_2 - height_child_1
            current_node_2 = child_2
            current_node_1 = child_1
        elif height_child_1 > height_child_2:
            height_diff = height_child_1 - height_child_2
            current_node_2 = child_1
            current_node_1 = child_2
        for i in range(height_diff):
            current_node_2 = current_node_2.ancestor
    else:
        current_node_1 = child_1
        current_node_2 = child_2

    while current_node_2.ancestor is not current_node_1.ancestor:
        current_node_2 = current_node_2.ancestor
        current_node_1 = current_node_1.ancestor

    return current_node_1.ancestor
