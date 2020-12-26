# 57. Insert Interval
# Hard

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i = 0
        start = 0
        end = 1
        
        # Find the last inteval in the current intervals that 
        # ends before the new interval starts.
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1
            
        # Now i is at the right position to insert
        # Check the next interval and see if it has a start that's earlier 
        # than the new interval's end - merge!
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1
        
        # Add the merged new interval to output
        merged.append(newInterval)
        
        # Add the remaining intervals to output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
            
        return merged
    
# Time complexity #
# As we are iterating through all the intervals only once, 
# the time complexity of the above algorithm is O(N), where ‘N’ is the total number of intervals.

# Space complexity #
# The space complexity of the above algorithm will be O(N) 
# as we need to return a list containing all the merged intervals.