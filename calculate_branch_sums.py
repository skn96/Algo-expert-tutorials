# This runs in O(n) in space and O(n) in time

from CreatingBST import *

def runningSums(tree, sums):
    sums = calculateRunningSums(tree, 0, sums)
    return sums

def calculateRunningSums(currentNode, runningSum, sums): 
    if currentNode is None: 
        return

    runningSum += currentNode.value

    if currentNode.left is None and currentNode.right is None: 
        sums.append(runningSum)
        return 
    
    calculateRunningSums(currentNode.left, runningSum, sums)
    calculateRunningSums(currentNode.right, runningSum, sums)


my_bst = BST()
nums = [10, 5, 15, 2, 5, 1, 13, 22, 14]
for num in nums: 
    my_bst.insert(num)

print_bst(my_bst.root)

sums = []
running_sum = runningSums(my_bst.root, sums)
print(f"Running sums: {sums}\n")
