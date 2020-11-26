# 895. Maximum Frequency Stack
# Hard

# Implement FreqStack, a class which simulates the operation of a stack-like data structure.

# FreqStack has two functions:

# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


# Example 1:

# Input:
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].

# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].

# pop() -> returns 5.
# The stack becomes [5,7,4].

# pop() -> returns 4.
# The stack becomes [5,7].

from heapq import *
from collections import defaultdict


class Element:
    def __init__(self, num, freq, seq):
        self.num = num
        self.freq = freq
        self.seq = seq

    def __lt__(self, other):
        # higher frequency wins
        if self.freq != other.freq:
            return self.freq > other.freq
        # if both elements have same frequency, return the element that was pushed later
        return self.seq > other.seq


class FreqStack(object):

    def __init__(self):
        self.seq = 0
        self.freq_map = defaultdict(int)
        self.maxHeap = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freq_map[x] += 1
        heappush(self.maxHeap, Element(x, self.freq_map[x], self.seq))
        self.seq += 1

    def pop(self):
        """
        :rtype: int
        """
        x = heappop(self.maxHeap).num
        if self.freq_map[x] > 1:
            self.freq_map[x] -= 1
        else:
            del self.freq_map[x]
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
