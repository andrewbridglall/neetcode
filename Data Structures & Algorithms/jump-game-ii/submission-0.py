class Solution:
    def jump(self, nums: List[int]) -> int:
        # bf
        # init vars
        n = len(nums)
        cache = {}
        # dfs - given index, returns min steps to reach n-1
        # run dfs
        def dfs(i):
            # base case
            if i >= n-1:
                return 0
            if i in cache:
                return cache[i]
            # recursive case
            minSteps = float('inf')
            for j in range(nums[i], 0, -1):
                minSteps = min(minSteps, 1 + dfs(i+j))
            cache[i] = minSteps
            return minSteps
        # return dfs result
        return dfs(0)