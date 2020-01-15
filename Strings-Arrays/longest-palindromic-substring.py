# 5. Longest Palindromic Substring
# Medium

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


def longestPalindrome(s):
    # Initialize two pointers to track palindromes
    s = list(s)
    i, left, right = 0, 0, 0
    result = []

    # Odd Length Palindromes
    for i in range(len(s)):
        left = i
        right = i
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        if len(result) < len(s[left+1:right]):
            result = s[left+1:right]

    # Even Length palindromes
    for i in range(len(s)):
        left = i
        right = i+1
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        if len(s[left+1:right]) > len(result):
            result = s[left+1:right]

    return result

print(longestPalindrome("babad"))