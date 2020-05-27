# 424. Longest Repeating Character Replacement
# Medium

# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

# In one operation, you can choose any character of the string and change it to any other uppercase English character.

# Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
 

# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        freq_map = collections.defaultdict(int)
        max_len = 0
        max_repeat_count = 0
        
        for end in xrange(len(s)):
            # Add char to freq_map
            freq_map[s[end]] += 1
            max_repeat_count = max(max_repeat_count, freq_map[s[end]])
            # Current window size is from start to end, overall we have a letter which is
            # repeating 'max_repeat_count' times, this means we can have a window which has one letter
            # repeating 'max_repeat_count' times and the remaining letters we should replace.
            # if the remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            if end - start + 1 - max_repeat_count > k:
                freq_map[s[start]] -= 1
                start += 1
            max_len = max(end - start + 1, max_len)
            
        return max_len
            
# Time Complexity #
# The time complexity of the above algorithm will be O(N) where ‘N’ is the number of letters in the input string.

# Space Complexity #
# As we are expecting only the lower case letters in the input string, we can conclude that the space complexity will be O(26),
# to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).