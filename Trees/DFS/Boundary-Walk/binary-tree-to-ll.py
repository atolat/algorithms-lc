# 114. Flatten Binary Tree to Linked List
# Medium

# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs(node, pred):
            pred.left = node
            pred = node

            if node.left:
                pred = dfs(node.left, pred)

            if node.right:
                pred = dfs(node.right, pred)

            return pred

        sentinel = TreeNode('stub')
        dfs(root, sentinel)
        head = sentinel.left

        curr = head
        while curr:
            curr.right = curr.left
            curr.left = None
            curr = curr.right

        return head


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs(node):
            if node.left is None and node.right is None:
                return node
            leftTail, rightTail = None, None
            if node.left:
                leftTail = dfs(node.left)
            if node.right:
                rightTail = dfs(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail if rightTail else leftTail

        dfs(root)
