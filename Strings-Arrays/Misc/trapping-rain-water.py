# 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Time Complexity: O(n)
# Space Complexity : O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height) - 1
        left_wall = height[0]
        right_wall = height[n]
        left = 0
        right = n-1
        result = 0
        while left <= right:
            if left_wall < right_wall:
                # Process left side
                if height[left] < left_wall:
                    # Can trap water
                    result += left_wall - height[left]
                else:
                    left_wall = height[left]
                left += 1
            else: # Process right side
                if height[right] < right_wall:
                    result += right_wall - height[right]
                else:
                    right_wall = height[right]
                right -= 1
        return result

        
        
        