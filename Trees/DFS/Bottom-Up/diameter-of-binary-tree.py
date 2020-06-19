# 543. Diameter of Binary Tree
# Easy

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        globaldiameter = [0]
        if not root:
            return 0

        def dfs(node):
            if node.left is None and node.right is None:
                pass

            height = 0
            diameter = 0

            if node.left:
                heightL = 1 + dfs(node.left)
                height = max(height, heightL)
                diameter = height

            if node.right:
                heightR = 1 + dfs(node.right)
                height = max(height, heightR)
                diameter += heightR

            globaldiameter[0] = max(globaldiameter[0], diameter)
            return height

        dfs(root)
        return globaldiameter[0]