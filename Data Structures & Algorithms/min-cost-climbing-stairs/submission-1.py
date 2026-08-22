class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bf - 2 branch recursion
        # init vars
        n = len(cost)
        # make dfs
        def dfs(i, cache):
            # base case
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            # recursive case
            left = dfs(i+1, cache)
            right = dfs(i+2, cache)
            cache[i] = cost[i] + min(left, right)
            return cost[i] + min(left, right)
        # run dfs
        zeroStart = dfs(0, {})
        oneStart = dfs(1, {})
        return min(zeroStart, oneStart)
        