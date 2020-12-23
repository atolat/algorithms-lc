### Search System

#### Functional Requirements
- Given a search string of terms, return all documents (document IDs) that contain all the terms in the string.

#### Non Functional Requirements
- High throughput
- Low Latency

#### Notes
- Indexing: Quick access to resources.
- Building blocks of a search engine:
  - Crawling - fetching web pages from the internet and storing it in a persistent storage.
  - Indexing - indexes webpages and emits metadata
  - Query Engine - Users use the query engine to retrieve results
- Inverted Index/Term document matrix:
  - tokenize all words, remove stop words and noise (remove urls, html, hashtags, etc.), stemming (get base word, remove suffixes), lemmatization (convert stemmed words to meningful words)
  - map terms to documents
  - 


