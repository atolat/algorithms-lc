# 211. Design Add and Search Words Data Structure
# Medium

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.endOfWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(node, word):
            if not word:
                if node.endOfWord == True:
                    self.res = True
                return
            if word[0] == '.':
                for n in node.children.values():
                    dfs(n, word[1:])
            else:
                n = node.children[word[0]]
                if not n:
                    return
                dfs(n, word[1:])
        self.res = False
        node = self.root
        dfs(node, word)
        return self.res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
