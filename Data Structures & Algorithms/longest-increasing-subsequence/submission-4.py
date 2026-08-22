class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # make dfs
        def dfs(i, j):
            # base case
            if i == len(nums):
                return 0
            # recursive case
            # include i
            incl = 0
            if j == -1 or nums[j] < nums[i]:
                incl = 1+dfs(i+1, i)
            # skip i
            skip = dfs(i+1, j)
            # return max incl skip
            return max(incl, skip)
        # run  dfs
        return dfs(0, -1)