# 563. Binary Tree Tilt
# Easy

# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Bottom up DFS
        global_tilt = [0]

        def dfs(node):
            # Each node returns the sum of it's left and right subtrees
            if node.left is None and node.right is None:
                return node.val

            leftsum, rightsum, mytilt = 0, 0, 0
            if node.left is not None:
                leftsum = dfs(node.left)
            if node.right is not None:
                rightsum = dfs(node.right)

            mytilt = abs(leftsum-rightsum)

            global_tilt[0] += mytilt

            return rightsum + leftsum + node.val

        if root is None:
            return 0
        dfs(root)
        return global_tilt[0]
