# 1268. Search Suggestions System
# Medium

# Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed. 

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Example 3:

# Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
# Example 4:

# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]

from bisect import bisect_left
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        result = []
        curr = ''
        products.sort()
        for char in searchWord:
            curr += char
            i = bisect_left(products, curr)
            result.append([product for product in products[i:i+3] if product.startswith(curr)])
        return result
    
# Analysis:
# Sorting and searching cost O(n * m * log n) and O(L * m * logn), respectively; 
# Therefore,
# Time: O((n + L) * m * logn), 
# space: O(1) - excluding space cost of sorting and return List, 
# where m = average length of products, n = products.length, L = searchWord.length().