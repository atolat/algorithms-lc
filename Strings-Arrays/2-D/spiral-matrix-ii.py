# 59. Spiral Matrix II
# Medium

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        left = 0
        right = n - 1
        bottom = n - 1
        top = 0
        counter = 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res[top][i] = counter
                counter += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = counter
                counter += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res[bottom][i] = counter
                    counter += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res[i][left] = counter
                    counter += 1
                left += 1

        return res
