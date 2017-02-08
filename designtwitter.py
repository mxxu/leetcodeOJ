class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_map = {}
        self.user_tweets = {}
        
        self.sort_id = 0
        
    def buildSortId(self):
        self.sort_id += 1
        return self.sort_id

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
            
        self.user_tweets[userId].insert(0, (tweetId, self.buildSortId()))
        self.user_tweets[userId] = self.user_tweets[userId][:10]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        users = [userId]
        if userId in self.follow_map:
            users.extend(self.follow_map[userId])
            
        tweets = []
        for uid in users:
            tweets.extend(self.user_tweets[uid])
        return sorted(tweets, key=lambda t: t[1], reversed=True)[:10]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()
            
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follow_map and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)