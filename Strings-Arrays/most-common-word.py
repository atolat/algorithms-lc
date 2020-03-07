# 819. Most Common Word
# Easy

# Example:

# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
 

# Note:

# 1 <= paragraph.length <= 1000.
# 0 <= banned.length <= 100.
# 1 <= banned[i].length <= 10.
# The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
# paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
# There are no hyphens or hyphenated words.
# Words only consist of letters, never apostrophes or other punctuation symbols.

from collections import defaultdict
import re

class Solution(object):
    def mostCommonWord(self,paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count = defaultdict(int)
        banned_set = set(banned)
        result = ''
        max_count = float('-inf')
        
        # Remove Special Characters
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        # Convert every word to lowercase and split
        for word in paragraph.lower().split():
            # If the word is not in the banned set
            # Add to map/increase count by 1
            if word not in banned_set:
                count[word] += 1
        # Result is the word with maximum count
        # Alternate - Faster, lesser memory
        for k,v in count.items():
            if v > max_count:
                max_count = v
                result = k
            
        # result = [k for k,v in count.items() if v == max(count.values())]

        return result