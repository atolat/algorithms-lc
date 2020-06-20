# 124. Binary Tree Maximum Path Sum
# Hard

# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Top Down DFS
        globalmax = [float("-inf")]

        def dfs(node):
            mymaxpathsum = node.val
            mymaxVpathsum = node.val

            # Leaf node - PASS

            # Recursive Case
            if node.left is not None:
                leftmax = dfs(node.left)
                mymaxpathsum = max(leftmax + node.val, mymaxpathsum)
                mymaxVpathsum = mymaxpathsum
            if node.right is not None:
                rightmax = dfs(node.right)
                mymaxpathsum = max(rightmax + node.val, mymaxpathsum)
                
                # Maximize 4 options:
                # (i) node.val
                # (ii) node.val + leftmax
                # (iii) node.val + rightmax
                # (iv) node.val + leftmax + rightmax
                
                mymaxVpathsum = max(
                    mymaxVpathsum, mymaxVpathsum + rightmax, node.val+rightmax)

            if mymaxVpathsum > globalmax[0]:
                globalmax[0] = mymaxVpathsum
            return mymaxpathsum

        dfs(root)
        return globalmax[0]
