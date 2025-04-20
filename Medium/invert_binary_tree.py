class node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

# O(n) in time and O(n) in space: iterative procedure
def invertBinaryTree(tree):
    queue = [tree]
    while queue:
        current_node = queue.pop(0)
        if current_node is None:
            continue
        swapNodes(current_node)
        queue.append(current_node.left)
        queue.append(current_node.right)

# O(n) in time and O(h) in space 
def invertBinaryTreeRecursive(tree): 
    if tree is None:
        return 
    swapNodes(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapNodes(tree):
    tree.left, tree.right = tree.right, tree.left 