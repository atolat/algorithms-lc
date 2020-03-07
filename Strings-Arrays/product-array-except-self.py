# 238. Product of Array Except Self
# Medium

# 3712

# 315

# Add to List

# Share
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# REVISIT!
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [0] * length
        result[0] = 1
        # Compute products left of every number
        for i in range(1, length):
            result[i] = nums[i - 1] * result[i - 1]
        
        # R holds the product right of every number 
        R = 1
        for i in reversed(range(length)):
            result[i] = result[i] * R
            R = R * nums[i]
            
        return result