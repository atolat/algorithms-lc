### Search Engine for boolean retrieval.

#### Functional Requirements
- Given a search string of terms, return all documents (document IDs) that contain all the terms in the string.
- Queries can be of the form:
  - *Caesar*
  - *Brutus AND Caesar*
  - *Caesar OR Cleopatra*
  - *NOT Calpurina*
- No free text queries
- No ranking

#### Non Functional Requirements
- High throughput
- Low Latency

#### Notes
- **Naive Approach**
  - Something like grep. Parse throught the whole corpus for every boolean query.
  - Very slow - O(corpus size)

- **Term Document Incidence Matrix**
  - Transform and conquer the problem - Transform the corpus into a adjacency matrix:
    - Terms along the rows, documents along the columns.
    - A '1' denotes the term is present in the document.
    - Use bitwise operations on the rows to get desired query results.
  - This is not a space efficient approach since most real word corpora can be transformed into a sparse matrix:
    - 1 million documents, 500,000 unique terms, ~ 1000 words per document
    - The adjacency matrix would have 500,000 rows, 1 million columns -> atmost 1000 1's per column

- **Inverted Index**
  - Adjacency list representation of the corpus - Hash Table/Balanced Search Tree
  - Keys - terms, Values - list of document ID's (Postings list)
  - Answering boolean queries is equivalent to finding the intersection/union of sorted lists - *O(x+y)*
  - *How to construct Inverted Index on Disk?*
    - The corpus might be large and the inverted index might not fit in memory
    - We can separate the dictionary of terms and postings lists, store the dictionary on RAM and postings lists on disk.
    - The postings lists can be concatenated end-to-end to form a postings file that is stored on disk
    - In order to construct a postings list on disk, after tokenizing and processing terms from documents, store them as (term, docID) pairs on disk.
    - Once all documnets are processed, sort these pairs - primary by term, secondary by docID.
    - Next, load all the pairs for a term from disk to RAM, construct the postings list and write it back to disk.
    - The key challenge here is to figure out how to sort the pairs on disk - this would require an *external sort* on disk. 
    - https://www.geeksforgeeks.org/external-sorting/
