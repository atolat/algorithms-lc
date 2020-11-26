# 355. Design Twitter
# Medium

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:

# Twitter twitter = new Twitter();

# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);

# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);

# // User 1 follows user 2.
# twitter.follow(1, 2);

# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);

# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);

# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);

# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);

# 
from heapq import *
class Tweet:
    def __init__(self, tid, timestamp):
        self.tid = tid
        self.timestamp = timestamp
    
    def __lt__(self, other):
        return self.timestamp < other.timestamp
        
class User:
    def __init__(self, uid):
        self.uid = uid
        self.followed = set()
        self.tweets = []
        self.follow(uid)
    
    def follow(self, id):
        self.followed.add(id)
    
    def unfollow(self, id):
        if id in self.followed:
            self.followed.remove(id)
        
    def post(self, id, timestamp):
        tweet = Tweet(id, timestamp)
        self.tweets.append(tweet)

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user_map = collections.defaultdict(User)
          

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if not self.user_map.has_key(userId):
            user = User(userId)
            self.user_map[userId] = user
        self.user_map[userId].post(tweetId, self.time)
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = collections.deque()
        if userId not in self.user_map:
            return []
        minheap = []
        users = self.user_map[userId].followed
        for user in users:
            tweetList = self.user_map[user].tweets
            for tweet in tweetList:
                heappush(minheap, tweet)
                if len(minheap) > 10:
                    heappop(minheap)   
            
        while minheap:
            res.appendleft(heappop(minheap).tid)
        
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_map:
            user = User(followerId)
            self.user_map[followerId] = user
        if followeeId not in self.user_map:
            user = User(followeeId)
            self.user_map[followeeId] = user
        self.user_map[followerId].follow(followeeId)    
        
        
    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_map or followeeId == followerId:
            return
        self.user_map[followerId].unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)