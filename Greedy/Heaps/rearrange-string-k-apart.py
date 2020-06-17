# 358. Rearrange String k Distance Apart
# Hard

# Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

# Example 1:

# Input: s = "aabbcc", k = 3
# Output: "abcabc" 
# Explanation: The same letters are at least distance 3 from each other.
# Example 2:

# Input: s = "aaabc", k = 3
# Output: "" 
# Explanation: It is not possible to rearrange the string.
# Example 3:

# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.

from heapq import *
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        
        freq_map = collections.Counter(s)
        
        maxheap = []
        
        for char, freq in freq_map.items():
            heappush(maxheap,(-freq, char))
        out = []
        q = collections.deque()
        while maxheap:
            freq, char = heappop(maxheap)
            
            out.append(char)
            q.append((char, freq + 1))
            if len(q) == k:
                char, freq = q.popleft()
                if -freq > 0:    
                    heappush(maxheap,(freq, char))
                    
        if len(out) == len(s):
            return "".join(out)
        return ""
    
# Time complexity #
# The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of characters in the input string.

# Space complexity #
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.