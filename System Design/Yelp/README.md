### Yelp/Proximity Server
Proximity servers are used to discover nearby attractions like places, events, etc. If you haven’t used yelp.com before, please try it before proceeding (you can search for nearby restaurants, theaters, etc.) and spend some time understanding different options that the website offers.

#### Functional Requirements
- Users should be able to add/delete/update Places.
- Given their location (longitude/latitude), users should be able to find all nearby places within a given radius.
- Users should be able to add feedback/review about a place. The feedback can have pictures, text, and a rating.

#### Non Functional Requirements
- Users should have a real-time search experience with minimum latency.
- Our service should support a heavy search load. There will be a lot of search requests compared to adding a new place.

**Capacity Estimation**
- Main Table - Location Entry
  - ID UUID 32 bytes
  - Name str 256 bytes
  - Category 1 byte
  - GPS(latitude + longitude) 16 bytes
  - Description 1 kB
- ~ 1 MB for each location entry * (Total Entries) * Replication Factor + Year on increase
- 100k concurrent users 

- Choice of DB:
  - Our system needs to support high QPS
  - Consistency is not top priority
    - If a location's information changes, delays in updates are tolerable.
  - Choose NoSQL for location data, RDBMS for user profiles - MongoDB or Elastic Search
  - We need our DB to provide search support
    - full text 
    - GIS

**High Level Design**
![Design](https://i.imgur.com/rnTX2Qa.png)
- Read heavy system
- CDN is essential
- Photos uploaded by users can go through system's API gateway and then to S3 or directly to S3 using S3s SDK
- Memcached for caching user profiles and ratings
- Order management - STEP functions - BPMN(Business Process Management) - Business strategies represented as pictorial diagrams where each sequential step maps to an API.
- Anomaly detection - Logs -> Logstash -> Elasticsearch alerts.

**Location Based Search**
- Searching based on search space reduction on geospacial indices
- Use quad trees to store location information
- Partition Quad trees for availability and replication.
- https://medium.com/@waleoyediran/spatial-indexing-with-quadtrees-b998ae49336

#### Reading
- https://medium.com/@waleoyediran/spatial-indexing-with-quadtrees-b998ae49336
- https://www.educative.io/courses/grokking-the-system-design-interview/B8rpM8E16LQ
- https://youtu.be/TCP5iPy8xqo
- 
 