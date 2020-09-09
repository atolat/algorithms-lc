# 322. Coin Change
# Medium

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize 1D array of size amount
        # Every value in the dp table represents:
        # table[i] = min number of coins to make amount i
        table = [float('+inf')]*(amount+1)
        
        # Base Cases
        table[0] = 0
        
        # Tabulation
        for i in range(1, amount+1):
            minval = float('+inf')
            for c in coins:
                if i - c >= 0:
                    minval = min(table[i-c], minval)
            table[i] = minval + 1
            
        return table[-1] if table[-1] != float('+inf') else -1