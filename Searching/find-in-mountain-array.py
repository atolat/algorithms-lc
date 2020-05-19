# 1095. Find in Mountain Array
# Hard

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

# You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
 
 # """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def binary_search_ascending(start,end):
            while start <= end:
                mid = (start+end)//2
                mid_num = mountain_arr.get(mid)
                if mid_num == target:
                    return mid
                elif mid_num < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        def binary_search_descending(start,end):
            while start <= end:
                mid = (start+end)//2
                mid_num = mountain_arr.get(mid)
                if mid_num == target:
                    return mid
                elif mid_num < target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        # Find Peak
        start = 1
        end = mountain_arr.length() - 2
        peak_index = -1
        while start <= end:
            mid = (start+end)//2
            peak = mountain_arr.get(mid)
            peak_prev = mountain_arr.get(mid - 1)
            peak_next = mountain_arr.get(mid + 1)

            if peak > peak_prev and peak > peak_next:
                peak_index = mid
                break
            elif peak < peak_next:
                start = mid + 1
            else:
                end = mid - 1
        last = mountain_arr.length()-1
        target_index = binary_search_ascending(0, peak_index)
        if target_index != -1:
            return target_index
        return binary_search_descending(peak_index+1, last)