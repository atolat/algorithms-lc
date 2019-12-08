# 77. Combinations
# Medium

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


def combine(n, k):
    S = []
    for i in range(1,n+1):
        S.append(i)
    helper(S, 0, k, [])
    
def helper(S, i, k, slate):
    # Backtracking Case
    if len(slate) == k:
        print(slate[:])
        return
    # Base Case
    if len(S) == i:
        return
    # Recursive Case
    # Exclusion Case
    helper(S, i + 1, k, slate)
    
    # Inclusion Case
    slate.append(S[i])
    helper(S, i + 1, k, slate)
    slate.pop()

combine(4,2)