### Pastebin
Pastebin like services enable users to store plain text or images over the network (typically the Internet) and generate unique URLs to access the uploaded data. Such services are also used to share data over the network quickly, as users would just need to pass the URL to let other users see it.

#### Functional Requirements
- Users should be able to upload or “paste” their data and get a unique URL to access it.
- Paste size max 10 MB
- Users will only be able to upload text.
- Data and links will expire after a specific timespan automatically; users should also be able to specify expiration time.
- Users should optionally be able to pick a custom alias for their paste.
- User login/Anonymous

#### Non-Functional Requirements:
- The system should be highly reliable, any data uploaded should not be lost.
- The system should be highly available. This is required because if our service is down, users will not be able to access their Pastes.
- Users should be able to access their Pastes in real-time with minimum latency.
- Paste links should not be guessable (not predictable).

#### Capacity Estimations
- Assumptions:
  - Pastes: ~100k per day
  - Reads: ~10x Pastes -- READ HEAVY SYSTEM
- Traffic:
  - Writes: 100k per day ~ 4166 per hour
  - 100k/24/3600 per sec ~ 150 per sec
  - Reads: 1500 reads per second
- Data Storage:
  - Max: 10 MB per user ~ 1000GB per day (WORST CASE)
  - Average: 100 kB per user ~ 10GB per day (AVERAGE CASE)

#### Database Schema
- Do we really need to store all the data in DB?
    - We can offload the data to a static storage and save a reference to the blob in DB.
    - This would require external calls to get the data.
    - If we store everything in DB, DB IO would need to be very performant.
    - Hybrid approach - If the blob size is close to average (100 kB), store it in DB, else store it in S3 and save a reference url in DB.
    - A good startegy would be to store the data if it is <= 100kB. If it is > 100 kB, store a S3 url along with 100 kB of preview data that a user can see while the actual data loads from S3.

- Paste Table
  - PasteID
  - Content (100 kB)
  - S3_link
  - Created_at
  - Expire_at
- User Table
  - Id
  - Name
  - Created_at
  - Metadata

#### Design
![Serverless Design](https://i.imgur.com/Zv0qg2g.png)
- Key Generation - same as tinyURL
  - Distributed Key Generation - Twitter Snowflake - Strategy to generate a 64 bit key using:
    - Timestamp (41 bits)
    - Node Id - id corresponding to each node in the DKGS system (10 bits)
    -  A local counter on every node (10 bits)
    -  A random bit (1 bit)
- Async Cleanup Service:
  - Periodically checks all the records in the DB and purges expired records from DB and blob store.

#### Reading
- https://www.educative.io/courses/grokking-the-system-design-interview/3jyvQ3pg6KO
- https://www.youtube.com/watch?v=josjRSBqEBI
- https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake.html
- https://medium.com/better-programming/uuid-generation-snowflake-identifiers-unique-2aed8b1771bc



