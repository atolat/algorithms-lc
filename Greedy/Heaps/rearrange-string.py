# 767. Reorganize String
# Medium

# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"
# Example 2:

# Input: S = "aaab"
# Output: ""

from collections import Counter
from heapq import *
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        freq_map = Counter(S)
        maxheap = []
        result = []
        
        for char, freq in freq_map.items():
            heappush(maxheap, (-freq, char))
        
        prevChar, prevFreq = None, 0
        
        while maxheap:
            freq, char = heappop(maxheap)
            if prevChar and -prevFreq > 0:
                heappush(maxheap, (prevFreq, prevChar))
                
            result.append(char)
            prevChar = char
            prevFreq = freq + 1
            
        return "".join(result) if len(result) == len(S) else ""
    
# Time complexity #
# The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of characters in the input string.

# Space complexity #
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.