# 31. Next Permutation
# Medium

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    # Algorithm:
    # Find largest index i such that array[i − 1] < array[i].
    # (If no such i exists, then this is already the last permutation.)
    # Find largest index j such that j ≥ i and array[j] > array[i − 1].
    # Swap array[j] and array[i − 1].
    # Reverse the suffix starting at array[i].
    
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i == 0: # descending sequence
            nums.reverse()
            return

        k = i - 1

        # Find the successor of k in the subarray [k:]
        while nums[j] <= nums[k] and j >= 0:
            j -= 1

        # Swap nums[j] and nums[k]
        nums[j], nums[k] = nums[k], nums[j]

        # Reverse subsequence [k+1:]
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# Complexity Analysis:
# Time complexity : O(n). In worst case, only two scans of the whole array are needed.
# Space complexity : O(1). No extra space is used. In place replacements are done.