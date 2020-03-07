# 49. Group Anagrams
# Medium
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict
class Solution(object):
    # BF/Intuition
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         anamap = defaultdict(list)
#         results = []
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             anamap[sorted_word] = []
                
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             if sorted_word in anamap:
#                 anamap[sorted_word].append(word)
                
#         for key in anamap:
#             results.append(anamap[key])
            
#         return results
    
    # Optimal - Same Runtime as previous solution
    def groupAnagrams(self, strs):
        # Initialize a dictionary to store results
        # The values are a list of anagrams
        # The keys are a list of 0/1 - alphabet array with character counts
        # {
        # (0,0,1,1,1,0,...):[ate,tea],
        # ...
        # }
        results = defaultdict(list)
        for word in strs:
            # For every work in the list, initialize a 26 bit array
            count = [0] * 26
            for character in word:
                # For every character in the word, increment character 
                # count in the array by 1
                # this builds a unique key for every anagram
                count[ord(character)-ord('a')] += 1
            # Gather anagrams, convert to a tuple, list is unhashable
            results[tuple(count)].append(word)
        return results.values()
