class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # init vars
        n = len(nums)
        maxheap = []
        res = []
        l = 0
        # iterate thru nums
        for r in range(n):
            # evict left
            if r-l+1 > k:
                l+=1
            # add right
            heapq.heappush(maxheap, [-1*nums[r], r])
            # add to res
            if r-l+1 == k:
                while maxheap[0][1] not in range(l,r+1):
                    heapq.heappop(maxheap)
                res.append(-1*maxheap[0][0])
        # return res
        return res