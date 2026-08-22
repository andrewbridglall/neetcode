class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # init vars
        N, M = len(weight), capacity
        # build dp arr
        dp = [0]*(M+1)
        # init base case - taken care of
        # iterate thru dp arr
        for i in range(1, N+1):
            currdp = [0]*(M+1)
            for c in range(1, M+1):
                # incl item i-1
                incl = 0
                if c-weight[i-1] >= 0:
                    incl = profit[i-1] + currdp[c-weight[i-1]]
                # skip item i-1
                skip = dp[c]
                # store max
                currdp[c] = max(incl, skip)
            dp = currdp
        # return dp n m
        return dp[M]
