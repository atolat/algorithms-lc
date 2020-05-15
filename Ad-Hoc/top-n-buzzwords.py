# You work on a team whose job is to understand the most sought after toys for the holiday season. A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different articles. You need to take these quotes and identify which toys are mentioned most frequently. Write an algorithm that identifies the top N toys out of a list of quotes and list of toys.

# Your algorithm should output the top N toys mentioned most frequently in the quotes.

# Input:
# The input to the function/method consists of five arguments:

# numToys, an integer representing the number of toys
# topToys, an integer representing the number of top toys your algorithm needs to return;
# toys, a list of strings representing the toys,
# numQuotes, an integer representing the number of quotes about toys;
# quotes, a list of strings that consists of space-sperated words representing articles about toys

# Output:
# Return a list of strings of the most popular N toys in order of most to least frequently mentioned

# Note:
# The comparison of strings is case-insensitive. If the value of topToys is more than the number of toys, return the names of only the toys mentioned in the quotes. If toys are mentioned an equal number of times in quotes, sort alphabetically.

# Example 1:

# Input:
# numToys = 6
# topToys = 2
# toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
# numQuotes = 6
# quotes = [
# "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
# "The new Elmo dolls are super high quality",
# "Expect the Elsa dolls to be very popular this year, Elsa!",
# "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
# "For parents of older kids, look into buying them a drone",
# "Warcraft is slowly rising in popularity ahead of the holiday season"
# ];

# Output:
# ["elmo", "elsa"]

# Explanation:
# elmo - 4
# elsa - 4
# "elmo" should be placed before "elsa" in the result because "elmo" appears in 3 different quotes and "elsa" appears in 2 different quotes.

import re, heapq

def topKitems(toys, quotes, K):
    results = []
    
    # Build a map to store toy frequency and quote count toys->[freq, quote_count]
    # Initialize this to 0,0 for each toy
    toy_freq = {toy:[0,0] for toy in toys}
    
    for quote in quotes:
        # For every quote, maintain a map of toy: T/F to check if the toy has already been added for that quote
        # Can be avoided ... optimize
        quote_toy = {toy : False for toy in toys}
        
        # For every word in the quote
        for word in quote.lower().split():
            # Sanitize the word, lower case, remove special characters
            word = re.sub('[^a-z]','',word)
            # If the word is a toy
            if word in toy_freq:
                # Update toy frequency and quote count
                toy_freq[word][0] += 1
                if quote_toy[word] is False:
                    toy_freq[word][1] += 1
                    quote_toy[word] = 1
    
    # Sorting Approach  
    # Sort by frequency - descending, quote_count - descending, toy name alphabetical 
    # Time complexity: O(W)+O(TlogT)
    # W - total number of words(quotes* words in each quote)
    # T - number of toys
    #Space complexity: O(T) -->(dictionary)

    # result = [w[0] for w in sorted(toy_freq.items(), key= lambda x: (-x[1][1], -x[1][0], x[0]))[:K]]
    
    # Heap Approach
    # Time complexity: O(W)+O(TlogN) ---> maintain heap of size N(max toys) at any time
    # W - total number of words(quotes* words in each quote)
    # T - number of toys
    # N - max number of toys to return
    # Space complexity: O(T) + O(N) -->(dictionary + heap)          

    toy_heap = []
    
    # Build a heap with [toy_freq, quote_count, toy]
    # Default heap is a min heap, multiply by -1 to get max heap
    for toy in toy_freq:
        freq, quote_count = toy_freq[toy][0], toy_freq[toy][1]
        toy_heap.append([-1*freq,-1*quote_count,toy])
    
    heapq.heapify(toy_heap)
    
    # Pop top K, returns the max
    for i in range(K):
        results.append(heapq.heappop(toy_heap)[2])

    print(results)

toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]

topKitems(toys,quotes,3)