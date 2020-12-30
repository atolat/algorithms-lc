#### Netflix/Video Streaming Service Design

**Functional Requirements:**
- Users should be able to upload videos.
- Users should be able to share and view videos.
- Users should be able to perform searches based on video titles.
- Our services should be able to record stats of videos, e.g., likes/dislikes, total number of views, etc.
- Users should be able to add and view comments on videos.

**Non-Functional Requirements:**
- The system should be highly reliable, any video uploaded should not be lost.
- The system should be highly available. Consistency can take a hit (in the interest of availability); if a user doesn’t see a video for a while, it should be fine.
- Users should have a real time experience while watching videos and should not feel any lag.

**High Level Design**
![Netflix](https://media-exp1.licdn.com/dms/image/C5112AQHVt9yrq8Br1Q/article-inline_image-shrink_1500_2232/0/1535206730604?e=1614816000&v=beta&t=bySQgxtDSJ4MN3M2lzhauUYMLy9OQLkWlozA9KMnSFQ)
- There are 3 main components:
  - Client - Devices that receive the content
    - Netflix client written in ReactJS
  - Backend - App tier, for netflix, anything that is not streaming related is handled by AWS.
  - Open Connect - Distributed CDN owned by Netflix.
    - A mix of origin servers (that contain the original content) and edge servers that hold copies that are geographically distributed.
  ![CDN](https://www.muvi.com/wp-content/uploads/2017/07/CDN_Muvi.png)
- ELB - Elastic Load Balancer - Load is balanced across zones (logical grouping of servers) first and then across instances. The first layer balances across zones usinf Round Robin.
  ![ELB](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/images/cross_zone_load_balancing_disabled.png)
- Video Onboarding - Before a video or movie is made available to a user, the video is conververted to different formats to support different devices at different bandwidths. This process is called transcoding.
  ![Transcoding](https://miro.medium.com/max/2280/1*TAsYF170okJzB61X51TDzg.png)
  - In order to support adaptive bitrate streaming multiple copies (~1200 files) of the same video are created in different resolutions. This is done using parallel workers working on chunks of a single video. The chunks are merged and uploaded to S3 and open connect servers.
- ZUUL - Gateway Service that provides dynamic routing, monitoring, resilience and security. 
  ![ZUUL](https://miro.medium.com/max/872/0*ycjEWsSKCaPemEg3.)
  - Netty Proxy - requests are proxied to inbound filters.
  - Inbound filters - authentication, routing, decorating requests.
  - Endpoint filters - return dtatic response or forward requests to backend services.
  - Outbound filters - zip content, add/remove headers to response, calculate metrics. 
  - Advantages of a gateway servers:
    - Rule based traffic sharding
    - Load Testing
    - Testing new services
    - Filter bad requests
- Hystrix - Latency and fault tolerant library designed to isolate the points of access the remote services. In microservice architecture, a single microservice depends on multiple microservices that may reside on different servers. This can result in cascading errors at certain endpoints. These cascading failures can be monitored and controlled in real-time using hystrix.
  - Every u-service is decorated and controlled by hysterix. The QoS of every service can be controlled by setting timeouts.
  - When the thread pool for a service is full, requests are rejected.
  - Services can be taken down if error rates are high.
- EV Cache - Custom cache client based on memcached. Implemented in RAM and SSD.
- DB - MySQL and Cassandra
  - All billing, tx info, user info is stored in MySQl
  - All other data is stored on cassandra
  - MySQL deployed on EC2 in Master-Master setup
    - Writes to mater are written to other master node before acknowledging the write request.
    - Reads are handled by read replicas - available locally (HA).
    - In case of master failure, writes are redirected to secondary master node.
  - Cassandra is redesigned to have smaller memory footprint, consistent R/W performance.
    - W:R ~ 9:1
    - Data segregated into live viewing history and compressed viewing history by scheduled jobs. 
    - Compressed data moved to different cassandra nodes.
- Kafka & Chukwa - Data+Event ingestion. 
  - 500 Billion events ~ 1.3 peta bytes per day - video viewing activity, UI activity, error logs, performance events, troubleshooting events.
  - Chukwa is an open source data collection system build on HDFS, Hadoop, MapR.
  - All the events from the different parts of the system are sent to Chukwa for monitoring. Chukwa forwards data to S3 and Kafka
  - Kafka routes this data to various sinks - Elasticsearch, Spark, etc.
- Elasticsearch - ingest chukwa data
  - ~ 150 clusters, ~ 3500 instances
  - Used for customer support
- Spark - ML, content recognization, recommendations
  - collaborative filtering
  - content based filtering

#### Reading
- https://www.educative.io/courses/grokking-the-system-design-interview/xV26VjZ7yMl
- https://medium.com/@NetflixTechBlog
- https://www.linkedin.com/pulse/system-design-netflix-narendra-l/?published=t
- https://www.infoq.com/presentations/Netflix-Architecture/
- https://chukwa.apache.org/
- https://netflixtechblog.com/announcing-zuul-edge-service-in-the-cloud-ab3af5be08ee
  