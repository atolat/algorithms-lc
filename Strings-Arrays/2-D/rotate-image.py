# 48. Rotate Image
# Medium

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # Find Transpose
        for i in range(m):
            for j in range(n):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse every row
        for row in matrix:
            row.reverse()
