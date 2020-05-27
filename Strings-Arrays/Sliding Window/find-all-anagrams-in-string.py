# 438. Find All Anagrams in a String
# Medium

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Same as # 567. Permutation in String
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        start = 0
        pattern_freq = collections.Counter(p)
        match = 0
        result = []
        
        for end in range(len(s)):
            end_char = s[end]
            if end_char in pattern_freq:
                pattern_freq[end_char] -= 1
                if pattern_freq[end_char] == 0:
                    match += 1
                    
            if end - start + 1 > len(p):
                start_char = s[start]
                start += 1
                if start_char in pattern_freq:
                    if pattern_freq[start_char] == 0:
                        match -= 1
                    pattern_freq[start_char] += 1
                    
            if len(pattern_freq) == match:
                result.append(start)
                
        return result