### TinyURL

#### Functional Requirements
- Given a URL, our service should generate a shorter and unique alias of it.
- When users access a short link, our service should redirect them to the original link.
- Users should optionally be able to pick a custom short link for their URL.
- Links will expire after a standard default timespan. Users should be able to specify the expiration time.

#### Non-Functional Requirements:
- The system should be highly available. This is required because, if our service is down, all the URL redirections will start failing.
- URL redirection should happen in real-time with minimal latency.
- Shortened links should not be guessable (not predictable).

#### Notes

- Use a key value store like a hash table to store shortURL as key and longURL as value. Insert/Search/Delete O(1)
- We have to encode the longURL and generate a unique key that also serves as the back half of the shortURL.

#### APIs
- encode(longURL) : shortURL
- decode(shortURL) : longURL

##### Algorithms
- **Simple counter**
  - Use a simple counter to generate a key. 
  - Everytime a longURL comes in, increment a global counter and make an entry in the hashtable.
  - Use the string version of the  counter as the back half for the shortURL.
  - Pros:
    - No collisions
  - Cons:
    - If we are not using any additional encoding, i.e., only digits 0-9 (base 10), the length of the short URL might grow too long (10 digits for billionth URL) - this scheme might not work well if we need a fixed size shortner.  
    - Predictable

- **Base62/64 Encoding**
  - Continuing from the previous scheme, use a higher base to encode the counter value.
  - We can shrink larger numbers to lesser characters using higher base for encoding.
  - If we work with base 64 (a-z, A-Z, 0-9, -, _) and use let's say length 7 for back half, we can generate 64^7 unique strings ~ 4 trillion.  
  - Pros:
    - Fixed length
    - No collisions
  - Cons: 
    - Predictable

- **Random Counter**
  - Continuing from the previous scheme, in order to make the URLs unpredictable, use a random number generator instead of a counter.
  - Pros:
    - Unpredictable
  - Cons:
    - Chance of collisions
    - Reduce collisions by increasing length

- **Cryptographic Hashing**
  - MD5 (128 bit), SHA-1 (160 bit), SHA-2, SHA-3, SH256...
  - LongURL -> CRYPT-HASH -> 128-bits digest -> base64 (encode groups of 6 bits) -> 22 chars -> Pick 6 chars as ShortURL
  - Higher probability of collision since we pick only a subset of the 128 bit digest
  - Hash functions are deterministic - same longURL maps to the same shortURL, short URL is not unique
    - This can be fixed- take a hash of longURL + counter/timestamp

- **Offline Key Generation**
  - Pregenerate short urls and store them in advance.
  - ShortURL is independent of LongUrl
  - No Collisions
  - Unpredictable
  - Need space to store pregenerated shortURLs

##### Scaling
###### Scaling for Capacity
- **Capacity Estimates**:
  - 2-3 billion short links every year - 73 queries per second
  - 20 billion clicks per month - 7700 queries per second
  - Reads:Writes ~ 100:1
  - Plan for ~3 yrs or 1000 days
    - Number of seconds per day ~ 100,000
    - Number of seconds in 3 yrs = 10^8
    - Number of K-V pairs = Q * 10^8, where q is number of queries per second
    - Here -> 73*10^8 ~ 10 billion K-V pairs
    - Key: shortURL ~ 34 bits to represent 10 billion, 6 bits are encoded as base64 character -> 6 characters ~ 6 bytes
    - Value: longURL ~ 2048 chars ~ 2kB
    - Size of each k-v pair ~ 2 kB
    - Total storage space = 10^8 * 2kB ~ 20TB
    - 1 commodity machine - 2TB ~ 10 machines
  - Each shard server will store 1/10 th of the data.
  - Each shard server replicated * 3 ~ 30 ccommodity machines in the DB tier.
  - **Cache Estimates** - Assuming cache tier serves only read requests
    - 10% entries in cache -> 90% hit rate
    - 20% - 30% entries in cache -> 98% - 99% hit rate
    - 2 billion k-v pairs <-> 4 TB
    - 1 commodity machine - 128 GB RAM ~ 30 machines
    - 90 sharded and replicated cache servers 
  
###### Scaling for Throughput
- Let x = time(in ms) needed to process a given request, by a single thread.
- The tread can handle 1000/x back-to-back requests per second.
- A typical commodity machine has 8-12 cores, 8 threads per core, 100 such threads per machine can serve (100*1000)/x requests per second. 
- Realistic assumption ~ 30-40% CPU utilization ~ 30000/x requests per second.
- In general, for a single commodity server
  - DB : x ~ 10 ms -> 3000 requests per second
  - Cache : x ~ 2 ms -> 15000 requests per second
  - App : x ~ 1 ms -> 30000 requests per second
- For TinyURL, Reads ~ 7700 qps, writes ~ 73 qps - a single commodity server is sufficient for the given traffic.