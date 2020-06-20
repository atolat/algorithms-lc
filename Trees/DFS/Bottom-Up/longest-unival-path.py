# 687. Longest Univalue Path
# Easy

# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# The length of path between two nodes is represented by the number of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2


# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        globalcount = [0]

        def dfs(node):
            height, diameter = 0, 0
            if node.left:
                hL = dfs(node.left)
                if node.val == node.left.val:
                    height = max(height, hL + 1)
                    diameter = height

            if node.right:
                hR = dfs(node.right)
                if node.val == node.right.val:
                    height = max(hR + 1, height)
                    diameter += hR + 1

            globalcount[0] = max(globalcount[0], diameter)
            return height

        dfs(root)
        return globalcount[0]
