# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s):
    # Edge Cases
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1

    # Initialize pointers
    start = 0
    end = 0

    # Set longest substring length to 0
    longest = 0

    # Initialize map -- {'char at index' : index} with first entry
    char_map = {}
    char_map[s[0]] = 0

    while end < len(s) - 1:
        # Increment end pointer
        end += 1
        charAtIndex = s[end]

        # If charAtIndex is in the map and index is == start or greater than start, move start to index + 1
        if charAtIndex in char_map and char_map[charAtIndex] >= start:
            start = char_map[charAtIndex] + 1

        # Add charAtIndex to map
        char_map[charAtIndex] = end

        # Update the result
        if end - start + 1 > longest:
            longest = end - start + 1

    return longest
