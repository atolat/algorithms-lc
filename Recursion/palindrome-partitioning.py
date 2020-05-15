# 131. Palindrome Partitioning
# Medium

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Example:

# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def isPalindrome(st):
            return st == st[::-1]
        
        def helper(S, slate):
            # Base
            if not S:
                res.append(slate[:])
                return
            
            # Recursive
            for i in range(1,len(S)+1):
                if isPalindrome(S[:i]):
                    slate.append(S[:i])
                    helper(S[i:], slate)
                    slate.pop()
                    
        helper(s,[])
        return res