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
            
        heap = MinHeap(10)
        for uid in set(users):
            for tweet in self.user_tweets.get(uid, []):
                heap.push(tweet)
        return [e[0] for e in heap.items()]

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


class MinHeap(object):
    def __init__(self, n):
        self.buf = []
        self.size = n
        self.curr_size = 0
        
    def push(self, item):
        if self.curr_size < self.size:
            self.buf.append(item)
            self.down_up(self.curr_size)
            self.curr_size += 1
        elif self.buf[0][1] < item[1]:
            self.buf[0] = item
            self.up_down(0)
            
    def items(self):
        while self.curr_size > 1:
            self.buf[0], self.buf[self.curr_size-1] = self.buf[self.curr_size-1], self.buf[0]
            self.curr_size -= 1
            self.up_down(0)
        return self.buf
            
    def down_up(self, i):
        parent = (i - 1) / 2
        if parent >= 0 and self.buf[parent][1] > self.buf[i][1]:
            self.buf[parent], self.buf[i] = self.buf[i], self.buf[parent]
            self.down_up(parent)
            
    def up_down(self, i):
        min_son = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < self.curr_size and self.buf[min_son][1] > self.buf[l][1]:
            min_son = l
        if r < self.curr_size and self.buf[min_son][1] > self.buf[r][1]:
            min_son = r
        if min_son == i:
            return
            
        self.buf[min_son], self.buf[i] = self.buf[i], self.buf[min_son]
        self.up_down(min_son)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.follow(1, 1)
print obj.getNewsFeed(1)
# userId = 10
# tweetId = 100
# followerId = 10
# followeeId = 11
# obj.postTweet(userId,tweetId)
# print obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
#
#
# obj.postTweet(followeeId, 99)
# print obj.getNewsFeed(userId)
# obj.unfollow(followerId,followeeId)