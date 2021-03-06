# 205. Isomorphic Strings
# Easy

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) where n is length of the string
# Did this run on Leetcode: Yes
# Any problems faced: No
# Approach:
# - Store mapping for exery character in the pattern with every word in the string and vice versa
# - If there is a mismatch at any point return False

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge Case
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in s_map:
                if s_map[s_char] != t_char:
                    return False
            if t_char in t_map:
                if t_map[t_char] != s_char:
                    return False
            s_map[s_char] = t_char
            t_map[t_char] = s_char
        return True
