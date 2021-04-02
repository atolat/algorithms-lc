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

- **How to store an inverted index?**
  - Dictionary in RAM, where keys are the terms and values represent a segment offset on disk for the postings list of the term.
  - Since the terms are lexicographically sorted, we need not store all the terms in dictionary. 
    - EG: brutal, brute, brutus - we can store only brute in RAM. When we get a query for brute, find the ancestor - brutal, retrieve a block from disk and look up the successor terms till brute is found. 
    - We can use this to answer range queries too - eg words starting with brut*
    - This representation where the postings lists appear in sorted order of terms is called a *SSTable - Sorted String Table*
    - https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/
    - ![SSTable](https://www.igvita.com/posts/12/xsstable.png.pagespeed.ic.IkMoqaKZX9.webp)

- **Distributed File System & Map Reduce**
  - A large scale search system can contain billions of documents that cannot fit on a single machine.
  - Google serves ~ 70,000 requests per second.
  - We need to scale the batch processing pipeline for index construction (*INDEXER*) as well as the online search microservice (*RETRIEVER*)
  - The documents to be index as well as the index need to be sharded across a large froup of machines.
  - Distributed file system with multiple documents concatenated into chunks that are stored on individual machines. Tags can identify the start and end of each document. A master node keeps track of the chunks and the corresponding chunk servers.
  - https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf
  - A batch processing pipeline can then work on multiple chunks in parallel to construct the index.
