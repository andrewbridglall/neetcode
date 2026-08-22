class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp - space optimized
        dp = [0]*(n)

        for r in range(m-1, -1 ,-1):
            currRow = [0]*(n)
            currRow[n-1] = 1
            for c in range(n-2, -1, -1):
                currRow[c] = dp[c] + currRow[c+1]
            dp = currRow
        
        return dp[0]