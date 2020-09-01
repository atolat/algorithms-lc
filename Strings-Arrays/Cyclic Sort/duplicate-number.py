# 287. Find the Duplicate Number
# Medium

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3

## I ##
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Cyclic Sort
        i = 0
        while i < len(nums):
            # What number is expected at i?
            expected = i + 1
            if expected != nums[i]:
                # What index should the number be at?
                index = nums[i] - 1
                if nums[index] != nums[i]:  # swap
                    nums[index], nums[i] = nums[i], nums[index]
                else:  # Found the duplicate
                    return nums[i]
            else:
                i += 1

        return -1

## II ##
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Floyd's Algorithm
        tortoise, hare = nums[0], nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        ptr1 = nums[0]
        ptr2 = tortoise

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
