import collections
import heapq
class Twitter:
    '''
    getNewsFeed takes in userId, only want to return tweets by userId or ppl userId follows
    ordering does matter (most recent is first)

    {
        1: [2,3,4],
        2: [1,3]
    }

    {
        tweetId: (time, userId)
    }

    (-1, userId, tweetId)
    (-2, userId, tweetId)
    time = -2
    '''

    def __init__(self):
        self.user_follows = collections.defaultdict(set)
        self.time = -1
        self.main_feed = {}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.main_feed[tweetId] = ((self.time, userId, tweetId))
        self.time -= 1

        # if userId in self.main_feed:
        #     self.main_feed[userId].append((self.time, tweetId))
        # else:
        #     self.main_feed[userId] = [(self.time, tweetId)]
        
        # self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        followings = []
        minHeap = []
        if userId in self.user_follows:
            followings = self.user_follows[userId]
        
        # for user, tweets in self.main_feed.items():
        #     if user == userId:
        #         minHeap.extend(tweets)
        #     if len(followings) and user in followings:
        #         minHeap.extend(tweets)
        

        for tweet, pair in self.main_feed.items():
            time, other_user, tweetId = pair
            if other_user == userId:
                heapq.heappush(minHeap, pair)
            if len(followings) and other_user in followings:
                heapq.heappush(minHeap, pair)
                
        # heapq.heapify(minHeap)
        num = 0
        while len(minHeap):
            if num == 10:
                break
            time, user, tweetId = heapq.heappop(minHeap)
            posts.append(tweetId)
            num += 1
        
        return posts
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId) 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)