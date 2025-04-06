# Calculate the sum of the node depths of the binary tree
# Time complexity = O(N), Space complexity = O(h), h is height of the binary tree
from CreatingBST import * 

def evaluateSumNodeDepths(tree):
    return evaluateNodeArray(tree, 0)

def evaluateNodeArray(currentNode, depth):

    if currentNode is None:
        return 0

    return depth + evaluateNodeArray(currentNode.left, depth + 1) + \
        evaluateNodeArray(currentNode.right, depth + 1)


my_bst = BST()
arr = [10, 5, 15, 2, 5, 1, 13, 22, 14]
for num in arr:
    my_bst.insert(num)

print_bst(my_bst.root)
mySum = evaluateSumNodeDepths(my_bst.root)
print(f"Sum of the depths of the BST is {mySum}\n")
