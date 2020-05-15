# 74. Search a 2D Matrix
# Medium

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Use binary search template
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        start = 0
        end = (m*n) - 1
        
        while start <= end:
            mid = (start+end) // 2
            row = mid//n
            col = mid%n
            if target == matrix[row][col]:
                return True
            if target > matrix[row][col]:
                start = mid + 1
            else:
                end = mid - 1
        return False
            
            