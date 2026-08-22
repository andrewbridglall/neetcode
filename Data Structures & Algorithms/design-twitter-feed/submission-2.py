class Twitter:

    def __init__(self):
        # init follwer map uid -> set()
        self.timestamp = 0
        self.followerMap = defaultdict(set)
        # init tweets map uid -> [timestamp, tweetId]
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append to userId list of tweets
        self.tweetMap[userId].append([self.timestamp, tweetId])
        # increment timestamp
        self.timestamp +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # get all tweets from self and followers
        res.extend(self.tweetMap[userId])
        for f in self.followerMap[userId]:
            res.extend(self.tweetMap[f])
        # sort and get last 10 or sort desc and get 10 or until end of arr
        res.sort(reverse=True)
        newsFeed = []
        for i in range(min(10, len(res))):
            t, tweetId = res[i]
            newsFeed.append(tweetId)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        # u1 follows u2 - add u2 to u1's set
        if followerId == followeeId:
            return
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove u2 from u1's set
        if followerId == followeeId or followeeId not in self.followerMap[followerId]:
            return
        self.followerMap[followerId].remove(followeeId)
