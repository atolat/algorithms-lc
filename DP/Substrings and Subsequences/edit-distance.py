# 72. Edit Distance
# # Hard

# # Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# # You have the following 3 operations permitted on a word:

# # Insert a character
# # Delete a character
# # Replace a character
# # Example 1:

# # Input: word1 = "horse", word2 = "ros"
# # Output: 3
# # Explanation:
# # horse -> rorse (replace 'h' with 'r')
# # rorse -> rose (remove 'r')
# # rose -> ros (remove 'e')
# # Example 2:

# # Input: word1 = "intention", word2 = "execution"
# # Output: 5
# # Explanation:
# # intention -> inention (remove 't')
# # inention -> enention (replace 'i' with 'e')
# # enention -> exention (replace 'n' with 'x')
# # exention -> exection (replace 'n' with 'c')

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(1+len(word2))] for _ in range(1+len(word1))]

        # Base Cases
        for col in range(1 + len(word2)):
            dp[0][col] = col

        for row in range(1 + len(word1)):
            dp[row][0] = row

        # Tabulate
        for row in range(1, 1 + len(word1)):
            for col in range(1, 1 + len(word2)):
                if word1[row - 1] == word2[col - 1]:
                    s = 0
                else:
                    s = 1
                dp[row][col] = min(dp[row-1][col] + 1, dp[row]
                                   [col-1] + 1, dp[row-1][col-1] + s)
        return dp[-1][-1]
