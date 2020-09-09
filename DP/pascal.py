# 118. Pascal's Triangle
# Easy

# 1716

# 118

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        table = [1] * (numRows)

        for row in range(numRows):
            table[row] = [1] * (row+1)

        for row in range(2, numRows):
            for k in range(1, row):
                table[row][k] = table[row-1][k] + table[row-1][k-1]

        return table
