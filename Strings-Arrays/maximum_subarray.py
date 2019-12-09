# 53. Maximum Subarray
# Easy

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max_sum = nums[0]
        max_sum = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            current_max_sum = max(nums[i], current_max_sum + nums[i])
            max_sum = max(max_sum, current_max_sum)
        return max_sum
