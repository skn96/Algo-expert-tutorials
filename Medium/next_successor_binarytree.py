# This is the binary tree class that we have been given 
class binaryTree:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left 
        self.right = right
        self.parent = parent

# # 1st solution: O(n) in time and O(n) in space 
# def nextSuccessor(tree, target):
#     result = []
#     inOrderTraversal(tree, result)
#     for i, val in enumerate(result): 
#         if val == target:
#             break 
#     if i == len(result) - 1:
#         return None 
#     return i + 1

# def inOrderTraversal(tree, result):
#     if tree is None:
#         return 
    
#     inOrderTraversal(tree.left, result)
#     result.append(tree.val)
#     inOrderTraversal(tree.right, result)

# Solution number 2 (Much more efficient)
# O(h) in time and O(1) in space 
def nextSuccessor(tree, node): 
    if node.right is not None: 
        return findLeftMostRightChild(node)
    else:
        return findRightMostParent(node)
    
def findLeftMostRightChild(node):
    currentNode = node.right 
    while currentNode is not None:
        currentNode = currentNode.left     
    return currentNode.parent
        

def findRightMostParent(node):
    current_node = node
    while current_node.parent is not None and current_node.parent.right == current_node:
        current_node = current_node.parent 

    return current_node.parent






