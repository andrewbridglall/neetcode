class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bf - 2 branch recursion
        # init vars
        n = len(cost)
        cache = {}
        # make dfs
        def dfs(i):
            # base case
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            # recursive case
            left = dfs(i+1)
            right = dfs(i+2)
            cache[i] = cost[i] + min(left, right)
            return cost[i] + min(left, right)
        # run dfs
        return min(dfs(0), dfs(1))