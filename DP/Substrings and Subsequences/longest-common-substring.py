# 718. Maximum Length of Repeated Subarray
# Medium

# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Example 1:

# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # Consider this as a longest common substring problem
        # Initialize dp table with 0's
        dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

        # Maxlen to track the longest substring
        maxlen = 0

        # Tabulate
        # dp[i][j] -> the length of the common substring at index B[i], A[j]
        for i in range(1, len(B)+1):
            for j in range(1, len(A)+1):
                # If the numbers at the current index are equal, check the length of the ssubstring formed by the previous characts and add 1
                if A[j-1] == B[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                # If not equal, reset dp[i][j] to 0
                else:
                    dp[i][j] = 0
                # Track max seen so far
                maxlen = max(dp[i][j], maxlen)

        return maxlen
