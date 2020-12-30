# 343. Integer Break
# Medium

# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# Example 1:

# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Edge Case
        if n == 2:
            return 1

        dp = [0 for _ in range(n+1)]

        # Base Cases
        dp[1] = 1
        dp[2] = 2

        # Tablulate
        for i in range(3, n+1):
            if i == n:
                best = n-1
            else:
                best = i
            for j in range(1, i):
                best = max(best, dp[i-j]*dp[j])
            dp[i] = best
        return dp[n]
