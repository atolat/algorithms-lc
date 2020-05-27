# 76. Minimum Window Substring
# Hard

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = 0
        min_length = float('+inf')
        pattern_map = collections.Counter(t)
        result = ""
        matched = 0
        
        for end in range(len(s)):
            end_char = s[end]
            if end_char in pattern_map:
                pattern_map[end_char] -= 1
                # If we have seen all occurances of character
                if pattern_map[end_char] == 0:
                    matched += 1
            
            # Pattern matched, let's shrink the window
            while len(pattern_map) == matched:
                # Update result
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    result = s[start:end+1]
                start_char = s[start]
                start += 1
                if start_char in pattern_map:
                    if pattern_map[start_char] == 0:
                        # This character was completely matched earlier
                        matched -= 1
                    pattern_map[start_char] += 1
                    
                    
        return result
    
# Time Complexity #
# The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

# Space Complexity #
# The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. 
# In the worst case, we also need O(N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.
                    