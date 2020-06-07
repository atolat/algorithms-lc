# 151. Reverse Words in a String
# Medium

# Given an input string, reverse the string word by word.

# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def trim_spaces(s):
            # s = s.strip()
            out = []
            start = 0
            end = len(s)-1
            while start < len(s) and s[start] == ' ':
                start += 1
            while end >= 0 and s[end] == ' ':
                end -= 1  
            while start <= end:
                if s[start] != ' ':
                    out.append(s[start])
                elif out[-1] != ' ':
                    out.append(s[start])
                start += 1
            return out
                
        
        def reverse_range(s, start, finish):
            while start < finish:
                s[start], s[finish] = s[finish], s[start]
                start, finish = start + 1, finish - 1
        
        s = trim_spaces(s)
        
        # Reverse whole string
        reverse_range(s, 0, len(s) - 1)
        
        # Reverse each word
        start = 0
        while True:
            finish = start
            while finish < len(s) and s[finish] != ' ':
                finish += 1
            if finish == len(s):
                break
            
            # Reverse Word
            reverse_range(s, start, finish-1)
            start = finish + 1
            
        # Reverse last word
        reverse_range(s, start, len(s)-1)
        
        return "".join(s)