# 583. Delete Operation for Two Strings
# Medium

# 1165

# 26

# Add to List

# Share
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(1+len(word2))] for _ in range(1+len(word1))]

        # Base Cases
        for col in range(1 + len(word2)):
            dp[0][col] = col

        for row in range(1 + len(word1)):
            dp[row][0] = row

        # Tabulate
        for row in range(1, 1 + len(word1)):
            for col in range(1, 1 + len(word2)):
                if word1[row - 1] == word2[col - 1]:
                    s = 0
                else:
                    s = 3
                dp[row][col] = min(dp[row-1][col] + 1, dp[row]
                                   [col-1] + 1, dp[row-1][col-1] + s)
        return dp[-1][-1]
