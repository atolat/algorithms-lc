# 268. Missing Number
# Easy

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Compute sum to n
        n = len(nums)
        sum_n = (n*(n+1))/2
        sum_missing = 0
        # Find sum of array
        for n in nums:
            sum_missing += n
        
        return sum_n - sum_missing