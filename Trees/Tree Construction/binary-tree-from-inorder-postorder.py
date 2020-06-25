# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium

# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        ino_map = {}
        for i in range(len(inorder)):
            ino_map[inorder[i]] = i

        def helper(p_start, p_end, i_start, i_end):
            # Base Case
            if p_start > p_end:
                return None
            if p_start == p_end:
                return TreeNode(postorder[p_start])

            root_val = postorder[p_end]
            root_index = ino_map[root_val]
            root = TreeNode(root_val)

            numleft = root_index - i_start
            numright = i_end - root_index

            root.left = helper(p_start,
                               p_start + numleft - 1,
                               i_start,
                               i_start + numleft - 1)
            root.right = helper(p_start + numleft,
                                p_end - 1,
                                root_index + 1,
                                i_end)
            return root

        return helper(0, len(postorder) - 1, 0, len(inorder) - 1)