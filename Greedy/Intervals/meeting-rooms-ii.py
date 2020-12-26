# 253. Meeting Rooms II
# Medium

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:x[0]) # Sort intervals by start time
        
        if intervals is None or len(intervals) == 0 : 
            return 0
        
        # Initialize a minheap
        minHeap = []
        minHeap.append(intervals[0][1]) # Put End time of first meeting in heap
        
        # For every interval, check if the start time of the interval is greater than the 
        # end time of the meeting that ends the earliest
        # If this is the case, the new meeting starts after the earliest meeting ends -
        # Pop off the min element from heap -> Room is free
        # Append each new interval to the heap
        for interval in intervals[1:]:
            if minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval[1])
        
        # Length of the heap is the number of rooms required 
        return len(minHeap)