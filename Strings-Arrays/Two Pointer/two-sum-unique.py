# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

# Example 1:

# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:

# Input: nums = [1, 1], target = 2
# Output: 1
# Explanation:
# 1 + 1 = 2
# Example 3:

# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.

def uniquePairs(nums, target):
    diff_set = set()
    result = set()
    for n in nums:
        diff = target - n
        if diff in diff_set:
            if n < diff:
                result.add((n,diff))
            else:
                result.add((diff,n))
        diff_set.add(n)
    return len(result)

nums = [1,1,5,5]
target = 2
print(uniquePairs(nums,target))