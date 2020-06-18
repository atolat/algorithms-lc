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
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []

        def dfs(node, slate, slatesum):
            slatesum += node.val
            slate.append(node.val)
            # Base Case - Leaf Node
            if node.left is None and node.right is None:
                if slatesum == sum1:
                    result.append(slate[:])
            if node.left:
                dfs(node.left, slate, slatesum)
            if node.right:
                dfs(node.right, slate, slatesum)
            slate.pop()

        dfs(root, [], 0)
        return result
