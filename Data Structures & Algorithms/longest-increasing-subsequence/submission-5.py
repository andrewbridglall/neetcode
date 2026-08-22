class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # make dfs
        cache = {}

        def dfs(i, j):
            # base case
            if i == len(nums):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # recursive case
            # include i
            incl = 0
            if j == -1 or nums[j] < nums[i]:
                incl = 1+dfs(i+1, i)
            # skip i
            skip = dfs(i+1, j)
            # return max incl skip
            
            cache[(i,j)] = max(incl, skip)
            return cache[(i,j)]
        # run  dfs
        return dfs(0, -1)