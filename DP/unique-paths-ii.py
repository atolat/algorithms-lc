# 63. Unique Paths II
# Medium

# A robot is located at the top-left corner of a m x n grid 
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid.
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Initialize Table
        n = len(obstacleGrid) # number of rows
        m = len(obstacleGrid[0]) # number of columns
        
        # Edge Case::
        if obstacleGrid[0][0] == 1: return 0
        
        table = [[None for i in range(m)] for j in range(n)]
        
        # Fill in the base cases
        table[0][0] = 1 # Start
        
        for col in range(1,m):
            if obstacleGrid[0][col] == 1: # Obstacle
                table[0][col] = 0
            else:
                table[0][col] = table[0][col-1]
                
        for row in range(1,n):
            if obstacleGrid[row][0] == 1: # Obstacle
                table[row][0] = 0
            else:
                table[row][0] = table[row-1][0]
                
        # Tabulate results
        for row in range(1, n):
            for col in range(1, m):
                if obstacleGrid[row][col] == 1: # Obstacle
                    table[row][col] = 0
                else:
                    table[row][col] = table[row-1][col] + table[row][col-1]
        return table[-1][-1]