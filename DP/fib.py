509. Fibonacci Number
Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # return self.recursiveFib(N)
        # return self.memoFib(N)
        return self.tabFib(N)
        
    # Recursive
    def recursiveFib(self, N):
        if N == 0 or N == 1:
            return N
        else:
            return self.recursiveFib(N-1) + self.recursiveFib(N-2)
        
    # Bottom Up Memoization
    def memoFib(self, N):
        memo = collections.defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        
        if N in memo:
            return memo[N]
        else:
            memo[N] = self.memoFib(N-1) + self.memoFib(N-2)
            return memo[N]
        
    # Top Down Tabulation
    def tabFib(self, N):
        if N == 0 or N == 1:
            return N
        
        table = [None] * (N+1)
        table[0] = 0
        table[1] = 1
        
        for i in range(2, N+1):
            table[i] = table[(i-1)] + table[(i-2)]
        return table[N]