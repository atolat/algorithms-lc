# 746. Min Cost Climbing Stairs
# Easy

# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

# Decrease and Conquer: At any arbitrary step i, you could reach i from either the (i-1)th step or (i-2)th step. The objectiove function to find the min cost f(i) -> f(i) = cost(i) + min(f(i-1), f(i-2))
# RECURSIVE SOLUTION #
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def f(i):
            if i == 0 or i == 1:
                return cost[i]
            min_cost = cost[i] + min(f(i-1), f(i-2))
            return min_cost
        n = len(cost) - 1
        
        return min(f(n), f(n-1))
    
# BOTTOM UP DP #
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])
