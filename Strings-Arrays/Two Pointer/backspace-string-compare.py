# 844. Backspace String Compare
# Easy

# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Returns the next valid character
        def get_next_valid_index(s, index):
            backspace = 0
            while index >= 0:
                if s[index] == '#':
                    backspace += 1
                elif backspace > 0: # Valid character followed by a backspace
                    backspace -= 1
                else: # Just a Valid character, no following backspaces
                    break
                    
                index -= 1
                
            return index
        
        index1 = len(S) - 1
        index2 = len(T) - 1
        
        while index1 >= 0 or index2 >= 0:
            i1 = get_next_valid_index(S, index1)
            i2 = get_next_valid_index(T, index2)
            
            if S[i1] != T[i2]:
                return False
            
            if i1 < 0 and i2 < 0:
                return True
            
            if i1 < 0 or i2 < 0:
                return False
            
            index1 = i1 - 1
            index2 = i2 - 1
            
        return True
    
# Complexity Analysis
# Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.
# Space Complexity: O(1).