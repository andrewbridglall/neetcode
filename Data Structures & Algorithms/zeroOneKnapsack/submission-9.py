class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dp soln
        N,M = len(weight), capacity
        # init dp array
        dp = [[0]*(M+1) for _ in range(N+1)]
        # base case - taken care of
        # iterate thru dp array
        for i in range(1, N+1):
            for c in range(1, M+1):
                # incl i-1
                incl = 0
                if c-weight[i-1] >= 0:
                    incl = profit[i-1] + dp[i-1][c-weight[i-1]]
                # skip i-1
                skip = dp[i-1][c]
                dp[i][c] = max(incl, skip)
        # return res dp n m
        return dp[N][M]
