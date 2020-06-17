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
    
# Time complexity #
# The time complexity of the above algorithm is O(logN + K*logK). 
# We need O(logN)O(logN) for Binary Search and O(K*logK)O(K∗logK) to insert the numbers in the Min Heap, 
# as well as to sort the output array.

# Space complexity #
# The space complexity will be O(K), as we need to put a maximum of 2K numbers in the heap.

# Alternate - Binary Search - FASTER
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
            if left >= 0 and right < n:
                diff1 = abs(arr[left] - x)
                diff2 = abs(arr[right] - x)
                if diff1 <= diff2:
                    result.appendleft(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            elif left >= 0:
                result.appendleft(arr[left])
                left -= 1
            elif right < n:
                result.append(arr[right])
                right += 1
        return result