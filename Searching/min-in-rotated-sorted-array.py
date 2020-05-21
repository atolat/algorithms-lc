# 153. Find Minimum in Rotated Sorted Array
# Medium

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use binary search template
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end) // 2
            # Use last element as anchor
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]