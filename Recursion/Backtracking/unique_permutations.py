# 47. Permutations II
# Medium

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

def permuteUnique(nums):
    helper(nums, 0, [])
    
def helper(S, i, slate):
    # Base Case
    if len(S) == i:
        print(slate)
        return
    
    # Maintain a hashmap to track duplicates
    hmap = {}
    for pick in range(i,len(S)):
        # If elements not in hashmap, add it to hashmap and delegate task to subordinates, else do nothing (duplicate case already solved)
        if S[pick] not in hmap:
            hmap[S[pick]] = 1
            S[pick], S[i] = S[i], S[pick]
            slate.append(S[i])
            helper(S, i+1, slate)
            slate.pop()
            S[i], S[pick] = S[pick], S[i]

permuteUnique([1,1,2])
