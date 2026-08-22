class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        curr = None
        for _ in range(k):
            curr = heapq.heappop(nums)
        return -1*(curr)