class BST:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

# This runs in O(n) in time and O(n) in space
# def kthLargestValueBST(tree, k): 
#     result = []
#     inOrderTraverse(tree, result)
#     return result[len(result) - k]

# def inOrderTraverse(tree, result): 
#     if tree is None: 
#         return 
    
#     inOrderTraverse(tree.left, result)
#     result.append(tree.value)
#     inOrderTraverse(tree.right, result)

# A more efficient algorithm: 
# O(h + k) in time and O(h) in space 

class TreeInfo:
    def __init__(self, num_visits, last_visit): 
        self.num_visits = num_visits
        self.last_visit = last_visit

def kthLargestValueBST(tree, k): 
    tree_info = TreeInfo(0, None)

    reverseInorderTraverse(tree, tree_info, k)
    return tree_info.last_visit

def reverseInorderTraverse(tree, tree_info, k):
    if tree is None or tree_info.num_visits >= k:
        return 
    
    reverseInorderTraverse(tree.right, tree_info, k)
    if tree_info.num_visits < k:
        tree_info.num_visits += 1
        tree_info.last_visit = tree.value
        reverseInorderTraverse(tree.left, tree_info, k)

    

