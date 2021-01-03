### Typeahead Suggestions/Autocomplete System

#### Functional Requirements
- As the user types in their query, our service should suggest top 10 terms starting with whatever the user has typed.
- Relevant or contextual results.

#### Non Functional Requirements
- The suggestions should appear in real-time. The user should be able to see the suggestions within 200ms.

#### Algorithms/Datastructures
- Use a prefix trie for prefix search
  - [Design](../../DS/Design/Trie.py)
  - O(l) retrieval - l is length of word
  - Space Optimized
- A naive approach is to use a trie to store all the terms.