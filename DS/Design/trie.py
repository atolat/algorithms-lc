# 208. Implement Trie (Prefix Tree)
# Medium

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class TrieNode:
    # A trie node has a map for every character
    # Boolean to indicate if the character marks the end of word
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize with empty root
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        # Get the root
        current = self.root
        # For every character in the word:
        # Check if the node is present
        # If not, create a TrieNode for the character
        # Advance down the prefix tree
        for c in word:
            node = current.children.get(c)
            if node is None:
                node = TrieNode()
                current.children[c] = node
            current = node
        current.endOfWord = True
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            node = current.children.get(c)
            if node is None:
                return False
            current = node
        return current.endOfWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            node = current.children.get(c)
            if node is None:
                return False
            current = node
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)