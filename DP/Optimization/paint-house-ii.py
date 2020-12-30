# 265. Paint House II
# Hard

# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:

# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Follow up:
# Could you solve it in O(nk) runtime?

from copy import deepcopy

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])

        dp = deepcopy(costs)
        prev_min = [[0, 0] for _ in range(n)]
        prev_min[0][0], prev_min[0][1] = min(
            costs[0]), self.second_smallest(costs[0])

        # Tabulate
        for house in range(1, n):
            for color in range(k):
                if prev_min[house-1][0] == dp[house-1][color]:
                    best = prev_min[house-1][1]
                else:
                    best = prev_min[house-1][0]
                dp[house][color] = best + costs[house][color]
            prev_min[house][0], prev_min[house][1] = min(
                dp[house]), self.second_smallest(dp[house])

        return min(dp[-1])

    def second_smallest(self, numbers):
        m1, m2 = float('inf'), float('inf')
        for x in numbers:
            if x <= m1:
                m1, m2 = x, m1
            elif x < m2:
                m2 = x
        return m2
