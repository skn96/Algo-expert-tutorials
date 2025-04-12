from CreatingBST import *

def findClosestValueBST(target, tree): 
    closest = findClosestValueHelperBST_Iterative(target, tree, float("inf"))
    return closest

def findClosestValueHelperBST(target, tree, closest):

    # (1) End condition
    if tree is None:
        return closest 

    # (2) Update the closest? (Check if the current diff of tree.value, target is greater than
    # the difference between the current closest and the target, based on that update)
    print(f"Tree value: {tree.value}, target value: {target}")
    print(f"Tree value - target: {tree.value - target}")
    print(f"Closest - target: {closest - target}")
    if abs(tree.value - target) < abs(closest - target): 
        closest = tree.value

    print(f"Closest set to: {closest}\n")

    # (3) Check which is the next tree to be considered (left or right) based on the
    # fact that tree.value < or > target and call the function recursively
    if tree.value < target: 
        return findClosestValueHelperBST(target, tree.right, closest)
    elif tree.value > target: 
        return findClosestValueHelperBST(target, tree.left, closest)
    else: 
        return closest


## Doing it iteratively
def findClosestValueHelperBST_Iterative(target, tree, closest):

    currentNode = tree

    while currentNode is not None: 

        if abs(currentNode.value - target) < abs(closest - target):
            closest = currentNode.value

        if currentNode.value < target:
            currentNode = currentNode.right
        elif currentNode.value > target:
            currentNode = currentNode.left
        else:
            break
    
    return closest


my_bst = BST()
for num in [10, 5, 15, 2, 5, 1, 13, 22, 14]:
    my_bst.insert(num)

target = 12

closest_value = findClosestValueBST(target, my_bst.root)
print_bst(my_bst.root)
print(f"The closest value in the tree to the target is : {closest_value}\n")
