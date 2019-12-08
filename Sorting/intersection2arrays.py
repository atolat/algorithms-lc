# 349. Intersection of Two Arrays
# Easy
# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.


def intersection_extra_space(nums1, nums2):
        set1 = set(nums1)
        result = set()
        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    result = []
    i = 0
    j = 0
    while i <= len(nums1)-1 and j <= len(nums2)-1:
            # if first element is greater than second or vice versa, increment one pointer
        if nums1[i] < nums2[j]:
            i += 1

        elif nums1[i] > nums2[j]:
            j += 1

        # Equal => check if result is empty or the last element is not equal to the current element (eliminate duplicates)
        else:
            if len(result) == 0 or result[len(result)-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
    return result


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
