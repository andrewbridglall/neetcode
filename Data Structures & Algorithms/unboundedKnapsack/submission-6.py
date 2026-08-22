class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # init vars
        N, M = len(weight), capacity
        # build dp arr
        dp = [[0]*(M+1) for _ in range(N+1)]
        # init base case - taken care of
        # iterate thru dp arr
        for i in range(1, N+1):
            for c in range(1, M+1):
                # incl item i-1
                incl = 0
                if c-weight[i-1] >= 0:
                    incl = profit[i-1] + dp[i][c-weight[i-1]]
                # skip item i-1
                skip = dp[i-1][c]
                # store max
                dp[i][c] = max(incl, skip)
        # return dp n m
        return dp[N][M]
