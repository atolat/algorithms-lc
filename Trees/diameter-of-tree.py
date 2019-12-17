# 543. Diameter of Binary Tree
# Easy

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        globalDiameter = [0]
        if root is None:
            return 0
        def dfs_helper(node):
            local_height = 0
            local_diameter = 0
            # Base Case
            if node.left is None and node.right is None:
                pass
            
            # Recursive Case
            if node.left is not None:
                left_subtree_height = dfs_helper(node.left)
                local_height = 1 + left_subtree_height
                local_diameter = 1 + left_subtree_height
                
            if node.right is not None:
                right_subtree_height = dfs_helper(node.right)
                local_height = max(1 + right_subtree_height, local_height)
                local_diameter += 1 + right_subtree_height
                
            if local_diameter > globalDiameter[0]:
                globalDiameter[0] = local_diameter
                
            return local_height
        
        
        dfs_helper(root)
        return globalDiameter[0]
                