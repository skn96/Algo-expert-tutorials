class Tree: 
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right 

class TreeInfo: 
    def __init__(self, height, is_balanced):
        self.height = height 
        self.is_balanced = is_balanced

def heightBalanced(root):
    return getTreeInfo(root).is_balanced

def getTreeInfo(node):
    if node is None:
        return TreeInfo(-1, True)
    
    left_tree_info = getTreeInfo(node.left)
    right_tree_info = getTreeInfo(node.right)

    current_height = max(left_tree_info.height, right_tree_info.height) + 1
    is_balanced = (left_tree_info.is_balanced and 
                   right_tree_info.is_balanced and 
                   abs(left_tree_info.height - right_tree_info.height) <= 1)
    
    return TreeInfo(current_height, is_balanced)    
    

    


