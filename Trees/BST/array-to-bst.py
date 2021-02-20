# 108. Convert Sorted Array to Binary Search Tree
# Easy

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # Inner Helper Function
        def helper(nums, start, end):
            # Base Case
            if start > end:
                return None

            # Recursive Case
            # Find the middle element and create a root node from it
            mid = int((start+end)/2)
            root = TreeNode(nums[mid])

            # Recursively create the left and right subtrees from array
            root.left = helper(nums, start, mid-1)
            root.right = helper(nums, mid+1, end)

            return root

        # Outer Function
        return helper(nums, 0, len(nums)-1)