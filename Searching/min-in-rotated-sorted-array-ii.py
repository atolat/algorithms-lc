# 154. Find Minimum in Rotated Sorted Array II
# Hard

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        polestar = nums[-1]
        while start < len(nums)-1 and nums[start] == polestar:
            start += 1
                    
        while start <= end:
            mid = (start + end)//2
            # Green Region
            if nums[mid] > polestar:
                start = mid + 1
            else:
                end = mid - 1
                
        return nums[start]