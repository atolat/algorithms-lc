### Scaling
- **Reasons to scale**:
  - may need to scale DB and cache tier if size of the **data** is too huge.
  - if the number of requests per second is too huge, need to **scale for throughput**.
  - if the **response time** is too high, need to **parallelize** computation.
  - **Availability/Reliability** in the face of faults
  - **Geolocation** - minimize network latency by using multiple servers at different locations.
  - **Hotspots** - disproportionately high load on a single piece of data.

- **Vertical Scaling**: scaling up, shared memory architecture
  - cost grows faster than linearly
  - has a ceiling

- **Horizontal Scaling**: scaling out, shared nothing architecture

- **Scaling for Data**:
  - **DB Estimates**: commodity machine - 2TB disk space
  - **Cache Estimates** - Assuming cache tier serves only read requests
    - 10% entries in cache -> 90% hit rate
    - 20% - 30% entries in cache -> 98% - 99% hit rate
    - 1 commodity machine - 128 GB RAM
- **Scaling for Throughput**:
  - Let x = time(in ms) needed to process a given request, by a single thread.
  - The tread can handle 1000/x back-to-back requests per second.
  - A typical commodity machine has 8-12 cores, 8 threads per core, 100 such threads per machine can serve (100*1000)/x requests per second. 
  - Realistic assumption ~ 30-40% CPU utilization ~ 30000/x requests per second.
  - In general, for a single commodity server
    - DB : x ~ 10 ms -> 3000 requests per second
    - Cache : x ~ 2 ms -> 15000 requests per second
    - App : x ~ 1 ms -> 30000 requests per second

**How do we measure performace of a scalable system?**
- **SLI (Service Level Indicator)**: A quantitative measure of the level of service being provided.
  - *Correctness*: Is the right data being returned?  
    - Error as a fraction of all requests.
  - *Availability*: Could we respond to the request? 
    - fraction of time the service is usable
    - fraction of well formed requests
  - *Throughput*: The number of requests per second that could be handled.
  - *Response Time*: Time taken to return a response to the client.
    - Look at p50, p85, p90, p95, p99 and try to optimize for p99.
- **SLO (Service Level Objective)**: A target value/range for an SLI.
  - EG: p50 < 200 ms and p99 < 1sec and availability > 99.9%
  - Functional requirements decide SLOs for correctness
  - Non functional requirements describe SLOs for availability, throughput, response time.
  - Scaling for data size, throughput, bulky service time, availability, geolocation and data hotspots also meant to satisfy SLOs.
- **Service Level Agreement**: An explicit/implicit contract with your users on what the SLOs are, including consequences of missing/meeting the SLOs (rebate/penalty).

**Latency vs Response Time**
- Latency: Duration that request is latent (awaiting service, not actually being served). Depends on 3 components:
  - Transmission Time = (Size of message/Bandwidth)
  - Propogation Delay = (Distance/Speed of light)
  - Queuing Delay
- Response Time (for client): Latency (round trip time) + Service time (at server)

**Reverse and Forward Proxy**
- A proxy is an intermediary between client and server. It defers all the work to the servers behind it.
- Reverse Proxy (server-side proxy) - it acts on behalf of the server. 
  - load balancer
  - decryption and encryption within the private n/w
- Forward Proxy (client-side proxy) - forwards client's request into the public internet from the client. Multiple clients share a forward proxy (super client). 
  - web cache
  - content filtering - clients unauthorized to access certain web content.

**Why use LB?**
- **Increase throughput** - handles 10x - 100x (100k - 1M qps) requests compared to app servers.
  - Policies:
    - Round Robin
    - Least number of active connections
    - Least response time
    - Weighted RR
    - Random RR
    - Hashing
- **Increase availability, reduce response time**
    - Heartbeat/Healthcheck for app servers
    - Take servers down servers one by one for upgrades
  - Local
    - Passive Backup LB (different machines - same IP) to prevent single point of failure.
  - Global
    - DNS-based LB: Multiple Active LBs with different IPs - DNS service returns different IP addresses to client.
    - IP Anycast: Multiple active LBs with same IP in different datacenters. Client request is directed to nearest router with the same Anycast IP addr (closest router - Dijkstra's algorithm).
 
### Replication
- **Single Leader Data Replication**
  - All writes go to a single replica - leader/primary/master
  - Other replicas are followers
  - Leader records all the write changes in a change log
  - Each follower follows change log to synchronize data
  - Read requests can be served by any replica 
  - If the leader fails, a new node is elected as leader.
  - ISSUE: Reads may sometimes see stale data until replication is completed.(INCONSISTENCY)
  - Eventually, the followers catch up with the leader (EVENTUAL CONSISTENCY - replication lag)
  - Strong Consistency - When clients can't tell the system is replicated.
- **Multileader Data Replication**
  - One leader in each datacenter. 
  - Use timestamps to achieve eventual consistency with respect to conflicting writes.
- **Leaderless Replication**
  - instead of a leader being the source of truth, a simple majority of replicas can be the source of truth.
  - when writing, send the write request to all replicas
  - once a majority of them ack the write, consider it successful
  - when reading, ask for everyone's opinion and take the majority view
  - what if one of the replicas fail?
    - add a timestamp to writes to discern the truth
  - N = number of replicas
  - W = number of replicas that need to ack the write request (write quorum)
  - R = number of replicas that need to ack the read request (read quorum)
  - As long as as R + W > N, we can figure out the true value.
  - For N = 3
    - W = 2, R = 2 -> Most fault tolerant. If one of the nodes fails, we can still get a successful read/write operation.
    - W = 3, R = 1 -> Writes take more time
    - W = 1, R = 3 -> Reads take more time
- **CAP Theorem**
  - When a distributed system is (network) partitioned, it can either be consistent (CP) or available (AP).
  - Consistent+Available(CA) is not a distributed system.
- **Content Distribution Networks**
  - Strategy to optimize reads
  - The client reads from a proxy cache (server-side) - APP + CACHE which stores popular content.
  - The DB can be in a different datacenter
  - A CDN is a geographically distributed collection of proxy cache servers.
- **Cache Reads and Writes**
    - Cache Aside: Cache and DB are disconnected. App layer maintains data synchronization bertween cache and DB.
    - Read Through Cache: Cacche is responsible for updating itself with DB. App reads only from cache. If there is a cache miss, cache fetches value from DB and updates itself. A write happens in the cache and percolated to the DB through the cache (Write-through). Write operations are slow.
    - Write Back/Write Behind: Writes happen only in cache. Data is written to DB from cache periodically or when the entry is evicted from cache. Writes are faster here but if the system crashes, there is a chance of stale data in DB.

### Sharding 
- Large amount of data that can't fit on a single machine or qps is so high that a single machine cannot handle it.
- Breaking up the data so it can fit on multiple machines is called sharding.
- Each k-v pair belongs to one partition or shard, each shard is replicated for high availability.
- Data must be distributed uniformly across all shards.
- When a partition or shard receives a disproportionate amount of traffic - HOTSPOT
- The mapping must be random and uniformly distributed across shards to prevent data hotspotting.
- Using hashing:
  - k-v pairs -> across 0 to s-1 shards
  - MD5(key) -> 128-bit string -> %s -> shard id
  - Requests to a key are routed by a partition aware LB/router
  - Adding/deleting shards would require re-hashing - expensive operation

- **Consistent Hashing**
  - 