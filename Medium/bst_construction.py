class BST: 
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

    def insert(self, value): 
        current_node = self 

        while True: 
            if value < current_node.value: 
                if current_node.left is None: 
                    current_node.left = BST(value)
                    break
                else: 
                    current_node = current_node.left 
            elif value >= current_node.value: 
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else: 
                    current_node = current_node.right
        return self


    def contains(self, value): 
        # This checks if the data is in a BST 
        current_node = self 
        while current_node is not None: 
            if current_node.value > value: 
                current_node = current_node.left 
            elif current_node.value < value: 
                current_node = current_node.right
            else:
                return True
        return False 
    
    def getMinValue(self): 
        # This gets the minimum value in the BST
        current_node = self 
        while current_node.left is not None: 
            current_node = current_node.left 
        return current_node.value   
         

    def remove(self, value, parentNode = None): 
        # This removes a node from the BST 
        current_node = self 
        while current_node is not None: 
            if value < current_node.value: 
                parentNode = current_node
                current_node = current_node.left 
            elif value > current_node.value: 
                parentNode = current_node
                current_node = current_node.right
            else: 
                # We found the node we want to remove
                if current_node.left is not None and current_node.right is not None: 
                    # If the node has two children, we need to find the smallest value in the right subtree
                    # and replace the value of the node we want to remove with that value
                    current_node.value = current_node.right.getMinValue()
                elif parentNode is None: 
                    # If the node is the root node and has only one child, we need to replace it with that child
                    if current_node.left is not None: 
                        self.value = current_node.left.value
                        self.right = current_node.right
                    else: 
                        self.value = current_node.right.value
                        self.left = current_node.left
                elif parentNode.left == current_node: 
                    # If the node is a left child, we need to replace it with its child
                    if current_node.left is not None: 
                        parentNode.left = current_node.left
                    else: 
                        parentNode.left = current_node.right
                elif parentNode.right == current_node: 
                    # If the node is a right child, we need to replace it with its child
                    if current_node.left is not None: 
                        parentNode.right = current_node.left
                    else: 
                        parentNode.right = current_node.right

                break

        return self
    
        


    