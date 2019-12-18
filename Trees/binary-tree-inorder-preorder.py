# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Use the top down tree construction template
# 3 steps:
# - Construct the root node
# - Recursively construct the left subtree
# - Recursively construct the right subtree

# General strategy:
# - find the root node as the first node in the preorder array
# - Use this to find index of root node in inorder array
# - Split inorder array at root and recursively construct the left and right subtrees


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Initialize a map that will store inorder elements with indices, easy access to find root node
        inorder_map = {}
        # Populate map with inorder values and indices
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def helper(preorder, startP, endP, inorder, startI, endI):
            # Base Case
            if startP > endP:
                return None

            # Recursive Case
            # Find root - first element of preorder array
            root = preorder[startP]

            # Find the index of this node in the inorder array
            rootIndex = inorder_map[root]

            # Find the number of elements in the left and right subtree from the inorder array
            # PREORDER *ROOT* [LEFT] [RIGHT]
            # INORDER [LEFT] *ROOT* [RIGHT]
            numleft = rootIndex - startI
            numright = endI - rootIndex

            # Create a root node from first element of preorder array
            subtreeroot = TreeNode(preorder[startP])

            # Delegate the task of creating left and right subtrees recursively
            subtreeroot.left = helper(
                preorder, startP+1, startP + numleft, inorder, startI, startI + numleft - 1)
            subtreeroot.right = helper(
                preorder, startP+numleft+1, endP, inorder, rootIndex+1, rootIndex+numright)

            return subtreeroot

        return helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
