# 62. Unique Paths
# Medium

# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[1] * n for _ in range(m)]
        
        for row in range(1,m):
            for col in range(1,n):
                table[row][col] = table[row-1][col] + table[row][col-1]
                
        return table[m-1][n-1]