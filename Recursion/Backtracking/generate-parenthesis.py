# 22. Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        def _helper(S, slate, left, right):
            # Base Case:
            if left + right == 2*S:
                results.append(''.join(slate[:]))
                return
            
            # Recursive Case
            # Add a left Brace
            if left < n:
                slate.append('(')
                _helper(S, slate, left + 1, right)
                slate.pop()
            
            # Add a right Brace
            if right < left:
                slate.append(')')
                _helper(S, slate, left, right + 1)
                slate.pop()
            
    
        _helper(n, [], 0, 0)
        return results
            