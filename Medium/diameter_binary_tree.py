class binaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right 

class treeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height 

def treeDiameter(tree):
    tree_info = treeInfo(0, 0)
    return treeDiameter_helper(tree).diameter

def treeDiameter_helper(tree):
    if tree is None:
        return treeInfo(0,0)
    
    left_tree_info = treeDiameter_helper(tree.left)
    right_tree_info = treeDiameter_helper(tree.right)

    current_diameter = max(left_tree_info.diameter, right_tree_info.diameter, left_tree_info.height + right_tree_info.height)
    current_height = max(left_tree_info.height, right_tree_info.height) + 1

    return treeInfo(current_diameter, current_height)