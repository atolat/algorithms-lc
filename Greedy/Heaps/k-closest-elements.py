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
        index = bisect.bisect_left(arr, x)
        low = max(0, index - k)
        high = min(index + k, len(arr) - 1)
        minheap = []
        result = []
        
        for i in range(low, high + 1):
            diff = abs(arr[i] - x)
            heappush(minheap, (diff, arr[i]))
        
            
        for _ in range(k):
            result.append(heappop(minheap)[1])
            
        return sorted(result)