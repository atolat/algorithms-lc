# 373. Find K Pairs with Smallest Sums
# Medium

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:

# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

from heapq import *


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Initialize a maxheap
        maxheap = []

        # Insert every pair of numbers in the maxheap along with the sum
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(maxheap) < k:
                    heappush(
                        maxheap, (-(nums1[i]+nums2[j]), (nums1[i], nums2[j])))

                else:
                    if (nums1[i] + nums2[j]) > -maxheap[0][0]:
                        break
                    else:
                        heappop(maxheap)
                        heappush(
                            maxheap, (-(nums1[i]+nums2[j]), (nums1[i], nums2[j])))

        out = []
        for sum, pair in maxheap:
            out.append(pair)

        return out
