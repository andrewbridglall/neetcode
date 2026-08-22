class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # bf
        # init vars
        n = len(nums)
        res = []
        # iterate thru all windows of size k
        for i in range(n-k+1):
            maxWindow = float('-inf')
            for j in range(i, i+k):
                maxWindow = max(maxWindow, nums[j])
            res.append(maxWindow)
        # calc max and append to res
        # return res
        return res