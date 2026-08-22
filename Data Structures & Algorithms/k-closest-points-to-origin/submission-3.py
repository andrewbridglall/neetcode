class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create min heap to hold squared distance and point
        minheap = []
        for x,y in points:
            minheap.append((x**2+y**2, x,y))
        # heapify heap array by distance
        heapq.heapify(minheap)
        # pop k times and append point to res
        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(minheap)
            res.append([x,y])
        return res
