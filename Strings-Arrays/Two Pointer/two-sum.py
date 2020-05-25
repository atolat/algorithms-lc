# 1. Two Sum
# Easy

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[nums[i]] = i
        return -1
    
# Complexity Analysis:

# Time complexity : O(n). We traverse the list containing n elements only once. Each look up in the table costs only O(1) time.
# Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.