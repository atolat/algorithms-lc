# 621. Task Scheduler
# Medium

# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.


# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

from collections import Counter
from heapq import *


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        maxheap = []
        intervals = 0
        freq_map = Counter(tasks)

        for task, freq in freq_map.items():
            heappush(maxheap, (-freq, task))

        while maxheap:
            # Try to execute n + 1 tasks per iteration
            # Task + n cooldown
            m = n + 1
            waitlist = []
            while m > 0 and maxheap:
                freq, task = heappop(maxheap)
                intervals += 1
                # Execute task, decrement frequency and add to waitlist
                if -freq > 1:
                    waitlist.append((task, freq + 1))
                m -= 1

            # Once we are out:
            # Either maxheap is empty - All tasks are executed
            # Or m == 0 - current iteration is complete
            # Add waitlisted tasks to back to heap...
            for task, freq in waitlist:
                heappush(maxheap, (freq, task))

            # Now, if the maxheap still has tasks,
            # we need to add the remaining cycles m as idle cycles
            if maxheap:
                intervals += m

        return intervals

# Time complexity #
# The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of tasks. 

# Space complexity #
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ tasks in the HashMap.
