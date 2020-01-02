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

# Use the bottom-up DFS template to solve this. In this template, information flows from nodes to root for every subtree.
# Global Problem - Root node, manager: Count the number of uni-val sub-trees
# Local Problem - intermidiate nodes, subordinates: Am I a unival sub-tree?
# How does the local problem answer the global problem?
# Global Answer = Σ Local Answers

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Initialize a global answer that is the sum of all unival trees
        globalAnswer = [0]
        
        # Edge Case
        if root is None:
            return 0
        
        def dfs_helper(node):
            # This bool will hold the result for every subordinate node - Am I a unival subtree?
            amIUnival = True
            
            # Base Case: Leaf Nodes, every leaf node is a unival sub-tree, add 1 to the global answer and return True
            if node.left is None and node.right is None:
                globalAnswer[0] += 1
                return True

            # Recursive Case: Intermediate Nodes - DFS traversal, return a boolean that checks if subtree is unival
            # If the boolean is False or parent-child values are not equal, update amIUnival to False
            if node.left is not None:
                boolLeft = dfs_helper(node.left)
                if boolLeft is False or node.val != node.left.val:
                    amIUnival = False
                
            if node.right is not None:
                boolRight = dfs_helper(node.right)
                if boolRight is False or node.val != node.right.val:
                    amIUnival = False

            # For every valid unival subtree, update the global answer  
            if amIUnival is True:
                globalAnswer[0] += 1
                
            return amIUnival
        
        dfs_helper(root)
        return globalAnswer[0]