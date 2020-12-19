#### Network
#### OS
#### DB
- Hash Index: in-memory index/hashtable of key, val where val is an offset of the position of the key on disk to make disk lookups faster.
- 
#### Scaling
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

###### How do we measure performace of a scalable system?
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

###### Latency vs Response Time
- Latency: Duration that request is latent (awaiting service, not actually being served). Depends on 3 components:
  - Transmission Time = (Size of message/Bandwidth)
  - Propogation Delay = (Distance/Speed of light)
  - Queuing Delay
- Response Time (for client): Latency (round trip time) + Service time (at server)

###### Reverse and Forward Proxy
- A proxy is an intermediary between client and server. It defers all the work to the servers behind it.
- Reverse Proxy (server-side proxy) - it acts on behalf of the server. 
  - load balancer
  - decryption and encryption within the private n/w
- Forward Proxy (client-side proxy) - forwards client's request into the public internet from the client.       Multiple clients share a forward proxy (super client). 
  - web cache
  - content filtering - clients unauthorized to access certain web content.

###### Load Balancing
**Why use LB?**
- Increase throughput - handles 10x - 100x (100k - 1M qps) requests compared to app servers.
- Policies:
  - Round Robin
  - Least number of active connections
  - Least response time
  - Weighted RR
  - Random RR
  - Hashing
- Increase availability
  - Heartbeat/Healthcheck for app servers
  - Take servers down servers one by one for upgrades
- Passive Backup LB (different machines - same IP) to prevent single point of failure.
- Multiple Active LBs with different IPs - DNS service returns different IP addresses to client (DNS-based LB).
