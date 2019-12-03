# 46. Permutations
# Medium

# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def permute(nums):
    helper([],nums)
    
def helper(slate,n):
    if len(n) == 0:
        print(slate)
    else:
        for x in n:
            slate.append(x)
            helper(slate, len(n)-1)
            slate.pop()

permute([1,2,3])