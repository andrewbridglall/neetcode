class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # memo
        # build cache n x m
        N,M = len(profit), capacity
        cache = [[-1]*(M+1) for _ in range(N)]
        # build memo func

        # define dfs
        def memo(i, c, cache):
            # base case
            # i oob
            if i == len(profit):
                return 0
            # if in cache return val at pos
            if cache[i][c] != -1:
                return cache[i][c]
            # recursive case
            # skip item i
            skip = memo(i+1, c, cache)
            # include item i
            include = 0
            if c-weight[i] >= 0:
                include = profit[i] + memo(i+1, c-weight[i], cache)
            # get max skip and include
            # assign max to cache at i c
            cache[i][c] = max(skip, include)
            # return val
            return cache[i][c]
        # run dfs and return
        return memo(0, capacity, cache)