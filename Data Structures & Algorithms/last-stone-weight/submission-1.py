class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            first, second = abs(first), abs(second)
            heapq.heappush(stones, -1*(first-second))
        
        if not stones:
            stones.append(0)
        return -1*stones[0]