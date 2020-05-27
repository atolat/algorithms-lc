# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        index_map = collections.defaultdict(int)
        maxlen = float('-inf')
        for end in range(len(s)):
            end_char = s[end]
            if end_char in index_map: # Repeated Character
                start = max(start, index_map[end_char]+1)
                
            index_map[end_char] = end
            maxlen = max(maxlen, end-start+1)
            
        return maxlen if maxlen != float('-inf') else 0