# 76. Minimum Window Substring
# Hard

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Initialize map for T, convert s to a list
        count_map = Counter(t)
        string_list = list(s)
        
        # Initialize result, min_length
        result = ""
        min_length = float('inf')
        # Count keeps track of how many characters we have seen from t
        count = len(t)
        
        # Initialize window
        left,right = 0,0
        
        # Edge cases
        if len(t) > len(s): return ""
        if t == s: return t
        
        # Start...
        while right < len(s):
            # Check if the character is in t
            if count_map[string_list[right]] > 0:
                # Character is in t, decrease count
                count -= 1
            # In all cases decrease count in count_map
            # For the characters in t, this will be >= 0
            # For other characters -> negative
            count_map[string_list[right]] -= 1
            # Expand window
            right += 1
            
            # When count is 0, we have encountered all characters t
            # The substring contained within left and right is valid
            # Let's try to shrink the window...
            while count == 0:
                # increment count of left character before shrinking window
                # This means we are adding the character back to the map
                # Un-do what we did when we looked at the character
                count_map[string_list[left]] += 1
                
                # For characters in t, the counts will be positive
                # For all other characters, count in map will be negative or 0
                if count_map[string_list[left]] > 0:
                    # Update result
                    if right-left+1 < min_length:
                        min_length = right-left+1
                        result = string_list[left:right]
                    count += 1
                # Shrink Window
                left += 1
                
        
        return ''.join(result)
                    