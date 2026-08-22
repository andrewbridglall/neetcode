class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # run dfs
        def dfs(i, prev):
            # base case
            if i == len(nums):
                return 0
            # recursive case
            include = 0
            if nums[i] > prev:
                include = 1+dfs(i+1, nums[i])
            skip = dfs(i+1, prev)
            return max(include, skip)
        return dfs(0, float('-inf')) 
