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
        dp = [[0 for _ in range(1+len(text2))] for _ in range(1+len(text1))]

        # Tabulate
        for row in range(1, 1 + len(text1)):
            for col in range(1, 1 + len(text2)):
                if text1[row - 1] == text2[col - 1]:
                    s = 1
                else:
                    s = 0
                dp[row][col] = max(dp[row-1][col], dp[row]
                                   [col-1], dp[row-1][col-1] + s)
        return dp[-1][-1]r
