# 540. Single Element in a Sorted Array
# Medium

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Apply Binary Search template
        # Zones in the array::
        # even-odd pairs :: unpaired number :: odd-even pairs
        
        # Edge cases
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end) // 2
            if nums[mid-1] != nums[mid] !=nums[mid+1]: # Unpaired element found
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] == nums[mid+1]) or \
                 (mid % 2 == 1 and nums[mid] == nums[mid-1]): # even-odd zone
                    start = mid + 1
            else: # odd-even zone
                end = mid - 1
                
        return -1
        