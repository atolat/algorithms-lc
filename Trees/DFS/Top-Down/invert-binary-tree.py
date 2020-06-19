# 226. Invert Binary Tree
# Easy

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        def dfs(node):
            old_left = node.left
            old_right = node.right
            node.left = old_right
            node.right = old_left

            if old_left:
                dfs(old_left)
            if old_right:
                dfs(old_right)

        dfs(root)
        return root
