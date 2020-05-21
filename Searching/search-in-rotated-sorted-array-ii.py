# 81. Search in Rotated Sorted Array II
# Medium

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        start = 0
        end = len(nums) - 1
        polestar = nums[-1]
        region = None
        while start < len(nums) and nums[start] == polestar:
            start += 1
            
        if target == polestar:
            return True
        else:
            if target < polestar:
                region = 'orange'
            else:
                region = 'green'
                
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return True
            if nums[mid] <= polestar:
                if target < nums[mid] or region is 'green':
                    end = mid - 1
                else:
                    start = mid + 1
                    
            else:
                if target > nums[mid] or region is 'orange':
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False