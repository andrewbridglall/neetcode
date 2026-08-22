class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # true dp soln
        # build cache
        n, m = len(profit), capacity
        cache = [[0]*(m+1) for _ in range(n)]
        # populate first row - assume access to item 0 only with changing cap
        for cap in range(m+1):
            if weight[0] <= cap:
                cache[0][cap] = profit[0]
        # iterate row by row through cache
        for i in range(1, n):
            for cap in range(1, m+1):
                # include or skip and store max profit
                skip = cache[i-1][cap]
                include = 0
                newcap = cap - weight[i]
                if newcap >= 0:
                    include = profit[i]+cache[i-1][newcap]
                cache[i][cap] = max(skip, include)
        return cache[n-1][m]
                