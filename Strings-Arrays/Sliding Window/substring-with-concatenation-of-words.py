# 30. Substring with Concatenation of All Words
# Hard

# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# Example 1:

# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []

# https://www.educative.io/courses/grokking-the-coding-interview/N8nMBvDQJ0m

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == '' or len(words) == 0: return []
        word_freq = collections.Counter(words)
        word_count = len(words)
        word_length = len(words[0])
        
        results = []
        
        for i in range((len(s) - word_length * word_count) + 1):
            words_seen = collections.defaultdict(int)
            for j in range(word_count):
                next_word_index = i + j * word_length
                word = s[next_word_index:next_word_index + word_length]
                
                if word not in word_freq:
                    break
                
                words_seen[word] += 1
                
                if words_seen[word] > word_freq.get(word):
                    break
                    
                if j + 1 == word_count:
                    results.append(i)
                    
        return results
                    
# Time Complexity #
# The time complexity of the above algorithm will be O(N * M * Len) 
# where ‘N’ is the number of characters in the given string, ‘M’ is the total number of words, and ‘Len’ is the length of a word.

# Space Complexity #
# The space complexity of the algorithm is O(M) since at most, we will be storing all the words in the two HashMaps. 
# In the worst case, we also need O(N) space for the resulting list. 
# So, the overall space complexity of the algorithm will be O(M+N).