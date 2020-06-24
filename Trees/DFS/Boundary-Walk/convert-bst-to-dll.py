# 426. Convert Binary Search Tree to Sorted Doubly Linked List
# Medium

# 883

# 89

# Add to List

# Share
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        def dfs(node, pred):

            if node.left:
                pred = dfs(node.left, pred)

            pred.right = node
            node.left = pred
            pred = node

            if node.right:
                pred = dfs(node.right, pred)

            return pred

        sentinel = Node('stub')
        tail = dfs(root, sentinel)
        head = sentinel.right
        head.left = tail
        tail.right = head
        return head
