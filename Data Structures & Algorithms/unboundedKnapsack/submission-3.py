class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit), capacity
        # memory optimized dp
        dp = [0]*(M+1)
        # true dp soln
        
        # init first row, col
        for c in range(M+1):
            if weight[0] <= c:
                dp[c] = (c//weight[0])*profit[0]
        # traverse grid row by row and col by col
        for i in range(1,N):
            currRow = [0]*(M+1)
            for c in range(1, M+1):
                # calc skip i 
                skip = dp[c]
                # calc include i
                include = 0
                if c-weight[i] >= 0:
                    include = profit[i] + currRow[c-weight[i]]
                # assign max
                currRow[c] = max(skip, include)
            dp = currRow
        # end - return dp n-1 m
        return dp[M]