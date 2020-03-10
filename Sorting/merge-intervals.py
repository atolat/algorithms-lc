# 56. Merge Intervals
# Medium

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Edge Case
        if len(intervals) < 2: return intervals
        intervals.sort()
        # Results...
        merged = []
        current_interval = intervals[0]
        merged.append(current_interval)
        
        for interval in intervals[1:]:
            current_start = current_interval[0]
            current_end = current_interval[1]
            next_start = interval[0]
            next_end = interval[1]
            
            if next_start <= current_end:
                # Overlap, update current_interval
                current_interval[1] = max(current_interval[1], next_end)
            else: # No overlap
                # Update current interval
                current_interval = interval
                merged.append(current_interval)
                
        return merged