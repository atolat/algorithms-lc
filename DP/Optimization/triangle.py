# 120. Triangle
# Medium

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

from copy import deepcopy

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Initialize Table
        dp = deepcopy(triangle)
        n = len(triangle)

        # Base Cases
        dp[0][0] = triangle[0][0]

        for row in range(1, n):
            # Left side
            dp[row][0] = dp[row-1][0] + triangle[row][0]
            # Right side
            dp[row][row] = dp[row-1][row-1] + triangle[row][row]

        # Fill Table
        for row in range(2, n):
            for col in range(1, row):
                dp[row][col] = triangle[row][col] + \
                    min(dp[row-1][col], dp[row-1][col-1])
        return min(dp[-1])
