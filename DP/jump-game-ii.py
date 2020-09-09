# 45. Jump Game II
# Hard

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Recursive Solution - Brute Force
import math


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursive Solution
        def helper(jumps, currentIndex):
            n = len(jumps)
            # Base Cases
            if currentIndex == n - 1:
                return 0
            if jumps[currentIndex] == 0:
                return float('+inf')

            totalJumps = float('+inf')
            start = currentIndex + 1
            end = currentIndex + jumps[currentIndex]
            for i in range(start, end+1):
                if i < n:
                    minJumps = 1 + helper(jumps, i)
                    if minJumps != float('+inf'):
                        totalJumps = min(minJumps, totalJumps)
            return totalJumps

        return helper(nums, 0)

# Top Down - Recursion + Memo


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursive Solution with memo
        def helper(jumps, currentIndex):
            n = len(jumps)
            # Base Cases
            if currentIndex == n - 1:
                return 0
            if jumps[currentIndex] == 0:
                return float('+inf')

            if dp[currentIndex] != 0:
                return dp[currentIndex]

            totalJumps = float('+inf')
            start = currentIndex + 1
            end = currentIndex + jumps[currentIndex]
            for i in range(start, end+1):
                if i < n:
                    minJumps = 1 + helper(jumps, i)
                    if minJumps != float('+inf'):
                        totalJumps = min(minJumps, totalJumps)
            dp[currentIndex] = totalJumps
            return dp[currentIndex]

        dp = [0 for x in range(len(nums))]
        return helper(nums, 0)
