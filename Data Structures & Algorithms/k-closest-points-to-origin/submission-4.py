class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calc distance
        def distance(i):
            return (points[i][0]**2 + points[i][1]**2)**(0.5)
        # add to minheap
        res = []
        minheap = []
        for i in range(len(points)):
            minheap.append([distance(i), i])
        heapq.heapify(minheap)
        # pop k times from minheap
        for _ in range(k):
            _, i = heapq.heappop(minheap)
            res.append(points[i])
        # append k points to res
        # return res
        return res