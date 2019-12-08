# 784. Letter Case Permutation
# Easy

# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

# Use general strategy to solve combinatorial problems:


class Solution(object):
    def letterCasePermutation(self, S):
        # Global copy of results array, if this is defined inside helper, it is empty with every recursive call to the function
        result = []

        def helper(S, i, slate):
            # Base Case
            if len(S) == i:
                result.append(slate[:])
                return
            # For alphabets, delegate two subordinates -- lowercase, uppercase
            if S[i].isalpha():
                helper(S, i+1, slate+S[i].lower())
                helper(S, i+1, slate+S[i].upper())
            # For numbers, delegate one helper -- include the number directly
            else:
                helper(S, i+1, slate + str(S[i]))

        helper(S, 0, "")
        return result

# Solution using mutable slate -- O(n) space


class Solution(object):
    def letterCasePermutation(self, S):
        result = []

        def helper(S, i, slate):
            if len(S) == i:
                result.append(''.join(slate[:]))
                return
            if S[i].isalpha():
                slate.append(S[i].lower())
                helper(S, i+1, slate)
                slate.pop()
                slate.append(S[i].upper())
                helper(S, i+1, slate)
                slate.pop()
            else:
                slate.append(S[i])
                helper(S, i+1, slate)
                slate.pop()

        helper(S, 0, [])
        return result