# 301. Remove Invalid Parentheses
# Hard

# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Example 1:

# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:

# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:

# Input: ")("
# Output: [""]

# Time Complexity: Exponential - O(2^n) + O(n)
# Space Complexity: O(N)
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # BFS
        q = collections.deque([s])

        # Boolean to track if valid string is found at a particular level
        found = False
        visited = set()
        result = []

        while q and not found:
            numnodes = len(q)
            for _ in range(numnodes):
                curr = q.popleft()
                # Check if the current string is valid, add to result and set found = True
                if self.isValid(curr):
                    found = True
                    result.append(curr)
                for i in range(len(curr)):
                    # If curr is not a parenthesis, continue
                    if curr[i] not in '()':
                        continue
                    # Generate neighbors by removing a parenthesis at each index
                    new_str = curr[:i] + curr[i+1:]
                    if new_str not in visited:
                        q.append(new_str)
                        visited.add(new_str)
        return result

    # Check if given string is valid
    def isValid(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0
