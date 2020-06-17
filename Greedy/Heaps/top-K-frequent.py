# 347. Top K Frequent Elements
# Medium

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter
from heapq import *

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = Counter(nums)
        minheap = []
        
        for key, val in freq_map.items():
            heappush(minheap, (val, key))
            if len(minheap) > k:
                heappop(minheap)
                
        result = [y for (x,y) in minheap]
        
        return result
    
# Time complexity #
# The time complexity of the above algorithm is O(N+N*logK).

# Space complexity #
# The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap. 
# For the frequency map, however, we need to store all the ‘N’ numbers.