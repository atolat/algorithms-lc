# 387. First Unique Character in a String
# Easy

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        # Iterate over string, character by character
        # Check if the count of the character is 1 in the map
        # return index
        for idx, ch in enumerate(s):
            print(idx, ch)
            if count[ch] == 1:
                return idx     
        return -1