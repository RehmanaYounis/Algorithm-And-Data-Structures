class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap=defaultdict(set)
        self.tweetMap=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count-=1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap=[]
        self.followerMap[userId].add(userId)
        for followee in self.followerMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) -1
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index-1])
        res=[]
        while minHeap and len(res) <10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                newCount, newTweet= self.tweetMap[followee][index]
                heapq.heappush(minHeap,[newCount, newTweet, followee, index-1] )
        return res
    
    
   
      
    
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)