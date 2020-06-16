# 252. Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Example 1:

# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: [[7,10],[2,4]]
# Output: true
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) < 2: return True
        intervals.sort(key = lambda x:x[0])
        start = 0
        end = 1
        
        current_interval = intervals[0]
        
        for interval in intervals[1:]:
            current_start = current_interval[start]
            current_end = current_interval[end]
            next_start = interval[start]
            next_end = interval[end]
            
            if next_start < current_end:
                return False
            else:
                current_interval = interval
            
        return True
    
# Time complexity : O(n log n). 
# The time complexity is dominated by sorting. 
# Once the array has been sorted, only O(n) time is taken to go through the array and determine if there is any overlap.

# Space complexity : O(1). Since no additional space is allocated.
