# 112. Path Sum
# Easy

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        # Use DFS Template to solve this
        # Edge Case
        if root is None:
            return False
        # Set a global boolean as the answer
        answer = [False]
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs_helper(node, target, slatesum):
            # Base Case : Leaf Node
            if node.left is None and node.right is None:
                if target == slatesum + node.val:
                    answer[0] = True
                    return
                
            # Recursive Case : Internal Node
            if node.left is not None:
                dfs_helper(node.left, target, slatesum + node.val)
                
            if node.right is not None:
                dfs_helper(node.right, target, slatesum + node.val)
                

        dfs_helper(root, sum, 0)
        return answer[0]