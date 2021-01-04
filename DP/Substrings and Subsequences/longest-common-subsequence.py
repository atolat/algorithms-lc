# 1143. Longest Common Subsequence
# Medium

# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.


# If there is no common subsequence, return 0.


# Example 1:

# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
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
