# 230. Kth Smallest Element in a BST
# Medium

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        kth = [0]

        def dfs(node, numpred):
            # Backtrack
            if numpred > k:
                return numpred

            # Base
            if node.left is None and node.right is None:
                numpred += 1
                if k == numpred:
                    kth[0] = node.val
                return numpred

            # Recursive
            if node.left:
                numpred = dfs(node.left, numpred)

            # Inorder
            numpred += 1
            if k == numpred:
                kth[0] = node.val

            if node.right:
                numpred = dfs(node.right, numpred)

            return numpred

        dfs(root, 0)
        return kth[0]
