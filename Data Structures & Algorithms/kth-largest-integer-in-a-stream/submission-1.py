import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # make heap with heapq
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # if size heap > k and val > heap top, append to heap and remove top
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0] and len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
