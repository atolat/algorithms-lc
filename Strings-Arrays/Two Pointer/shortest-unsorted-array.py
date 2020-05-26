# 581. Shortest Unsorted Continuous Subarray
# Easy

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the low boundary:
        # First number of the unsorted sub-array
        low = 0
        while low < len(nums) - 1 and nums[low] <= nums[low+1]:
            low += 1
        
        if low == len(nums) - 1: # Entire array is sorted
            return 0
        
        # Find the high boundary
        high = len(nums) - 1
        while high > 0 and nums[high] >= nums[high-1]:
            high -= 1
        
        # Find the max and min numbers in the unsorted subarray
        max_num = max(nums[low:high+1])
        min_num = min(nums[low:high+1])
        
        # Extend low to include numbers greater than min_num
        while low > 0 and nums[low-1] > min_num:
            low -= 1
        # Extend high to include numbers lesser than max_num
        while high < len(nums)-1 and nums[high+1] < max_num:
            high += 1
            
        return high - low + 1
        
# Time complexity #
# The time complexity of the above algorithm will be O(N).

# Space complexity #
# The algorithm runs in constant space O(1).