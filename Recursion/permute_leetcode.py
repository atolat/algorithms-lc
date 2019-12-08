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
    helper(nums,0,[])
    
def helper(S, i, slate):
    if len(S) == i:
        print(slate)
        return
    
    for pick in range(i, len(S)):
        S[i], S[pick] = S[pick], S[i]
        slate.append(S[i])
        helper(S, i+1, slate)
        slate.pop()
        S[pick], S[i] = S[i], S[pick]
        
    
permute([1,1,2])