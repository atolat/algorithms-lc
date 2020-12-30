# 119. Pascal's Triangle II
# Easy

# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [1]*(rowIndex + 1)

        for row in range(rowIndex+1):
            dp[row] = [1] * (row+1)

        for row in range(2, rowIndex + 1):
            for k in range(1, row):
                dp[row][k] = dp[row-1][k] + dp[row-1][k-1]

        return dp[rowIndex]
