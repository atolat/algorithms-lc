# 1092. Shortest Common Supersequence
# Hard

# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

# (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

# Example 1:

# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # LCP + Traceback
        # PART I LCP
        dp = [[0 for _ in range(1+len(str2))] for _ in range(1+len(str1))]

        # Tabulate
        for row in range(1, 1 + len(str1)):
            for col in range(1, 1 + len(str2)):
                if str1[row - 1] == str2[col - 1]:
                    s = 1
                else:
                    s = 0
                dp[row][col] = max(dp[row-1][col], dp[row]
                                   [col-1], dp[row-1][col-1] + s)
        print dp[-1][-1]

        # Part II Traceback
        result = []
        row = len(str1)
        col = len(str2)

        while row != 0 and col != 0:
            if dp[row][col] == dp[row-1][col]:
                result.append(str1[row-1])
                row -= 1

            elif dp[row][col] == dp[row][col-1]:
                result.append(str2[col-1])
                col -= 1

            else:
                result.append(str1[row-1])
                row -= 1
                col -= 1

        while row != 0:
            result.append(str1[row-1])
            row -= 1

        while col != 0:
            result.append(str2[col-1])
            col -= 1

        result.reverse()
        return "".join(result)
