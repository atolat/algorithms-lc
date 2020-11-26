# 378. Kth Smallest Element in a Sorted Matrix
# Medium

# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.

from heapq import *


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        minheap = []
        for l in matrix:
            heappush(minheap, (l[0], 0, l))

        count = 0
        num = 0
        while minheap:
            num, index, l = heappop(minheap)
            count += 1

            if count == k:
                break

            if len(l) > index+1:
                heappush(minheap, (l[index+1], index + 1, l))
        return num
