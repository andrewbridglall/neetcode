class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count elts
        count = defaultdict(int)
        for n in nums:
            count[n] +=1
        # add to heap
        maxheap = []
        for num, freq in count.items():
            heapq.heappush(maxheap, ((-1)*freq, num))
        res = []
        for _ in range(k):
            _, num = heapq.heappop(maxheap)
            res.append(num)
        return res
        