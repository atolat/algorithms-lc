# 354. Russian Doll Envelopes
# Hard

# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Note:
# Rotation is not allowed.

# Example:

# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

# DP Approach
# Time Complexity: O(n log n) + O(n^2)
# Space Complexity: O(n)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Edge Case
        if not envelopes:
            return 0

        # Sort the input array by index 0
        envelopes.sort(key=lambda x: x[0])

        # Initialize dp array - dp[i] - longest increasing subsequence at i
        dp = [1 for _ in range(len(envelopes))]
        maxlen = 1

        for i in range(1, len(envelopes)):
            for j in range(0, i):
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] != envelopes[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
                    maxlen = max(maxlen, dp[i])

        return maxlen

# Binary Search Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Edge Case
        if not envelopes:
            return 0

        # Sort the input array by index 0 in crereasing order and index 1 in decreasing order
        # Envelopes that are equal in index 0 can never be in the same increasing subsequence
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # Initialize aux array to hold the longest increasing subsequence so far
        aux = [envelopes[0][1]]

        for i in range(1, len(envelopes)):
            if envelopes[i][1] > aux[-1]:
                aux.append(envelopes[i][1])
            else:
                idx = bisect.bisect_left(aux, envelopes[i][1], 0, len(aux)-1)
                aux[idx] = envelopes[i][1]
        return len(aux)
