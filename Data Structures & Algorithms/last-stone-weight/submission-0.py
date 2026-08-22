class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n < 2:
            return stones[0]
        # make init count of stones not zero - o(n)
        count = 0
        for stone in stones:
            if stone != 0:
                count +=1
        # while count >1 - worst case loop runs max/min times 
        while count > 1:
        # sort stones
            stones.sort()
        # take last two
        # "smash together" and update vals
            if stones[n-1] >= stones[n-2]:
                stones[n-1] = stones[n-1] - stones[n-2]
                stones[n-2] = 0
            else:
                stones[n-2] = stones[n-2] - stones[n-1]
                stones[n-1] = 0
        # update count - o(n)
            currCount = 0
            for stone in stones:
                if stone != 0:
                    currCount +=1
            count = currCount



        # iter through to find last nonzero stone if any -o(n)
        lastStone = 0
        for stone in stones:
            if stone != 0:
                lastStone = stone
        # return stone or 0
        return lastStone