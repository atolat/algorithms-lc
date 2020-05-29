# 49. Group Anagrams
# Medium
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Initialize a dictionary to store results
        # The values are a list of anagrams
        # The keys are a list of 0/1 - alphabet array with character counts
        # {
        # (0,0,1,1,1,0,...):[ate,tea],
        # ...
        # }
        def computeArray(s):
            array = [0]*26
            for char in s:
                array[ord(char) - ord('a')] += 1
                
            return tuple(array)
        
        s_map = collections.defaultdict(list)
        out = []
        for s in strs:
            arr = computeArray(s)
            s_map[arr].append(s)
        for v in s_map.values():
            out.append(v)
            
        return out

# Complexity Analysis
# Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. 
# Counting each string is linear in the size of the string, and we count every string.

# Space Complexity: O(NK), the total information content stored in ans.