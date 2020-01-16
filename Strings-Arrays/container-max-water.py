# 11. Container With Most Water
# Medium

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two pointers
        i = 0
        j = len(height) - 1
        max_area = -1
        min_height = sys.maxint
        
        while i<j:
            min_height = min(height[i],height[j])
            max_area = max(max_area, min_height*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area