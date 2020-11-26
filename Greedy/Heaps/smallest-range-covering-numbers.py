# 632. Smallest Range Covering Elements from K Lists
# Hard

# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.


# Example 1:

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Example 2:

# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
# Example 3:

# Input: nums = [[10,10],[11,11]]
# Output: [10,11]
# Example 4:

# Input: nums = [[10],[11]]
# Output: [10,11]
# Example 5:

# Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
# Output: [1,7]

from heapq import *


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        minheap = []
        maxNum = float('-inf')
        range = []
        if not nums:
            return []

        # initialize a range start and end
        rangeStart = float('-inf')
        rangeEnd = float('+inf')

        # Put the smallest number from every list in the min-heap
        # Keep track of the largest number amongst the smallest numbers
        for numlist in nums:
            if numlist:
                heappush(minheap, (numlist[0], 0, numlist))
                maxNum = max(numlist[0], maxNum)

        while len(minheap) == len(nums):
            num, index, numlist = heappop(minheap)
            # Check if the smallest number and maxNum give a smaller range than the current range - update range
            if rangeEnd - rangeStart > maxNum - num:
                rangeStart = num
                rangeEnd = maxNum

            if index + 1 < len(numlist):
                # Push the next smallest elements, update the maxNum
                heappush(minheap, (numlist[index+1], index+1, numlist))
                maxNum = max(maxNum, numlist[index+1])

        return [rangeStart, rangeEnd]
