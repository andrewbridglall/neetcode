class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # memory optimized dp
        N,M = len(profit), capacity
        dp = [0]*(M+1)

        # init first row
        for c in range(M+1):
            if weight[0] <= c:
                dp[c] = profit[0]
        # traverse "grid" - populate currRow given dp
        # row by row, col by col
        for i in range(1, N):
            currRow = [0]*(M+1)
            for c in range(M+1):
                # calc skip
                skip = dp[c]
                # calc include
                include = 0
                if c-weight[i] >= 0:
                    include = profit[i] + dp[c-weight[i]]
                # determine max
                # set cell to max
                currRow[c] = max(skip, include)
            dp = currRow
        # return last index in row
        return dp[M]