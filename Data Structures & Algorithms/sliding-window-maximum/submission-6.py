class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window soln
        # init vars
        n = len(nums)
        l = 0
        maxheap = []
        res = []
        # iterate thru nums
        for r in range(n):
        # for each new elt, add to window and maxheap
            heapq.heappush(maxheap, [-1*nums[r],r])
        # prune maxheap for elts whose index < l
            while maxheap[0][1] < l:
                heapq.heappop(maxheap)    
        # get maxheap top for max and append to res
        # window should be of size k
            if r-l+1 == k:
                res.append(-1*maxheap[0][0])
                l+=1
        # return res
        return res