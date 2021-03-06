# 290. Word Pattern
# Easy

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p = pattern
        s = s.split(' ')
        s_map = {}
        p_map = {}

        if len(s) != len(p):
            return False

        for i in range(len(s)):
            s_char = s[i]
            p_char = p[i]

            if s_char in s_map:
                if s_map[s_char] != p_char:
                    return False

            if p_char in p_map:
                if p_map[p_char] != s_char:
                    return False

            s_map[s_char] = p_char
            p_map[p_char] = s_char

        return True
