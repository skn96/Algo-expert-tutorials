# Remove the duplicates in a linked list which has an attribute value
# which is sorted

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

def create_linked_list(values):
    if not values:
        return None  # Return None for empty list

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def removeDuplicatesLinkedList(Node):
    current_node = Node 
    while current_node is not None: 
        distinct_node = current_node.next
        while distinct_node is not None and current_node.value == distinct_node.value:
            distinct_node = distinct_node.next

        current_node.next = distinct_node
        current_node = distinct_node
    
    return Node

my_array = [1, 1, 3, 4, 4, 4, 5, 6, 6]
my_list = create_linked_list(my_array)

print_linked_list(my_list)

processed_list = removeDuplicatesLinkedList(my_list)
print_linked_list(processed_list)