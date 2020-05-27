# 159. Longest Substring with At Most Two Distinct Characters
# Medium

# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        start = 0
        freq_map = collections.defaultdict(int)
        maxlen = float('-inf')
        
        for end in xrange(len(s)):
            end_char = s[end]
            freq_map[end_char] += 1
            
            if len(freq_map) > 2:
                start_char = s[start]
                freq_map[start_char] -= 1
                if freq_map[start_char] <= 0:
                    del freq_map[start_char]
                start += 1
            maxlen = max(maxlen, end - start + 1)
            
        return maxlen if maxlen != float('-inf') else 0
    
# Complexity Analysis

# Time complexity : O(N) where N is a number of characters in the input string.
# Space complexity : O(1) since additional space is used only for a hashmap with at most 3 elements.