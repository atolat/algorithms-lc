# 658. Find K Closest Elements
# Medium

# Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

from heapq import *
import bisect


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        index = bisect.bisect_left(arr, x) - 1
        left = index
        right = index + 1
        n = len(arr)
        result = collections.deque()
        for i in range(k):
            if left >= 0 and right < len(arr):
                left_diff = abs(arr[left] - x)
                right_diff = abs(arr[right] - x)
                if left_diff <= right_diff:
                    result.appendleft(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            elif left >= 0:
                result.appendleft(arr[left])
                left -= 1
            elif right < len(arr):
                result.append(arr[right])
                right += 1
        return result
