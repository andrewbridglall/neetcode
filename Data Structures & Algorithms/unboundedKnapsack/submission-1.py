class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # memoization of bf soln

        # build cache
        N,M = len(profit), capacity
        cache = [[-1]*(M+1) for _ in range(N)]
        # define dfs with cache
        def memo(i, c, cache):
            # base case
            # if i oob
            if i == len(profit):
                return 0
            # val in cache
            if cache[i][c] != -1:
                return cache[i][c]
            # recursive case
            # skip item i 
            skip = memo(i+1, c, cache)
            # include item i
            include = 0
            if c-weight[i] >= 0:
                include = profit[i] + memo(i, c-weight[i], cache)
            # assign cache at i,c to max skip, include
            cache[i][c] = max(skip, include)
            # return val
            return cache[i][c]
        # call dfs and return
        return memo(0, capacity, cache)