# 392. Is Subsequence
# Easy

# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge Case
        if len(s) > len(t):
            return False

        # Two Pointers
        s_ptr, t_ptr = 0, 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1

        return s_ptr == len(s)
