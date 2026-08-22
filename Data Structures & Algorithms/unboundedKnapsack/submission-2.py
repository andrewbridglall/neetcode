class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # true dp soln
        # build dp grid n x m
        N,M = len(profit), capacity
        dp = [[0]*(M+1) for _ in range(N)]

        # init first row, col
        for i in range(N):
            dp[i][0] = 0
        for c in range(M+1):
            if weight[0] <= c:
                dp[0][c] = (c//weight[0])*profit[0]
        # traverse grid row by row and col by col
        for i in range(1,N):
            for c in range(1, M+1):
        # calc skip i 
                skip = dp[i-1][c]
        # calc include i
                include = 0
                if c-weight[i] >= 0:
                    include = profit[i] + dp[i][c-weight[i]]
        # assign max
                dp[i][c] = max(skip, include)
        # end - return dp n-1 m
        return dp[N-1][M]