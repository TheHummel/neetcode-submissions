class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)    # userId -> list of tweet ids
        self.followMap = defaultdict(set)     # userId -> set of user ids

        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.timestamp))

        self.timestamp -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        print("getnewsfeed", userId, self.followMap)

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            idx = len(self.tweets[followee]) - 1
            if idx >= 0:
                tweet, ts = self.tweets[followee][idx]
                heapq.heappush(minHeap, (ts, tweet, followee, idx))

        while len(res) < 10 and minHeap:
            ts, tweet, followee, idx = heapq.heappop(minHeap)
            res.append(tweet)

            if idx > 0:
                idx -= 1
                tweet, ts = self.tweets[followee][idx]
                heapq.heappush(minHeap, (ts, tweet, followee, idx))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
