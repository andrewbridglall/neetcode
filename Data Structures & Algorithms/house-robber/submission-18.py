class Solution:
    def rob(self, nums: List[int]) -> int:
        # bf
        cache = {}
        def dfs(i):
            # base case
            # i oob - no more homese to rob
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            # recursive case
            # rob
            rob = nums[i] + dfs(i+2)
            # skip
            skip = dfs(i+1)
            # calc max
            cache[i] = max(rob,skip)
            return cache[i]
        return dfs(0)