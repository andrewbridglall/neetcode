class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # run dfs
        cache = {}
        def dfs(i, prev):
            # base case
            if i == len(nums):
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            # recursive case
            include = 0
            if nums[i] > prev:
                include = 1+dfs(i+1, nums[i])
            skip = dfs(i+1, prev)
            cache[(i,prev)] = max(include, skip)
            return cache[(i,prev)]
        return dfs(0, float('-inf')) 
