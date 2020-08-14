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
        # Cyclic sort
        # The idea of cyclic sort is to try and place a number at it's index
        # Eg: 1 must go at index 1, 2 must go at index 2 and so on...
        i = 0
        n = len(nums)
        while i < n:
            # j is the index of the number
            j = nums[i]

            # Try to cyclically sort the whole array, ignore numbers that
            # are out of range (> len array)
            if nums[i] < n and nums[i] != nums[j]:
                # If a number is within the range and not at the right index, swap it
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # Go through the array again and check if the number is at expected index
        # If not, it's missing!
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return n

#     O(n) time, constant space
#     [3,0,1] --> [0,1,3]
#     Second scan -
#     0th index - 0,
#     1st index - 1,
#     2nd index - 3 -- mismatch, return 2 is nissing

# ALTERNATE SOLUTION - using Gauss formula


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
