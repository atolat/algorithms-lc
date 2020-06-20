# 333. Largest BST Subtree
# Medium

# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

# Note:
# A subtree must include all of its descendants.

# Example:

# Input: [10,5,15,1,8,null,7]

#    10
#    / \
#   5  15
#  / \   \
# 1   8   7

# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Top Down DFS
        global_count = [0]

        def dfs(node):
            mysmallest, mylargest = node.val, node.val
            mysize = 1
            amIBST = True

            # Leaf nodes - PASS

            # Recursive case:
            if node.left is not None:
                (size, s, l, b) = dfs(node.left)
                mysize = mysize + size
                mysmallest = min(s, mysmallest)
                mylargest = max(l, mylargest)
                if not b or l >= node.val:
                    amIBST = False
            if node.right is not None:
                (size, s, l, b) = dfs(node.right)
                mysize = mysize + size
                mysmallest = min(s, mysmallest)
                mylargest = max(l, mylargest)
                if not b or node.val >= s:
                    amIBST = False
            if amIBST and mysize > global_count[0]:
                global_count[0] = mysize
            return (mysize, mysmallest, mylargest, amIBST)

        if root is None:
            return 0
        dfs(root)
        return global_count[0]
