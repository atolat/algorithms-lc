# 4. Median of Two Sorted Arrays
# Hard

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Always perform binary search on smaller of two arrays
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
    
        # Initialize pointers
        start_X = 0
        end_X = len(nums1)
        x = len(nums1)
        y = len(nums2)
        partition_X = 0
        partition_Y = 0
        
        while start_X <= end_X:
            partition_X = (start_X + end_X) / 2
            partition_Y = ((x + y + 1) / 2) - partition_X
            
            maxLeftX = nums1[partition_X - 1] if partition_X != 0 else float('-inf')
            minRightX = nums1[partition_X] if partition_X != x else float('inf')
            
            maxLeftY = nums2[partition_Y - 1] if partition_Y != 0 else float('-inf')
            minRightY = nums2[partition_Y] if partition_Y != y else float('inf')
            
            # Partition Found
            if maxLeftX <= minRightY and minRightX >= maxLeftY:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY)) / 2.0
                else:
                    return max(maxLeftX,maxLeftY)
            elif maxLeftX > minRightY:
                end_X = partition_X - 1
            else:
                start_X = partition_X + 1
                