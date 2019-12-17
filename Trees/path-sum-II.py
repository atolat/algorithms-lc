# 113. Path Sum II
# Medium

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        # Use DFS Template to solve this
        # Edge Case
        if root is None:
            return []
        # Set a global array as the answer
        answer = []
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs_helper(node, target, slate, slatesum):
            # Base Case : Leaf Node
            if node.left is None and node.right is None:
                if target == slatesum + node.val:
                    slate.append(node.val)
                    answer.append(slate[:])
                    slate.pop()
                    return
                
            # Recursive Case : Internal Node
            slate.append(node.val)
            if node.left is not None:
                dfs_helper(node.left, target,slate, slatesum + node.val)
                
            if node.right is not None:
                dfs_helper(node.right, target,slate, slatesum + node.val)
            slate.pop()

        dfs_helper(root, sum,[], 0)
        return answer