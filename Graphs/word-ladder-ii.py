# 126. Word Ladder II
# Hard

# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        # Edge Case
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
        n = len(beginWord)

        # Preprocess words and build a graph
        # Key: intermediate words
        # Val: words from wordList that can be formed using intermediate words
        # EG: h*t: [hit, hot]
        word_combo = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                word_combo[word[:i] + '*' + word[i+1:]].append(word)
        ans = []
        # BFS
        q = collections.deque([(beginWord, [beginWord])])
        visited = set([beginWord])
        while q and not ans:
            local = set()
            level_size = len(q)
            for _ in range(level_size):
                current_word, path = q.popleft()
                for i in range(n):
                    intermediate_word = current_word[:i] + \
                        '*' + current_word[i+1:]
                    for word in word_combo[intermediate_word]:
                        if word == endWord:
                            ans.append(path+[word])
                        if word not in visited:
                            local.add(word)
                            q.append((word, path+[word]))
            visited = visited.union(local)
        return ans
