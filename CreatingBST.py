# Creating a BST from a list of integers
import math
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value >= current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # If value == current.value, do nothing (no duplicates)

    def in_order_traversal(self):
        """Return the BST elements in sorted order."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current, result):
        if current is not None:
            self._in_order_recursive(current.left, result)
            result.append(current.value)
            self._in_order_recursive(current.right, result)


def print_bst(root):
    """Pretty-print a binary tree with connecting branches."""
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)


def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    if node is None:
        return [], 0, 0, 0

    # No child.
    if node.right is None and node.left is None:
        line = str(node.value)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.value)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.value)
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = str(node.value)
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [" " * n] * (q - p)
    elif q < p:
        right += [" " * m] * (p - q)
    zipped_lines = zip(left, right)
    lines = [a + u * " " + b for a, b in zipped_lines]
    return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2
