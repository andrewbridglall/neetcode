class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # make dfs
        n = len(nums)
        cache = {}
        def dfs(i):
            # base case
            if i in cache:
                return cache[i]
            # recursive case
            maxlen = 0
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    maxlen = max(maxlen, dfs(j))
            cache[i] = 1+maxlen 
            return 1+maxlen
        # run dfs
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        # return maxlen
        return res