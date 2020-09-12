# 256. Paint House
# Easy

# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:

# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
#              Minimum cost: 2 + 5 + 3 = 10.

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs) - 1
        red = [0, 0, 0]
        blue = [0, 0, 0]
        green = [0, 0, 0]

        # Base Cases
        red[0] = costs[0][0]
        blue[0] = costs[0][1]
        green[0] = costs[0][2]

        # Fill DP
        for i in range(1, len(costs)):
            red[i % 3] = costs[i][0] + min(green[(i-1) % 3], blue[(i-1) % 3])
            blue[i % 3] = costs[i][1] + min(green[(i-1) % 3], red[(i-1) % 3])
            green[i % 3] = costs[i][2] + min(blue[(i-1) % 3], red[(i-1) % 3])

        return min(red[n % 3], blue[n % 3], green[n % 3])
