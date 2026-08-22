class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # init vars
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            # pop two stones
            s1, s2 = -1*heapq.heappop(maxheap), -1*heapq.heappop(maxheap)
            diff = max(s1,s2)-min(s1,s2)
            if diff > 0:
                heapq.heappush(maxheap, -1*diff)
            # subtract
            # push if nonzero

        # return last stone if len > 0 else 0
        return -1*maxheap[0] if maxheap else 0 