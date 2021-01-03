# 1049. Last Stone Weight II
# Medium

# We have a collection of rocks, each rock has a positive integer weight.

# Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)


# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

# Recursive Solution - TLE
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        def helper(sum1, sum2, index):
            # Base Case
            if index == -1:
                return abs(sum1 - sum2)
            # Recursive Cases
            # Include the number at current index in first subset
            diff1 = helper(sum1 + stones[index], sum2, index - 1)
            # Include the number at current index in second subset
            diff2 = helper(sum1, sum2 + stones[index], index - 1)

            return min(diff1, diff2)

        return helper(0, 0, len(stones) - 1)

# Similar to partition equal subset sum.
# We can rephrase the question as - Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.
# Fill the dp table to see if target sum = sum/2 can be achieved.
# If true, return 0 - the set can be partitioned into two equal sum subsets - min diff is zero
# If false, traceback to the index in the last row of the DP table where the value is TRUE.
# This is the largest sum we can form from a subset that's less than S/2 - the sum of the remaining elements minus this value will give the minimum difference.

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        s = sum(stones)
        n = len(stones)

        # Create a DP table of size (n) * (s/2 + 1)
        dp = [[False for _ in range(int(s/2) + 1)] for _ in range(n)]

        # The '0' th column will be true - you can always form a subset of size 0 by excluding all elements
        for i in range(n):
            dp[i][0] = True

        # With only one number, you can form a subset sum s/2 if the number == s/2
        for j in range(1, int(s/2)+1):
            dp[0][j] = stones[0] == j

        # Tabulate
        for i in range(1, n):
            for j in range(1, int(s/2)+1):
                # Include number at current index
                pick = False
                if j - stones[i] >= 0:
                    pick = dp[i-1][j-stones[i]]
                # Exculde number at current index
                dont_pick = dp[i-1][j]
                dp[i][j] = pick or dont_pick

        sum1 = 0
        # Traceback and find the last position where the value was True
        for i in range(int(s/2), -1, -1):
            if dp[n-1][i]:
                sum1 = i
                break

        sum2 = s - sum1
        return abs(sum2 - sum1)
