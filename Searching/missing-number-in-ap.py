# 1228. Missing Number In Arithmetic Progression
# In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

# Then, a value from arr was removed that was not the first or last value in the array.

# Return the removed value.
# Example 1:

# Input: arr = [5,7,11,13]
# Output: 9
# Explanation: The previous array was [5,7,9,11,13].
# Example 2:

# Input: arr = [15,13,12]
# Output: 14
# Explanation: The previous array was [15,14,13,12].

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Use Binary Search Pattern
        
        # Calculate the common difference in AP
        # a0 = a0
        # a1 = a0 + d
        # a2 = a0 + 2d
        # ...
        # an = a0 + (n)d
        # => d = (an - a0) / n where n is number of elements in AP minus 1 (starts with 0)
        # In our case, since 1 element is missing, we divide by len(arr) 
        
        d = (arr[-1] - arr[0]) / len(arr) 
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start+end) // 2
            # Left Zones - Numbers in correct AP order, move to right Zone
            if arr[mid] == arr[0] + mid*d:
                start = mid + 1
            else: 
                end = mid - 1
        
        # At the boundary:
        # arr[start] is the first number after missing num
        # arr[end] is last number before missing num
        
        # if start != len(arr):
        #     return arr[start] - d
        # return arr[0]
        
        # OR
        
        return arr[end] + d
 