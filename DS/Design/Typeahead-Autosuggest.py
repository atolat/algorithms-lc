# 642. Design Search Autocomplete System
# Hard

# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
# Your job is to implement the following functions:

# The constructor function:

# AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

# Now, the user wants to input a new sentence. The following function will provide the next character the user types:

# List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:

# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".

# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".

# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

from collections import defaultdict
from heapq import *


class TrieNode:
    def __init__(self, word=None):
        # Each TrieNode has a map of the sentences with their hot counts
        self.children = collections.defaultdict(TrieNode)
        self.map = collections.defaultdict(int)


class Pair:
    def __init__(self, sentence, count):
        self.sentence = sentence
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.sentence > other.sentence
        return self.count < other.count


class AutocompleteSystem(object):
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        # Input keeps track of the characters being typed
        self.ip = ""
        # Build Trie and preload the nodes with given hot counts
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])

    def insert(self, sentence, count):
        curr = self.root
        for s in sentence:
            # Build Trie
            curr = curr.children[s]
            # Update the map at every TrieNode with sentence and count
            curr.map[sentence] += count

    def search(self, prefix):
        # Return the sentence map corresponding to a node if prefix is present
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return {}
            curr = curr.children[p]
        return curr.map

    def getValues(self, countMap):
        # Get the top 3 items from the map using a minheap
        heap = []
        for k, v in countMap.items():
            # Create a pair from sentence and count
            p = Pair(k, v)
            heappush(heap, p)
            # If there are more than 3 elements in heap, remove from heap
            if len(heap) > 3:
                heappop(heap)
        # At the end, we are left with the top 3 elements
        result = collections.deque()
        while len(heap) > 0:
            result.appendleft(heappop(heap).sentence)
        return result

    def input(self, c):
        # If we see an end character '#', insert the sentence in the trie and update count
        if c == '#':
            self.insert(self.ip, 1)
            self.ip = ""
            self.cursor = self.root
            return []
        self.ip += c
        countMap = self.search(self.ip)
        result = self.getValues(countMap)
        return result
