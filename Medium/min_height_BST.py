class BST:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else: 
            if self.right is None: 
                self.right = BST(value)
            else: 
                self.right.insert(value)


# O(nlogn) in time and O(n) in space
# def minHeightTree1(array):
#     return minHeightTree1_Helper(array, None, 0, len(array) - 1)

# def minHeightTree1_Helper(nums, bst, ib, ie):
#     if ie < ib:
#         return

#     mid = (ie + ib)//2
#     value_to_add = nums[mid]

#     if bst is None:
#         bst = BST(value_to_add)
#     else:
#         bst.insert(value_to_add)

#     minHeightTree1_Helper(nums, bst, ib, mid - 1)
#     minHeightTree1_Helper(nums, bst, mid + 1, ie)

#     return bst

# O(n) in time and O(n) in space
# def minHeightTree2(array):
#     return minHeightTree2_Helper(array, None, 0, len(array) - 1)

# def minHeightTree2_Helper(nums, bst, ib, ie):
#     if ie < ib:
#         return

#     mid = (ie + ib) // 2
#     value_to_add = nums[mid]
#     new_node = BST(value_to_add)

#     if bst is None:
#         bst = new_node
#     else:
#         if value_to_add < bst.value:
#             bst.left = new_node
#             bst = bst.left 
#         else: 
#             bst.right = new_node 
#             bst = bst.right 

#     minHeightTree2_Helper(nums, bst, ib, mid - 1)
#     minHeightTree2_Helper(nums, bst, mid + 1, ie)

#     return bst


# A much cleaner code
# O(n) in time and O(n) in space
def minHeightTree3(array):
    return minHeightTree3_Helper(array, 0, len(array) - 1)


def minHeightTree3_Helper(nums, ib, ie):
    if ie < ib:
        return

    mid = (ie + ib) // 2
    value_to_add = nums[mid]
    bst = BST(value_to_add)
    bst.left = minHeightTree3_Helper(nums, ib, mid - 1)
    bst.right = minHeightTree3_Helper(nums, mid +1, ie)

    return bst


array = [1, 2, 5, 7, 10, 13 ,14, 15, 22]
