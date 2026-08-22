class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # true dp soln
        # build dp grid
        N,M = len(profit), capacity
        dp = [[0]*(M+1) for _ in range(N)]
        # init first row col
        for i in range(N):
            dp[i][0] = 0
        for c in range(M+1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        # traverse grid row by row col by col filling in cells
        for i in range(1, N):
            for c in range(1, M+1):
                # calc skip
                skip = dp[i-1][c]
                # calc include
                include = 0
                if c-weight[i] >= 0:
                    include = profit[i] + dp[i-1][c-weight[i]]
                # fill with max
                dp[i][c] = max(skip, include)
        # outside loop return val at n-1 m
        return dp[N-1][M]