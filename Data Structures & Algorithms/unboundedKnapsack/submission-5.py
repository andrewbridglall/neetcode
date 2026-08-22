class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # bf
        N,M = len(weight), capacity
        cache = {}
        # make dfs
        def dfs(i,cap):
            # base case
            if cap == 0 or i == N:
                return 0 # no more additional profit
            if (i,cap) in cache:
                return cache[(i,cap)]
            # recursive case
            # incl i
            incl = 0
            if cap - weight[i] >= 0:
                incl = profit[i] + dfs(i, cap-weight[i])
            # skip i
            skip = dfs(i+1, cap)
            # ret max
            cache[(i,cap)] = max(incl, skip)
            return max(incl, skip)
        # run dfs
        return dfs(0, capacity)