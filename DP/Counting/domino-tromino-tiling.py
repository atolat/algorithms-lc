# 790. Domino and Tromino Tiling
# Medium

# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

# XX  <- domino

# XX  <- "L" tromino
# X
# Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

# (In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

# Example:
# Input: 3
# Output: 5
# Explanation: 
# The five different ways are listed below, different letters indicates different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY

class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        if N == 0: return 0
        if N == 1: return 1
        if N == 2: return 2
        
        tableF = [None] * (N+1)
        tableU = [None] * (N+1)
        #tableL = [None] * (N+1)
        
        # Base Cases
        tableF[1] = 1
        tableF[2] = 2
        
        tableU[1] = 1
        tableU[2] = 2
        
        # tableL[1] = 1
        # tableL[2] = 2
        
        for i in range(3, N+1):
            tableF[i] = (tableF[i-1] + tableF[i-2] + tableU[i-2] + tableU[i-2]) % MOD
            tableU[i] = (tableF[i-1] + tableU[i-1]) % MOD
            # tableL[i] = (tableF[i-1] + tableU[i-1] )% MOD
            
        return tableF[N]