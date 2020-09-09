# 64. Minimum Path Sum
# Medium

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Initialize 2d dp table
        m = len(grid)  # Rows
        n = len(grid[0])  # Cols

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Base Cases
        # Each cell in the dp table:
        # dp[i][j] - min cost to go from source to cell[i][j]
        dp[0][0] = grid[0][0]

        # Row 0
        for col in range(1, n):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        # Col 0
        for row in range(1, m):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        # Fill DP table
        # Recurrence - f(i,j) = grid(i,j) + min(f(i-1, j), f(i, j-1))
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
