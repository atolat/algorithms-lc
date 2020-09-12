# 935. Knight Dialer
# Medium

# Given an integer n, return how many distinct phone numbers of length n we can dial.
# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n.
# All jumps should be valid knight jumps.
# As the answer may be very large, return the answer modulo 109 + 7.


# Example 1:

# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
# Example 2:

# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# Example 3:

# Input: n = 3
# Output: 46
# Example 4:

# Input: n = 4
# Output: 104
# Example 5:

# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[0 for _ in range(10)] for _ in range(N+1)]

        # Base Case
        for i in range(10):
            dp[1][i] = 1

        # Fill Table
        for i in range(2, N+1):
            dp[i][0] = dp[i-1][4] + dp[i-1][6]
            dp[i][1] = dp[i-1][6] + dp[i-1][8]
            dp[i][2] = dp[i-1][7] + dp[i-1][9]
            dp[i][3] = dp[i-1][4] + dp[i-1][8]
            dp[i][4] = dp[i-1][0] + dp[i-1][3] + dp[i-1][9]
            dp[i][5] = 0
            dp[i][6] = dp[i-1][0] + dp[i-1][1] + dp[i-1][7]
            dp[i][7] = dp[i-1][2] + dp[i-1][6]
            dp[i][8] = dp[i-1][1] + dp[i-1][3]
            dp[i][9] = dp[i-1][2] + dp[i-1][4]

        return sum(dp[-1]) % (10**9+7)
