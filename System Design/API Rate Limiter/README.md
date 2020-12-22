### API Rate Limiter

#### Functional Requirements:
- Limit the number of requests an entity can send to an API within a time window, e.g., 15 requests per second.
- The APIs are accessible through a cluster, so the rate limit should be considered across different servers. The user should get an error message whenever the defined threshold is crossed within a single server or across a combination of servers.

#### Non-Functional Requirements:
- The system should be highly available. The rate limiter should always work since it protects our service from external attacks.
- Our rate limiter should not introduce substantial latencies affecting the user experience.


#### Notes

Rate Limiting is a process that is used to define the rate and speed at which consumers can access APIs. Throttling is the process of controlling the usage of the APIs by customers during a given period. Throttling can be defined at the application level and/or API level. When a throttle limit is crossed, the server returns HTTP status “429 - Too many requests".


##### Algorithms
- **Token Bucket**
  - For every unique user:
    - Get a token from the bucket if not present
    - If present, track last request time andd update token (decrease number of allowed requests if request is made within minimum duration or reset the count if request is made in a new duration).
    - EG: 5 req per minute per user
      - user U1 make a request at 11:01:10
      - BUCKET: U1 : 11:01:10 :: 4 -- UPDATE
      - U1 makes request at 11:01:25
      - BUCKET: U1 : 11:01:25 :: 3 -- UPDATE
      - U1 makes request at 11:03:10
      - BUCKET: U1 : 11:03:10 :: 4 -- RESET 
      - U1 makes request at 11:03:12
      - BUCKET: U1 : 11:03:12 :: 3 -- UPDATE
      - U1 makes request at 11:03:15
      - BUCKET: U1 : 11:03:15 :: 2 -- UPDATE
      - U1 makes request at 11:03:20
      - BUCKET: U1 : 11:03:20 :: 1 -- UPDATE
      - U1 makes request at 11:03:25
      - BUCKET: U1 : 11:03:25 :: 0 -- UPDATE
      - U1 makes request at 11:03:35
      - BUCKET: U1 : 11:03:35 :: 0 -- REJECT! -- TOO MANY REQUESTS

- **Leaky Bucket**
  - FIFO Queue - Requests come in at one end of the queue. There is a request processor at the other end that processes requests at x req/sec.
  - The queue has a finite capacity. Once number of requests exceed capacity, any further requests are rejected (overflow from the bucket).
  
- **Fixed Window Counter**
  - A fixed window for every time interval
  - EG: 10 req / min
    - U1 makes a req at 11:00:05
    - Counter U1_11_00: 0
    - U1 makes a req at 11:00:10
    - Counter U1_11_00: 1
    - ... Till U1_11_00: 10
    - For the next minute U1_11_01: 0 ... 
  - If there are many requests near the end of the window and beginning of the next window, the server will be overloaded.
    - EG 10 requests between 11:00:55 and 11:00:59 and 10 requests between 11:01:01 and 11:01:10 --> 20 requests in the duration 11:00:55 - 11:01:10 - server is overloaded.
  - Traffic is not smoothened or buffered.

- **Sliding Logs**
  - Maintain a hashtable with key as user id and val as an array of requests.
  - The requests are sorted by timestamp.
  - Everytime a new request comes in:
    - filter the user's array 
    - remove entries that are older than the duration
    - count how many requests were served in the current interval
    - if this doesn't exceed the rate limit, accept the request and add an entry, else reject the request
  - Downside - consumes a lot of memory

- **Sliding Window Counter**
  - Similar to previous algorithm, here in the array we maintain timestamp:count pairs as entries
  - EG U1: [(ts+01:3), (ts+03:2), (ts+05:3) ...] -> 1st second - 3 requests, 3rd second - 2 requests, ...
  - When a new request comes in, the array is filtered to remove older entries, if the sum of requests in the array is less than the rate, the current request is accepted and the corresponding timestamp counter is incremented.

**Problems in distributed systems**:
- Rate Limit Data Inconsistency: If a request is made to different nodes in different regions at the same time, the rate might not be updated in the DB and extra requests might be served - Sticky sessions - direct requests from a user to a single region/LB
- Race conditions - use LOCKS

