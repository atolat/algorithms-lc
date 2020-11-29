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

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        start = matrix[0][0]
        end = matrix[n-1][n-1]
        while start < end:
            mid = (start + end)//2
            smallest_gt_mid = matrix[n-1][n-1]
            largest_lt_mid = matrix[0][0]
            count, smallest_gt_mid, largest_lt_mid = \
                self.count_smaller_larger(matrix,
                                          smallest_gt_mid,
                                          largest_lt_mid,
                                          mid)
            if count == k:
                return largest_lt_mid
            else:
                if count < k:
                    start = smallest_gt_mid
                else:
                    end = largest_lt_mid
        return start

    def count_smaller_larger(self, matrix, smallest_gt_mid, largest_lt_mid, mid):
        n = len(matrix)
        row, col = n-1, 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                smallest_gt_mid = min(smallest_gt_mid, matrix[row][col])
                row -= 1
            else:
                largest_lt_mid = max(largest_lt_mid, matrix[row][col])
                col += 1
                count += row + 1
        return count, smallest_gt_mid, largest_lt_mid
