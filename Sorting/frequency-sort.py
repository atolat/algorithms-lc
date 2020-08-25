# 451. Sort Characters By Frequency
# Medium

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

from collections import Counter
from heapq import *


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        op = ""
        maxheap = []
        freq_map = Counter(s)

        for key, value in freq_map.items():
            heappush(maxheap, (-1*value, key))

        while maxheap:
            freq, char = heappop(maxheap)
            op += char * (-1*freq)

        return op
