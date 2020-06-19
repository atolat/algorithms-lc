# 250. Count Univalue Subtrees
# Medium

# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# Example :

# Input:  root = [5,1,5,5,5,null,5]

#               5
#              / \
#             1   5
#            / \   \
#           5   5   5

# Output: 4
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        globalcount = [0]
        if not root:
            return 0

        def dfs(node):
            if node.left is None and node.right is None:
                globalcount[0] += 1
                return True

            bL, bR = True, True
            amIUnival = True

            if node.left:
                bL = dfs(node.left)
                if not bL or node.val != node.left.val:
                    amIUnival = False
            if node.right:
                bR = dfs(node.right)
                if not bR or node.val != node.right.val:
                    amIUnival = False
            if amIUnival:
                globalcount[0] += 1
            return amIUnival

        dfs(root)
        return globalcount[0]
