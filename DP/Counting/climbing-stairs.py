# 70. Climbing Stairs
# Easy

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Recursive Solution
# Decrease and conquer - If you are in the last stair, you can reach it from the (n-1)th stair or (n-2)th stair - total number of ways f(n) = f(n-1) + f(n-2) -- similar to fibonacci.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            # Base Cases
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            return helper(n-1) + helper(n-2)

        return helper(n)

# Bottom Up DP
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using a decrease and conquer approach,
        # number of ways to reach to the last 'n'th step
        # f(n) =  f(n-1) + f(n-2)
        # Base case f(1) = 1, f(2) = 2

        table = [None] * (n + 1)

        if n == 1:
            return 1
        if n == 2:
            return 2
        table[1] = 1
        table[2] = 2
        for i in range(3, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]
