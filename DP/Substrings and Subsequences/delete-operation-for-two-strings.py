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

# Approach 1: USING LCS
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Find the lcs
        # minimum deletions = m+n−2∗lcs. Here, m and n refer to the length of the two given strings s1 and s2.
        # The above equation works because in case of complete mismatch(i.e. if the two strings can't be equalized at all), the total number of delete operations required will be m + n. Now, if there is a common sequence among the two strings of length lcs, we need to do lcs lesser deletions in both the strings leading to a total of 2*lcs lesser deletions, which then leads to the above equation.
        lcs = self.LCS(word1, word2)
        min_del = len(word1) + len(word2) - 2*(lcs)
        return min_del
        
        
    def LCS(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # initialize a dp table
        # dp[i][j] -> length of the longest common substring at text1[i], text2[j]
        dp = [[0 for _ in range(1+len(text2))] for _ in range(1+len(text1))]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                s = 0  # Reward
                # If the characcters at i, j match for text1 and text2, reward the match by setting s = 1
                if text2[j-1] == text1[i-1]:
                    s = 1
                # dp[i-1][j-1] -> substituition operation - match or mismatch
                # dp[i-1][j] -> pick a character from text2 and delete character from text1
                # dp[i][j-1] -> pick a character from text1 and delete character from text2
                dp[i][j] = max(dp[i-1][j-1] + s, dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


# Approach 2: WITHOUT USING LCS
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
