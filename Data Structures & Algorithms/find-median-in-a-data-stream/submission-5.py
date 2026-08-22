class MedianFinder:

    def __init__(self):
        # small maxheap
        # large minheap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # add to small default
        heapq.heappush(self.small, -1*num)
        # if small top > large top - move to large
        if self.large and -1*self.small[0] > self.large[0]:
            item = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, item)
        # if small > lg +1 - move to large
        # if lg > sm +1 - move to small
        if len(self.small) > len(self.large)+1:
            item = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, item)
        elif len(self.large) > len(self.small)+1:
            item = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*item)

    def findMedian(self) -> float:
        # if sm > lg - med in sm return top
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        # if lg > sm - med in lg return top
        elif len(self.large) > len(self.small):
            return self.large[0]
        # else even - get sm top lg top ret avg
        else:
            sm = -1*self.small[0]
            lg = self.large[0]
            return (sm+lg) / 2

        