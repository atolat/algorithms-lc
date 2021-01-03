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

#### Crawling
A web crawler is a software program which browses the World Wide Web in a methodical and automated manner. It collects documents by recursively fetching links from a set of starting pages. Many sites, particularly search engines, use web crawling as a means of providing up-to-date data. Search engines download all the pages to create an index on them to perform faster searches.

Some other uses of web crawlers are:
- To test web pages and links for valid syntax and structure.
- To monitor sites to see when their structure or contents change.
- To maintain mirror sites for popular Web sites.
- To search for copyright infringements.
- To build a special-purpose index, e.g., one that has some understanding of the content stored in multimedia files on the Web.

**Features**
- Politeness/Crawl Rate - respect the upper limit of visit frequencies of websites.
- DNS query
- Distributed crawling
- Priority Crawling
- Duplicate detection

**Scale/Capacity Estimation**
- 900 million registered websites
  - 60% -> 500 million * 100 pages per site ~ 50 billion pages
  - 120 kB average page size
  - 6 peta bytes -> 3 PB compressed

**High Level Design**
- Seed Url's: Url's to start crawling.
- URL Frontier: Queue that gives the next priority url to crawl.
- Fetchers + Renderer: 
  - Fetcher - gets the content of the url. Gets the next url to fetch from the frontier. Fetches the content. A custom DNS resolver might be required to optimize requests.