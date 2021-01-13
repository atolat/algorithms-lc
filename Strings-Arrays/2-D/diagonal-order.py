# 498. Diagonal Traverse
# Medium

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

# Example:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# Output:  [1,2,4,7,5,3,6,8,9]

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = []
        i, j, idx = 0, 0, 0
        dir = 'UP'

        while idx < (m*n):
            result.append(matrix[i][j])
            if dir == 'UP':
                if j == n - 1:
                    dir = 'DOWN'
                    i += 1
                elif i == 0:  # Switch
                    dir = 'DOWN'
                    j += 1

                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    dir = 'UP'
                    j += 1
                elif j == 0:
                    dir = 'UP'
                    i += 1
                else:
                    i += 1
                    j -= 1
            idx += 1

        return result
