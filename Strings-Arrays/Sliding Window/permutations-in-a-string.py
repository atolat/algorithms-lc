# 567. Permutation in String
# Medium

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        start = 0
        pattern_map = collections.Counter(s1)
        matched = 0
        
        for end in range(len(s2)):
            end_char = s2[end]
            if end_char in pattern_map:
                pattern_map[end_char] -= 1
                if pattern_map[end_char] == 0: # Character matched pattern
                    matched += 1
            
            # Check if window size is equal to pattern
            # If not, shrink
            if end - start + 1 > len(s1):
                start_char = s2[start]
                if start_char in pattern_map:
                    if pattern_map[start_char] == 0:
                        matched -= 1
                    pattern_map[start_char] += 1
                start += 1
                
            if matched == len(pattern_map):
                return True
            
        return False

# Time Complexity #
# The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

# Space Complexity #
# The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap.