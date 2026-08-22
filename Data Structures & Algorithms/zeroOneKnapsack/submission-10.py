class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dp soln
        N,M = len(weight), capacity
        # init dp array
        dp = [0]*(M+1)
        # base case - taken care of
        # iterate thru dp array
        for i in range(1, N+1):
            currdp = [0]*(M+1)
            for c in range(1, M+1):
                # incl i-1
                incl = 0
                if c-weight[i-1] >= 0:
                    incl = profit[i-1] + dp[c-weight[i-1]]
                # skip i-1
                skip = dp[c]
                currdp[c] = max(incl, skip)
            dp = currdp
        # return res dp n m
        return dp[M]
