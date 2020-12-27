# 759. Employee Free Time
# Hard

# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.


# Example 1:

# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:

# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]

from heapq import *
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # Build a minheap [(start time, interval, employee id, interval id)]
        minheap = []
        # Insert the first interval for each employee in the minheap
        for emp_id, employee_interval in enumerate(schedule):
            heappush(
                minheap, (employee_interval[0].start, employee_interval[0], emp_id, 0))

        # Set the previous interval to the interval with smallest start time - top of heap
        previous_interval = minheap[0][1]
        free_time = []
        while minheap:
            current_interval_start, current_interval, emp_id, interval_id = heappop(
                minheap)
            # If there is no overlap, insert a free slot
            if current_interval.start > previous_interval.end:
                free_time.append(
                    Interval(previous_interval.end, current_interval.start))
                # Update the previous_interval to current interval
                previous_interval = current_interval
            # If the intervals overlap, update previous interval only if it has a greater end time
            else:
                if previous_interval.end < current_interval.end:
                    previous_interval = current_interval
            # Check if the current employee's schedule has more intervals
            # Insert the next interval
            if interval_id + 1 < len(schedule[emp_id]):
                next_interval = schedule[emp_id][interval_id+1]
                heappush(minheap, (next_interval.start,
                                   next_interval, emp_id, interval_id+1))
        return free_time
