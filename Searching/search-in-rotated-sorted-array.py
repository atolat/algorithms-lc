# 33. Search in Rotated Sorted Array
# Medium

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        polestar = nums[-1]
        start = 0
        end = len(nums) - 1
        # Let's divide the array into regions 
        # green - Rotated sorted half
        # orange - Original sorted half
        # ##GREEN#MIN##ORANGE##
        while start <= end:
            if target == polestar:
                return len(nums) - 1
            # Determine which region the target is in
            if target < polestar:
                region = 'orange'
            else:
                region = 'green'
            # Let's do a binary search for the target
            mid = (start+end) // 2
            if target == nums[mid]:
                return mid
            # If mid is in orange region
            if nums[mid] < polestar:
                if target < nums[mid] or region == 'green':
                    end = mid - 1
                else:
                    start = mid + 1
            else: # If mid is in green
                if target > nums[mid] or region == 'orange':
                    start = mid + 1
                else:
                    end = mid - 1
        return -1