### Distributed Cache
- High speed data storage systems that save transient data. Reuse computational results. 
- Stored in fast access memory RAM. 

#### Estimation
- Data range in Tera bytes
- 50k to 1M queries per second
- ~ 1 msec latency
- LRU eviction
- 100 % availability
- Scalable
  
**Best Practices**
- Validity
- High hit rate
- Low cache miss
- TTL

**Cache Access Patterns**
- Write Through: Write requests go to cache. Cache writes to DB. Write is acknowledged as successful only when data is written to cache and DB.
- Write Around: Writes happen only in DB. Cache is updated when the first cache miss occurs.
- Write Back: Write update goes to the cache and data is saved to the cache. A separate async service updates cache data to DB.

**Data Structures**
- [HashTable](../../DS/Design/HashTable.py)
- [LRU Cache](../../DS/Design/LRU-cache.py)

**Fault Tolerance**
- Regular interval snapshots of cache that are saved to disk.
- Log Reconstruction: Sequence of read/write operations appended to a log file by an async process to HDD. This log can be used to reconstruct the cache data.

**Availability**
- Sharding with replication
- Master Slave configuration

#### Reading
- https://www.youtube.com/watch?v=DUbEgNw-F9c
- https://gist.github.com/VarunVats9/5b785b7aed29eddfaf3436f16f607bcc
- https://codecapsule.com/2012/11/07/ikvs-implementing-a-key-value-store-table-of-contents/
- https://www.quora.com/Whats-the-maximum-throughput-in-queries-per-second-for-memcached-with-small-object-sizeshttp://www.tom-e-white.com/2007/11/consistent-hashing.html
- https://ivoroshilin.wordpress.com/2013/07/15/distributed-caching-under-consistent-hashing/
- https://gist.github.com/jboner/2841832




