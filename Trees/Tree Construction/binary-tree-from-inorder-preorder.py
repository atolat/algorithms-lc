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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(p_start, p_end, i_start, i_end):
            # Base Case
            if p_start > p_end:
                return None
            if p_start == p_end:
                return TreeNode(preorder[p_start])

            root_val = preorder[p_start]
            root_index = ino_map[root_val]
            root = TreeNode(root_val)

            # Number of elements in left subtree:
            numleft = root_index - i_start
            # Number of elements in right subtree:
            numright = i_end - root_index

            # Recursively construct left and right subtrees
            root.left = helper(p_start + 1,
                               p_start + numleft,
                               i_start,
                               i_start + numleft - 1)
            root.right = helper(p_start + numleft + 1,
                                p_end,
                                root_index + 1,
                                i_end)
            return root

        # Maintain a hashmap of indexes of inorder array
        ino_map = {}
        for i in range(len(inorder)):
            ino_map[inorder[i]] = i
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
