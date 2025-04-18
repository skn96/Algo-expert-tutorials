# O(n) in time and O(d) in space
def validateTree(tree):
    return validateTreeHelper(tree, float("-inf"), float("+inf"))

def validateTreeHelper(node, min_val, max_val): 

    if node.left is None and node.right is None:
        return True
    
    if node.left <= min_val and node.right > max_val:
        return False
    
    leftIsValid = validateTreeHelper(node.left, min_val, node.value)

    return leftIsValid and validateTreeHelper(node.right, node.value, max_val)

