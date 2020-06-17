# 623. Add One Row to Tree
# Medium

# Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

# The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

# Example 1:
# Input:
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5

# v = 1

# d = 2

# Output:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5

# Example 2:
# Input:
# A binary tree as following:
#       4
#      /
#     2
#    / \
#   3   1

# v = 1

# d = 3

# Output:
#       4
#      /
#     2
#    / \
#   1   1
#  /     \
# 3       1

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None

        q = deque([root])
        level = 0

        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        while q:
            numnodes = len(q)
            level += 1
            for _ in range(numnodes):
                node = q.popleft()
                if level == d - 1:
                    oldLeft = node.left
                    oldRight = node.right
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    node.left.left = oldLeft
                    node.right.right = oldRight

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
